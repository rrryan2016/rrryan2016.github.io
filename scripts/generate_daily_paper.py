#!/usr/bin/env python3
"""Create one daily paper summary post from arXiv."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import socket
import sys
import textwrap
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from build_site import read_simple_yaml, slugify


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config.yaml"
POSTS_DIR = ROOT / "content" / "posts"
ARXIV_API = "https://export.arxiv.org/api/query"


def load_local_env() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def llm_settings(config: dict[str, Any]) -> tuple[str | None, str, str]:
    bot = config.get("paper_bot", {})
    key_env = str(bot.get("api_key_env", "OPENAI_API_KEY"))
    api_key = (
        os.environ.get(key_env)
        or os.environ.get("OPENAI_API_KEY")
        or os.environ.get("LLM_API_KEY")
        or bot.get("api_key")
    )
    model = os.environ.get("OPENAI_MODEL") or str(bot.get("model", "gpt-4.1-mini"))
    base_url = os.environ.get("OPENAI_BASE_URL") or str(bot.get("base_url", "https://api.openai.com/v1"))
    return api_key, base_url.rstrip("/"), model


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def today_local() -> dt.date:
    timezone = os.environ.get("TZ")
    if timezone:
        os.environ["TZ"] = timezone
    return dt.datetime.now().date()


def existing_arxiv_ids() -> set[str]:
    ids: set[str] = set()
    for path in POSTS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        ids.update(re.findall(r"arxiv_id:\s*['\"]?([^'\"\n]+)", text, flags=re.I))
        ids.update(re.findall(r"arxiv\.org/(?:abs|pdf)/([0-9.]+)", text, flags=re.I))
    return ids


def has_post_for_date(post_date: dt.date) -> bool:
    date_text = post_date.isoformat()
    for path in POSTS_DIR.glob("*.md"):
        if path.name.startswith(date_text):
            return True
        text = path.read_text(encoding="utf-8")
        if re.search(rf"(?m)^date:\s*['\"]?{re.escape(date_text)}['\"]?\s*$", text):
            return True
    return False


def fetch_arxiv(query: str, max_results: int, retries: int = 4) -> list[dict[str, Any]]:
    params = {
        "search_query": query,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "PaperRadar/1.0"})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = response.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt >= retries:
                raise
            retry_after = exc.headers.get("Retry-After")
            if retry_after and retry_after.isdigit():
                delay = int(retry_after)
            else:
                delay = 15 * (attempt + 1)
            print(f"arXiv API returned HTTP {exc.code}. Retrying in {delay}s...", file=sys.stderr)
            time.sleep(delay)
        except (TimeoutError, socket.timeout, urllib.error.URLError) as exc:
            if attempt >= retries:
                raise
            delay = 15 * (attempt + 1)
            print(f"arXiv API request failed: {exc}. Retrying in {delay}s...", file=sys.stderr)
            time.sleep(delay)
    else:
        raise RuntimeError("Failed to fetch arXiv results.")

    root = ET.fromstring(payload)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    papers = []
    for entry in root.findall("atom:entry", ns):
        arxiv_id = clean_text(entry.findtext("atom:id", default="", namespaces=ns)).rsplit("/", 1)[-1]
        title = clean_text(entry.findtext("atom:title", default="", namespaces=ns))
        abstract = clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
        published = clean_text(entry.findtext("atom:published", default="", namespaces=ns))
        updated = clean_text(entry.findtext("atom:updated", default="", namespaces=ns))
        authors = [
            clean_text(author.findtext("atom:name", default="", namespaces=ns))
            for author in entry.findall("atom:author", ns)
        ]
        categories = [
            category.attrib.get("term", "")
            for category in entry.findall("atom:category", ns)
            if category.attrib.get("term")
        ]
        pdf_url = ""
        abs_url = ""
        for link in entry.findall("atom:link", ns):
            href = link.attrib.get("href", "")
            if link.attrib.get("title") == "pdf":
                pdf_url = href
            if link.attrib.get("rel") == "alternate":
                abs_url = href
        papers.append(
            {
                "arxiv_id": arxiv_id,
                "title": title,
                "abstract": abstract,
                "published": published,
                "updated": updated,
                "authors": authors,
                "categories": categories,
                "url": abs_url or f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": pdf_url,
            }
        )
    return papers


def paper_score(paper: dict[str, Any], topic_name: str) -> int:
    text = f"{paper['title']} {paper['abstract']}".lower()
    score = 0
    keywords = {
        "Remote Sensing": [
            "remote sensing",
            "earth observation",
            "satellite",
            "hyperspectral",
            "sar",
            "geospatial",
            "foundation model",
            "multimodal",
            "change detection",
            "change caption",
            "change description",
            "vision-language",
            "visual language",
        ],
        "Agent": [
            "agent",
            "tool",
            "planning",
            "multi-agent",
            "large language model",
            "llm",
            "reasoning",
            "workflow",
            "vision-language",
            "multimodal",
        ],
    }
    for keyword in keywords.get(topic_name, []):
        if keyword in text:
            score += 3 if keyword in paper["title"].lower() else 1
    if "benchmark" in text:
        score += 1
    if "survey" in text:
        score -= 2
    if any(category in {"cs.CV", "cs.AI", "cs.CL", "cs.LG"} for category in paper["categories"]):
        score += 1
    return score


def choose_paper(config: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    bot = config.get("paper_bot", {})
    max_candidates = int(bot.get("max_candidates", 20))
    min_title_words = int(bot.get("min_title_words", 4))
    seen = existing_arxiv_ids()

    candidates: list[tuple[int, str, dict[str, Any]]] = []
    for topic in bot.get("topics", []):
        topic_name = str(topic.get("name", "Paper"))
        query = str(topic.get("query", "")).strip()
        if not query:
            continue
        if candidates:
            time.sleep(3)
        for paper in fetch_arxiv(query, max_candidates):
            if paper["arxiv_id"] in seen:
                continue
            if len(paper["title"].split()) < min_title_words:
                continue
            candidates.append((paper_score(paper, topic_name), topic_name, paper))

    if not candidates:
        raise RuntimeError("No new arXiv candidates found. Adjust config.yaml queries or max_candidates.")

    candidates.sort(key=lambda item: (item[0], item[2].get("published", "")), reverse=True)
    _, topic_name, paper = candidates[0]
    return topic_name, paper


def llm_summary(topic: str, paper: dict[str, Any], config: dict[str, Any]) -> str | None:
    api_key, base_url, model = llm_settings(config)
    if not api_key:
        return None

    bot = config.get("paper_bot", {})
    language = str(bot.get("language", "zh-CN"))
    research_context = str(
        bot.get(
            "research_context",
            "我关注遥感图像变化检测、变化描述、遥感 VLM 和面向科研流程的 Agent。",
        )
    )
    application_focus = bot.get("application_focus", [])
    if isinstance(application_focus, list):
        application_focus_text = "\n".join(f"- {item}" for item in application_focus)
    else:
        application_focus_text = f"- {application_focus}"
    endpoint = f"{base_url}/chat/completions"
    prompt = f"""请用{language}写一篇博客式论文摘要，读者是遥感、机器学习和大模型智能体方向的研究者。

