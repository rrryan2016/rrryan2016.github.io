# Paper Radar

一个从零开始的静态论文博客：每天自动从 arXiv 选择一篇 Remote Sensing 或 Agent 方向论文，调用 OpenAI 兼容大模型生成中文摘要，并发布到 GitHub Pages。

## 本地使用

生成站点：

```bash
python scripts/build_site.py
```

生成后的静态文件在 `site/`。可以用任意静态服务器预览：

```bash
python -m http.server 8000 -d site
```

手动生成一篇每日论文：

```bash
python scripts/generate_daily_paper.py
python scripts/build_site.py
```

如果未配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，脚本会写入 fallback 摘要，保留论文元数据和 arXiv 摘要，方便后续人工编辑。

验证模型是否可用：

```bash
python scripts/check_llm.py
```

## 配置大模型

在 GitHub 仓库的 `Settings -> Secrets and variables -> Actions` 中添加：

- `OPENAI_API_KEY`：必填，OpenAI 或兼容服务的 API key。
- `OPENAI_BASE_URL`：可选，默认 `https://api.openai.com/v1`。如果使用兼容接口，例如自建网关或第三方服务，在这里填 base URL。
- `OPENAI_MODEL`：可选，覆盖 `config.yaml` 里的 `paper_bot.model`。

本地运行时也可以用环境变量：

```bash
export OPENAI_API_KEY="..."
export OPENAI_BASE_URL="https://api.openai.com/v1"
export OPENAI_MODEL="gpt-4.1-mini"
python scripts/generate_daily_paper.py
```

也可以在本地创建 `.env`，它已经被 `.gitignore` 忽略：

```bash
OPENAI_API_KEY=...
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4.1-mini
```

## 配置站点和选题

编辑 `config.yaml`：

- `site.title`、`site.subtitle`、`site.author`：站点标题、描述和作者。
- `site.base_url`：部署到 GitHub Pages 后建议填写完整地址，例如 `https://your-name.github.io`。
- `paper_bot.topics`：每日论文候选主题，每个主题包含 `name` 和 arXiv API 检索式。
- `paper_bot.max_candidates`：每个主题拉取的候选数。
- `paper_bot.base_url`：OpenAI 兼容接口地址，例如 `https://api.openai.com/v1`。
- `paper_bot.api_key_env`：读取 API key 的环境变量名，默认 `OPENAI_API_KEY`。
- `paper_bot.model`：默认摘要模型。

arXiv 检索式示例：

```yaml
paper_bot:
  topics:
    - name: "Remote Sensing"
      query: 'cat:cs.CV AND (abs:"remote sensing" OR ti:"remote sensing" OR abs:"earth observation")'
    - name: "Agent"
      query: 'cat:cs.AI AND (abs:"agent" OR ti:"agent" OR abs:"tool use")'
```

## GitHub Pages 部署

1. 创建仓库，例如 `your-name.github.io`。
2. 把本目录推送到仓库的 `main` 分支。

   建议在 GitHub 上创建空仓库，不要勾选自动创建 README、`.gitignore` 或 LICENSE。然后在当前项目目录运行：

   ```bash
   git init
   git branch -M main
   git add .
   git status --short
   git commit -m "Initial Paper Radar site"
   git remote add origin https://github.com/<your-user>/<your-repo>.git
   git push -u origin main
   ```

   其中 `<your-user>` 和 `<your-repo>` 替换成你的 GitHub 用户名和仓库名。例如用户站点仓库通常是：

   ```bash
   git remote add origin https://github.com/rrryan2016/rrryan2016.github.io.git
   ```

   如果当前目录已经初始化过 Git，并且已经有 `origin`，只需要确认或修改远程地址：

   ```bash
   git remote -v
   git remote set-url origin https://github.com/<your-user>/<your-repo>.git
   git push -u origin main
   ```

   如果你在 GitHub 上创建仓库时已经生成了 README，首次 push 可能被拒绝。可以先拉取远端内容再推送：

   ```bash
   git pull --rebase origin main --allow-unrelated-histories
   git push -u origin main
   ```

   注意：`.env` 和 `site/` 已经在 `.gitignore` 中，不会被提交。API key 应只放在 `.env` 或 GitHub Actions secrets 中。
3. 在 `Settings -> Pages -> Build and deployment` 中选择 `GitHub Actions`。
4. 推送后 `Build and deploy site` workflow 会生成并部署 `site/`。
5. `Generate daily paper` workflow 默认每天 UTC 00:20 运行，即北京时间 08:20。

## 内容结构

文章保存在 `content/posts/*.md`，格式如下：

```markdown
---
title: "Remote Sensing Paper | Paper title"
date: "2026-05-25"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "Paper title"
paper_url: "https://arxiv.org/abs/..."
arxiv_id: "2601.00001"
authors: "A. Author, B. Author"
summary_model: "gpt-4.1-mini"
---

## 论文速览

正文...
```

## 参考风格

站点信息架构参考 Hexo/NexT 类型博客：顶部导航、文章列表、标签、归档、About、右侧作者与最新文章。实现上使用零依赖 Python 静态生成，方便你之后迁移到 Hexo、Hugo 或 Astro。
