---
title: "Agent Paper | Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits"
date: "2026-10-13"
tags: ["Agent", "cs.AI"]
paper_title: "Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits"
paper_url: "https://arxiv.org/abs/2610.13494v1"
pdf_url: "https://arxiv.org/pdf/2610.13494v1"
arxiv_id: "2610.13494v1"
authors: "Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu, Song Han, Sihao Liu, Ligeng Zhu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits
- **作者**：Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li et al.
- **arXiv ID**：2610.13494v1
- **分类**：cs.AI

## 摘要原文

> Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often
> use context engineering, implemented through custom harnesses that manage tools, skills, and
> accumulated experience. However, we find that as single-session execution lengthens, the agent's
> reasoning intensity declines alongside slowing progress, summarized as long-horizon
> deceleration, and the benefits of these custom harnesses vanish as the underlying model
> improves, summarized as harness staleness. These findings suggest that their benefits may not
> persist across versions, which motivates a workflow-level approach in which agents build on one
> another's work across sessions. We model these alternating agent sessions as a context-reset
> semi-Markov decision process (CR-SMDP) and establish sufficient conditions for alternation to
> exceed single-agent reference limits, derive an explicit experiment-budget bound, and
> characterize when session caps preserve this advantage. Guided by this analysis, we introduce
> Humanize MLE Agents (HMA), which alternates two agents on a shared workspace, limits each
> session to at most k experiments and resets the context between sessions, without additional
> task-specific harness or prior knowledge supplements. Across 75 Kaggle tasks in MLE-bench, HMA
> reaches a state-of-the-art any-medal rate of 78.2%, exceeding the strongest open-source baseline
> by 8.0 points with a quarter of its time budget. Moreover, among six configurations spanning
> five heterogeneous agent pairs, HMA improves any-medal rate over the constituent baselines by
> 6.4 points on average, demonstrating cross-pair generality. A supplementary case on kernel
> optimization reaches 878 cycles, within 1.6% of the community leaderboard leader, demonstrating
> applicability beyond MLE.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