要求：
- 标题不要重复论文标题，正文直接从“## 论文速览”开始。
- 使用 Markdown。
- 包含这些二级标题，且顺序保持一致：论文速览、方法要点、实验与结果、为什么值得关注、对我的研究启发、可实践方案、局限与开放问题。
- 不要编造摘要中没有的信息；如果实验细节不足，明确说明 arXiv 摘要未提供。
- 保持专业、克制、信息密度高。
- “对我的研究启发”必须结合下方研究背景，说明这篇论文对遥感变化检测/变化描述/VLM/Agent 工作可能有什么启发；如果论文主题较远，也要明确指出迁移价值有限在哪里。
- “可实践方案”必须给出 3-5 条可以落地到科研中的做法，尽量写成可执行实验设计，例如数据、模型、训练/推理流程、评测指标、消融或 Agent 工作流；不能只写泛泛建议。

我的研究背景：
{research_context}

我希望优先关联这些方向：
{application_focus_text}

主题：{topic}
论文标题：{paper['title']}
作者：{', '.join(paper['authors'])}
分类：{', '.join(paper['categories'])}
arXiv ID：{paper['arxiv_id']}
摘要：{paper['abstract']}
"""
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You write precise Chinese research-paper blog summaries. Never invent facts absent from the abstract.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.35,
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "PaperRadar/1.0",
        },
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result["choices"][0]["message"]["content"].strip()


def fallback_summary(topic: str, paper: dict[str, Any]) -> str:
    authors = ", ".join(paper["authors"][:6])
    if len(paper["authors"]) > 6:
        authors += " et al."
    abstract = paper["abstract"]
    wrapped_abstract = "\n".join(f"> {line}" for line in textwrap.wrap(abstract, width=96))
    return f"""## 论文速览

