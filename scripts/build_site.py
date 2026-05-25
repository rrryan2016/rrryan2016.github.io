#!/usr/bin/env python3
"""Build the static Paper Radar site."""

from __future__ import annotations

import datetime as dt
import html
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content" / "posts"
SRC_DIR = ROOT / "src"
SITE_DIR = ROOT / "site"
CONFIG_PATH = ROOT / "config.yaml"


@dataclass(frozen=True)
class Post:
    source: Path
    slug: str
    title: str
    date: dt.date
    tags: list[str]
    body_markdown: str
    body_html: str
    excerpt: str
    metadata: dict[str, Any]

    @property
    def url(self) -> str:
        return f"/blog/{self.slug}/"


def parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return ""
    if value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(item.strip()) for item in inner.split(",")]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    try:
        return int(value)
    except ValueError:
        return value


def read_simple_yaml(path: Path) -> dict[str, Any]:
    """Parse the small YAML subset used by this project."""
    data: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, data)]
    pending_key: tuple[int, dict[str, Any], str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]

        if line.startswith("- "):
            item_text = line[2:].strip()
            if not isinstance(parent, list):
                if pending_key is None:
                    raise ValueError(f"List item without parent in {path}: {raw_line}")
                _, pending_parent, key = pending_key
                new_list: list[Any] = []
                pending_parent[key] = new_list
                stack.append((pending_key[0], new_list))
                parent = new_list
            if ":" in item_text and not item_text.startswith(("'", '"')):
                key, value = item_text.split(":", 1)
                item: dict[str, Any] = {key.strip(): parse_scalar(value)}
                parent.append(item)
                stack.append((indent, item))
                pending_key = None
            else:
                parent.append(parse_scalar(item_text))
                pending_key = None
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            parent[key] = parse_scalar(value)
            pending_key = None
        else:
            new_map: dict[str, Any] = {}
            parent[key] = new_map
            stack.append((indent, new_map))
            pending_key = (indent, parent, key)

    return data


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Front matter started but never closed.")
    metadata_text = text[4:end]
    body = text[end + 5 :].lstrip()
    metadata: dict[str, Any] = {}
    for raw_line in metadata_text.splitlines():
        if not raw_line.strip():
            continue
        key, value = raw_line.split(":", 1)
        metadata[key.strip()] = parse_scalar(value)
    return metadata, body


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", value.lower()).strip("-")
    return slug or "post"


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def flush_paragraph(lines: list[str], output: list[str]) -> None:
    if not lines:
        return
    output.append(f"<p>{inline_markdown(' '.join(lines))}</p>")
    lines.clear()


