---
title: "Agent Paper | Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration"
date: "2026-10-04"
tags: ["Agent", "cs.AI"]
paper_title: "Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration"
paper_url: "https://arxiv.org/abs/2610.02036v1"
pdf_url: "https://arxiv.org/pdf/2610.02036v1"
arxiv_id: "2610.02036v1"
authors: "Xin Heng"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration
- **作者**：Xin Heng
- **arXiv ID**：2610.02036v1
- **分类**：cs.AI

## 摘要原文

> AI agents can each make locally valid decisions yet jointly produce an invalid result. We call
> this the global coherence problem: a failure of shared state, not merely of model intelligence.
> Our Observation-Aliasing Impossibility Theorem gives the exact boundary. A policy can guarantee
> a valid action exactly when all worlds producing the same observation share an admissible
> action. If k indistinguishable worlds require pairwise-disjoint actions, the best randomized
> worst-case success is 1/k; more reasoning, roles, messages, or samples cannot recover the
> missing distinction. A stronger model can reason better within its context, but it cannot see
> beyond it. We then give local-to-global runtime semantics X = (H, C, G, F; D): topology H
> records overlapping scopes; category C governs state-changing actions; groupoid G retains
> reversible translations; sheaf F tests whether local views glue into one world; and minimal
> history D keeps only distinctions that alter legal futures. Models propose; the harness owns
> shared state and governs commit. Nine studies test both the failure and its boundary. On a
> controlled revision benchmark, the same frontier model scores 40/40 when the deciding event is
> visible; when it is hidden, tested arms score 12--17/40, consistent with chance (1/3); restoring
> one authoritative fact returns 40/40. On TeamBench, ordinary teams exceed a shared budget in 5/5
> runs, a visible live count leaves 4/5 violations, and commit enforcement leaves 0/5. In
> tau2-bench Telecom, current-state checks score 0.07 after silent reverts, while the harness
> scores 1.00. Where a conventional solver already owns the complete relevant state, it ties the
> harness as predicted. The counterintuitive conclusion is that local intelligence cannot
> substitute for missing global state.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