这篇论文属于 **{topic}** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：{paper['title']}
- **作者**：{authors}
- **arXiv ID**：{paper['arxiv_id']}
- **分类**：{', '.join(paper['categories'])}

## 摘要原文

{wrapped_abstract}

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
"""


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_post(topic: str, paper: dict[str, Any], config: dict[str, Any], date: dt.date) -> tuple[str, str]:
    _, _, model = llm_settings(config)
    try:
        summary = llm_summary(topic, paper, config)
        summary_model = model if summary else "fallback-no-api-key"
    except Exception as exc:
        print(f"LLM generation failed, writing fallback summary: {exc}", file=sys.stderr)
        summary = None
        summary_model = "fallback-llm-error"

    if summary is None:
        summary = fallback_summary(topic, paper)

    title = f"{topic} Paper | {paper['title']}"
    title_slug = slugify(paper["title"])[:70].strip("-")
    slug = f"{date.isoformat()}-{title_slug}"
    filename = f"{slug}.md"
    authors = ", ".join(paper["authors"])
    tags = [topic] + [category for category in paper["categories"][:3] if category != topic]
    front_matter = "\n".join(
        [
            "---",
            f"title: {yaml_quote(title)}",
            f"date: {yaml_quote(date.isoformat())}",
            f"tags: {json.dumps(tags, ensure_ascii=False)}",
            f"paper_title: {yaml_quote(paper['title'])}",
            f"paper_url: {yaml_quote(paper['url'])}",
            f"pdf_url: {yaml_quote(paper.get('pdf_url', ''))}",
            f"arxiv_id: {yaml_quote(paper['arxiv_id'])}",
            f"authors: {yaml_quote(authors)}",
            f"summary_model: {yaml_quote(summary_model)}",
            "---",
            "",
        ]
    )
    return filename, front_matter + summary.strip() + "\n"


def main() -> None:
    load_local_env()
    parser = argparse.ArgumentParser(description="Generate a daily paper summary post.")
    parser.add_argument("--date", help="Post date in YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--dry-run", action="store_true", help="Print the selected paper without writing a post.")
    parser.add_argument("--force", action="store_true", help="Generate even if a post already exists for the date.")
    args = parser.parse_args()

    config = read_simple_yaml(CONFIG_PATH)
    post_date = dt.date.fromisoformat(args.date) if args.date else today_local()
    if has_post_for_date(post_date) and not args.force:
        print(f"Post for {post_date.isoformat()} already exists; skipping.")
        return

    topic, paper = choose_paper(config)

    if args.dry_run:
        print(json.dumps({"topic": topic, "paper": paper}, ensure_ascii=False, indent=2))
        return

    filename, content = build_post(topic, paper, config, post_date)
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    path = POSTS_DIR / filename
    if path.exists():
        raise FileExistsError(path)
    path.write_text(content, encoding="utf-8")
    print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
