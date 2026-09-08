---
title: "Agent Paper | Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents"
date: "2026-09-08"
tags: ["Agent", "cs.AI", "cs.SE"]
paper_title: "Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents"
paper_url: "https://arxiv.org/abs/2609.05261v1"
pdf_url: "https://arxiv.org/pdf/2609.05261v1"
arxiv_id: "2609.05261v1"
authors: "Jiazheng Sun, Boyu Yang, Binhao Yuan, Mingxuan Li, Xin Peng"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents
- **作者**：Jiazheng Sun, Boyu Yang, Binhao Yuan, Mingxuan Li, Xin Peng
- **arXiv ID**：2609.05261v1
- **分类**：cs.AI, cs.SE

## 摘要原文

> Large language model agents increasingly rely on execution traces to master complex interactive
> tasks. However, current paradigms are bottlenecked by shallow trajectory retrieval and flat
> skill summarization, fundamentally ignoring the temporal dependencies and outcome-conditioned
> topology of agent behavior. We introduce Trace2Tower, a transition-aware EigenTrace framework
> that distills raw trajectories into a robust skill hierarchy. Trace2Tower abstracts step-level
> interactions into canonical events, constructing a unified graph governed by semantic
> compatibility, transition dynamics, and outcome evidence. Through a novel contrastive spectral
> decomposition, it isolates stable, success-aligned behavioral modes while rigorously suppressing
> failure-prone shortcuts. These modes organically populate a dynamic skill tower of action
> templates, procedural routines, and overarching task strategies, continuously refined via
> verifier-guided feedback. On ALFWorld, Trace2Tower achieves 87.31% success requiring only 10.35
> steps and 0.26 invalid actions; on WebShop, it reaches 50.67% exact success. Across both
> benchmarks, Trace2Tower significantly outperforms existing baselines in task mastery and
> context-efficient experience reuse.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
