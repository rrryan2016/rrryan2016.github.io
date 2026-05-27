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
- `paper_bot.research_context`：你的长期研究背景，会注入每日摘要 prompt。
- `paper_bot.application_focus`：希望每日文章重点关联的科研方向，例如变化检测、变化描述、VLM 和 Agent。

当前自动选题是轻量筛选，不等同于严格的“顶会/高引用”筛选。脚本会：

- 从 `paper_bot.topics` 中配置的 arXiv 检索式拉取候选论文。
- 跳过已经发布过的 arXiv ID。
- 根据关键词、标题命中、arXiv 类别和是否为 survey 做简单打分。
- 选择得分最高且较新的候选。

如果希望进一步提高来源质量，可以收紧检索式，或在 `scripts/generate_daily_paper.py` 的 `paper_score` 中加入更强的规则，例如优先 `cs.CV/cs.AI/cs.CL`、优先 benchmark/foundation model/VLM/change detection，降低 survey 或纯应用论文权重。

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
<!-- 
   这个 workflow 来自 `.github/workflows/pages.yml`。它会在你向 `main` 分支 push 时自动运行，也可以在 GitHub 网页上手动运行。

   自动运行流程：

   ```bash
   git add .
   git commit -m "Update site"
   git push origin main
   ```

   推送后到仓库页面查看：

   1. 打开 GitHub 仓库。
   2. 进入 `Actions` 标签页。
   3. 点击 `Build and deploy site`。
   4. 等待 `build` 和 `deploy` 两个 job 都变成绿色。

   它实际做的事情是：

   1. Checkout 仓库代码。
   2. 安装 Python 3.12。
   3. 运行 `python scripts/build_site.py`。
   4. 把生成出来的 `site/` 作为 Pages artifact 上传。
   5. 使用 `actions/deploy-pages` 发布到 GitHub Pages。

   部署成功后，在 workflow 的 `deploy` job 里可以看到页面地址。用户站点通常是：

   ```text
   https://<your-user>.github.io/
   ```

   普通项目站点通常是：

   ```text
   https://<your-user>.github.io/<your-repo>/
   ```

   如果 workflow 没有自动运行，检查：

   - 仓库 `Settings -> Pages -> Build and deployment -> Source` 是否选择了 `GitHub Actions`。
   - `.github/workflows/pages.yml` 是否已经提交到 `main`。
   - `Actions` 页面是否提示需要手动启用 workflow。
   - `Settings -> Actions -> General -> Workflow permissions` 是否允许 GitHub Actions 运行。 -->

5. `Generate daily paper` workflow 默认每天多次错峰检查，成功生成当天文章后，后续同日运行会自动跳过。
<!-- 
   这个 workflow 来自 `.github/workflows/daily-paper.yml`。它有两种触发方式：定时自动运行和手动运行。

   定时运行配置如下：

   ```yaml
   schedule:
     - cron: "37 1 * * *"
     - cron: "17 3 * * *"
     - cron: "47 6 * * *"
   ```

   GitHub Actions 的 cron 时间使用 UTC。上面三次分别对应北京时间 09:37、11:17、14:47。多次错峰是为了降低 GitHub schedule 延迟或漏触发的影响；脚本会检测当天是否已经有文章，如果已经存在，就输出 `Post for YYYY-MM-DD already exists; skipping.` 并正常结束。

   手动运行方式：

   1. 打开 GitHub 仓库。
   2. 进入 `Actions` 标签页。
   3. 点击左侧的 `Generate daily paper`。
   4. 点击右侧 `Run workflow`。
   5. 分支选择 `main`。
   6. 再点击绿色的 `Run workflow`。

   首次运行前，需要在 `Settings -> Secrets and variables -> Actions -> Repository secrets` 中添加：

   ```text
   OPENAI_API_KEY
   OPENAI_BASE_URL
   OPENAI_MODEL
   ```

   其中 `OPENAI_API_KEY` 是必须项。`OPENAI_BASE_URL` 和 `OPENAI_MODEL` 如果不填，会使用代码或 `config.yaml` 中的默认值。当前 workflow 会把这些 secrets 注入给脚本：

   ```yaml
   env:
     TZ: Asia/Shanghai
     OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
     OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
     OPENAI_MODEL: ${{ secrets.OPENAI_MODEL }}
   ```

   它实际做的事情是：

   1. Checkout 仓库代码。
   2. 安装 Python 3.12。
   3. 运行 `python scripts/generate_daily_paper.py`，从 arXiv 选择一篇新论文并生成 Markdown。
   4. 运行 `python scripts/build_site.py`，确认新文章能正常构建。
   5. 如果 `content/posts/` 有新增文章，就提交并 push 回 `main`。
   6. 这次 push 会再次触发 `Build and deploy site`，从而发布新文章。

   如果没有配置大模型 key，脚本会生成 fallback 摘要，不会中断整个流程。fallback 文章会保留论文标题、作者、arXiv 链接和原始摘要，后续可以手动编辑。

   如果 `Generate daily paper` 运行失败，优先检查：

   - `Actions` 日志里是否是 arXiv 网络访问失败。
   - `OPENAI_API_KEY` 是否填写到了 `Repository secrets`，不是 `Variables`。
   - `OPENAI_BASE_URL` 是否是 OpenAI 兼容接口，例如 `https://api.openai.com/v1`。
   - `OPENAI_MODEL` 是否是你的接口实际支持的模型名。
   - 仓库 `Settings -> Actions -> General -> Workflow permissions` 是否选择 `Read and write permissions`，否则 workflow 可能无法把新文章 push 回 `main`。 -->

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
