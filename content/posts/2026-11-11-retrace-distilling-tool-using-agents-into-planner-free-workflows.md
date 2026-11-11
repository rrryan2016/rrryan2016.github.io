---
title: "Agent Paper | ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows"
date: "2026-11-11"
tags: ["Agent", "cs.AI", "cs.LG", "cs.MA"]
paper_title: "ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows"
paper_url: "https://arxiv.org/abs/2611.14492v1"
pdf_url: "https://arxiv.org/pdf/2611.14492v1"
arxiv_id: "2611.14492v1"
authors: "Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows
- **作者**：Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo et al.
- **arXiv ID**：2611.14492v1
- **分类**：cs.AI, cs.LG, cs.MA

## 摘要原文

> Business process automation runs the same Standard Operating Procedure (SOP) again and again on
> new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but
> they call an LLM to choose every step of every run, which adds latency and cost at scale. We
> present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in
> which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes
> with each tool call, often states why it took an action; the tool calls alone do not. ReTrace
> extracts the condition behind each step, merges these conditions across runs into a compact rule
> document, and generates an executable workflow from it. Only this last stage depends on the
> platform, so rule documents can be compiled for different orchestration platforms. On $79$
> procedures from our production platform, ReTrace workflows reach $93.8\%$ completion, against
> $96.8\%$ for the agent, at $24\%$ lower cost per task. On $τ^2$-Bench, they reach $75.8\%$ task
> success (agent: $80.6\%$) and run in $1.3$s instead of $170$s; three rounds of repair on
> training failures lift $k{=}2$ workflows from $66.7\%$ to $81.2\%$. On eight SOP-Bench
> procedures, ReTrace without repair trails few-shot generation ($80.6\%$ vs. $83.6\%$), but
> repair from labeled training failures lifts it to $87.8\%$ at $0.40$s per task, compared to
> $85.5\%$ in $46.6$s for the agent.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