def markdown_to_html(markdown: str) -> str:
    output: list[str] = []
    paragraph: list[str] = []
    list_stack: list[str] = []
    in_code = False
    code_lines: list[str] = []

    def close_lists() -> None:
        while list_stack:
            output.append(f"</{list_stack.pop()}>")

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                flush_paragraph(paragraph, output)
                close_lists()
                in_code = True
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_paragraph(paragraph, output)
            close_lists()
            continue

        heading = re.match(r"^(#{2,4})\s+(.+)$", line)
        if heading:
            flush_paragraph(paragraph, output)
            close_lists()
            level = len(heading.group(1))
            output.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            continue

        quote_match = re.match(r"^>\s*(.+)$", line)
        if quote_match:
            flush_paragraph(paragraph, output)
            close_lists()
            output.append(f"<blockquote><p>{inline_markdown(quote_match.group(1))}</p></blockquote>")
            continue

        unordered = re.match(r"^[-*]\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph(paragraph, output)
            list_type = "ul" if unordered else "ol"
            if not list_stack or list_stack[-1] != list_type:
                close_lists()
                output.append(f"<{list_type}>")
                list_stack.append(list_type)
            item = unordered.group(1) if unordered else ordered.group(1)
            output.append(f"<li>{inline_markdown(item)}</li>")
            continue

        close_lists()
        paragraph.append(line.strip())

    flush_paragraph(paragraph, output)
    while list_stack:
        output.append(f"</{list_stack.pop()}>")
    if in_code:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(output)


def excerpt_from_markdown(markdown: str, length: int = 180) -> str:
    text = re.sub(r"```.*?```", "", markdown, flags=re.S)
    text = re.sub(r"^#+\s+", "", text, flags=re.M)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`>#-]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= length:
        return text
    return text[:length].rstrip() + "..."


def load_posts() -> list[Post]:
    posts: list[Post] = []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(text)
        date_value = str(metadata.get("date") or path.name[:10])
        post_date = dt.date.fromisoformat(date_value)
        title = str(metadata.get("title") or path.stem)
        tags = metadata.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        slug = str(metadata.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem))
        posts.append(
            Post(
                source=path,
                slug=slugify(slug),
                title=title,
                date=post_date,
                tags=[str(tag) for tag in tags],
                body_markdown=body,
                body_html=markdown_to_html(body),
                excerpt=excerpt_from_markdown(body),
                metadata=metadata,
            )
        )
    return sorted(posts, key=lambda post: (post.date, post.slug), reverse=True)


def site_url(path: str, config: dict[str, Any]) -> str:
    base = str(config["site"].get("base_url") or "").rstrip("/")
    if not path.startswith("/"):
        path = "/" + path
    return base + path if base else path


def page_shell(title: str, content: str, config: dict[str, Any], posts: list[Post]) -> str:
    site = config["site"]
    full_title = site["title"] if title == site["title"] else f"{title} | {site['title']}"
    latest_posts = posts[:6]
    all_tags = sorted({tag for post in posts for tag in post.tags})
    nav = [
        ("/", "Home"),
        ("/blog/", "Blog"),
        ("/tags/", "Tags"),
        ("/archives/", "Archives"),
        ("/about/", "About"),
    ]
    nav_html = "\n".join(f'<a href="{href}">{label}</a>' for href, label in nav)
    latest_html = "\n".join(
        f'<li><a href="{post.url}">{html.escape(post.title)}</a></li>' for post in latest_posts
    )
    tag_html = "\n".join(
        f'<a class="tag" href="/tags/{quote(tag)}/">{html.escape(tag)}</a>' for tag in all_tags
    )
    year = dt.date.today().year
    return f"""<!doctype html>
<html lang="{html.escape(str(site.get("language", "zh-CN")))}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(full_title)}</title>
  <meta name="description" content="{html.escape(str(site.get("description", "")))}">
  <link rel="stylesheet" href="/assets/styles.css">
  <link rel="alternate" type="application/rss+xml" title="{html.escape(str(site["title"]))}" href="/feed.xml">
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="/">
        <span class="brand-title">{html.escape(str(site["title"]))}</span>
        <span class="brand-subtitle">{html.escape(str(site.get("subtitle", "")))}</span>
      </a>
      <nav class="nav" aria-label="Primary navigation">
        {nav_html}
      </nav>
    </div>
  </header>
  <div class="layout">
    <main class="main">
      {content}
    </main>
    <aside class="sidebar" aria-label="Sidebar">
      <section class="sidebar-card">
        <h2>About</h2>
        <p>{html.escape(str(site.get("description", "")))}</p>
        <p>Author: {html.escape(str(site.get("author", "")))}</p>
      </section>
      <section class="sidebar-card">
        <h2>Latest</h2>
        <ul class="sidebar-list">
          {latest_html}
        </ul>
      </section>
      <section class="sidebar-card">
        <h2>Topics</h2>
        <div class="tag-row">
          {tag_html}
        </div>
      </section>
    </aside>
  </div>
  <footer class="footer">
    <span>&copy; {year} {html.escape(str(site.get("author", "")))}.</span>
    <span> Built by Paper Radar.</span>
  </footer>
</body>
</html>
"""


def post_card(post: Post) -> str:
    tags = "".join(f'<a class="tag" href="/tags/{quote(tag)}/">{html.escape(tag)}</a>' for tag in post.tags)
    return f"""<article class="post-card">
  <h2><a href="{post.url}">{html.escape(post.title)}</a></h2>
  <div class="meta">{post.date.isoformat()} · {html.escape(", ".join(post.tags))}</div>
  <p class="excerpt">{html.escape(post.excerpt)}</p>
  <div class="tag-row">{tags}</div>
</article>"""


def render_index(posts: list[Post], config: dict[str, Any]) -> str:
    cards = "\n".join(post_card(post) for post in posts[:10]) or '<div class="empty">还没有文章。</div>'
    content = f"""<section class="hero-visual" aria-label="Paper Radar">
  <img src="/assets/paper-radar-cover.png" alt="">
</section>
<section class="post-list">
  {cards}
</section>"""
    return page_shell(str(config["site"]["title"]), content, config, posts)


def render_blog(posts: list[Post], config: dict[str, Any]) -> str:
    cards = "\n".join(post_card(post) for post in posts) or '<div class="empty">还没有文章。</div>'
    return page_shell("Blog", f'<section class="post-list">{cards}</section>', config, posts)


def paper_box(post: Post) -> str:
    fields = [
        ("Paper", post.metadata.get("paper_title")),
        ("Authors", post.metadata.get("authors")),
        ("Link", post.metadata.get("paper_url")),
        ("Model", post.metadata.get("summary_model")),
    ]
    rows = []
    for label, value in fields:
        if not value:
            continue
        value_text = str(value)
        if label == "Link":
            value_html = f'<a href="{html.escape(value_text)}">{html.escape(value_text)}</a>'
        else:
            value_html = html.escape(value_text)
        rows.append(f"<dt>{label}</dt><dd>{value_html}</dd>")
    if not rows:
        return ""
    return f'<div class="paper-box"><dl>{"".join(rows)}</dl></div>'


def render_post(post: Post, posts: list[Post], config: dict[str, Any]) -> str:
    tags = "".join(f'<a class="tag" href="/tags/{quote(tag)}/">{html.escape(tag)}</a>' for tag in post.tags)
    content = f"""<article class="post">
  <h1>{html.escape(post.title)}</h1>
  <div class="meta">{post.date.isoformat()} · {html.escape(", ".join(post.tags))}</div>
  <div class="tag-row">{tags}</div>
  {paper_box(post)}
  <div class="post-body">
    {post.body_html}
  </div>
</article>"""
    return page_shell(post.title, content, config, posts)


def render_tags(posts: list[Post], config: dict[str, Any]) -> dict[str, str]:
    pages: dict[str, str] = {}
    tags = sorted({tag for post in posts for tag in post.tags})
    tag_links = "\n".join(
        f'<a class="tag" href="/tags/{quote(tag)}/">{html.escape(tag)} ({sum(tag in post.tags for post in posts)})</a>'
        for tag in tags
    )
    pages["tags/index.html"] = page_shell("Tags", f'<article class="post"><h1>Tags</h1><div class="tag-row">{tag_links}</div></article>', config, posts)

    for tag in tags:
        tagged_posts = [post for post in posts if tag in post.tags]
        cards = "\n".join(post_card(post) for post in tagged_posts)
        pages[f"tags/{quote(tag)}/index.html"] = page_shell(
            f"Tag: {tag}",
            f'<section class="post-list"><article class="post-card"><h2>Tag: {html.escape(tag)}</h2></article>{cards}</section>',
            config,
            posts,
        )
    return pages


def render_archives(posts: list[Post], config: dict[str, Any]) -> str:
    items = "\n".join(
        f"""<div class="archive-item">
  <div class="archive-date">{post.date.isoformat()}</div>
  <div><a href="{post.url}">{html.escape(post.title)}</a></div>
</div>"""
        for post in posts
    )
    return page_shell("Archives", f'<article class="post"><h1>Archives</h1><div class="archive-list">{items}</div></article>', config, posts)


def render_about(posts: list[Post], config: dict[str, Any]) -> str:
    site = config["site"]
    topics = config.get("paper_bot", {}).get("topics", [])
    topic_items = "".join(f"<li>{html.escape(str(topic.get('name', 'Topic')))}</li>" for topic in topics)
    content = f"""<article class="post">
  <h1>About</h1>
  <div class="post-body">
    <p>{html.escape(str(site.get("description", "")))}</p>
    <h2>关注方向</h2>
    <ul>{topic_items}</ul>
    <h2>生成方式</h2>
    <p>本站文章以 Markdown 保存，静态页面由本仓库脚本生成。每日论文摘要可通过 GitHub Actions 调用配置的大模型接口自动生成。</p>
  </div>
</article>"""
    return page_shell("About", content, config, posts)


def render_feed(posts: list[Post], config: dict[str, Any]) -> str:
    site = config["site"]
    base_url = str(site.get("base_url") or "").rstrip("/")
    items = []
    for post in posts[:20]:
        link = f"{base_url}{post.url}" if base_url else post.url
        pub_date = dt.datetime.combine(post.date, dt.time(0, 0), tzinfo=dt.timezone.utc)
        items.append(
            f"""<item>
  <title>{xml_escape(post.title)}</title>
  <link>{xml_escape(link)}</link>
  <guid>{xml_escape(link)}</guid>
  <pubDate>{pub_date.strftime("%a, %d %b %Y %H:%M:%S %z")}</pubDate>
  <description>{xml_escape(post.excerpt)}</description>
</item>"""
        )
    return f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>{xml_escape(str(site["title"]))}</title>
  <link>{xml_escape(base_url or "/")}</link>
  <description>{xml_escape(str(site.get("description", "")))}</description>
  {''.join(items)}
</channel>
</rss>
"""


def render_sitemap(posts: list[Post], config: dict[str, Any]) -> str:
    urls = ["/", "/blog/", "/tags/", "/archives/", "/about/"] + [post.url for post in posts]
    base_url = str(config["site"].get("base_url") or "").rstrip("/")
    entries = "\n".join(
        f"  <url><loc>{xml_escape((base_url + url) if base_url else url)}</loc></url>" for url in urls
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
"""


def write_file(relative_path: str, content: str) -> None:
    path = SITE_DIR / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    config = read_simple_yaml(CONFIG_PATH)
    posts = load_posts()

    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    (SITE_DIR / "assets").mkdir(parents=True)
    shutil.copyfile(SRC_DIR / "styles.css", SITE_DIR / "assets" / "styles.css")
    assets_dir = SRC_DIR / "assets"
    if assets_dir.exists():
        for asset in assets_dir.iterdir():
            if asset.is_file():
                shutil.copyfile(asset, SITE_DIR / "assets" / asset.name)

    write_file("index.html", render_index(posts, config))
    write_file("blog/index.html", render_blog(posts, config))
    write_file("archives/index.html", render_archives(posts, config))
    write_file("about/index.html", render_about(posts, config))
    for post in posts:
        write_file(f"blog/{post.slug}/index.html", render_post(post, posts, config))
    for relative_path, content in render_tags(posts, config).items():
        write_file(relative_path, content)
    write_file("feed.xml", render_feed(posts, config))
    write_file("sitemap.xml", render_sitemap(posts, config))
    write_file(".nojekyll", "")

    print(f"Built {len(posts)} posts into {SITE_DIR}")


if __name__ == "__main__":
    main()
