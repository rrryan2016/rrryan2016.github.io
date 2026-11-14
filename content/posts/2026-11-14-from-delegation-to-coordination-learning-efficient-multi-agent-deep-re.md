---
title: "Agent Paper | From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research"
date: "2026-11-14"
tags: ["Agent", "cs.MA", "cs.AI"]
paper_title: "From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research"
paper_url: "https://arxiv.org/abs/2611.17041v1"
pdf_url: "https://arxiv.org/pdf/2611.17041v1"
arxiv_id: "2611.17041v1"
authors: "Yuyang Wu, Yang Liu, Zequn Xie, Junjie Wang, Dan Yang, Zehao Tan, Ding-Chu Zhang, Junming Yang, Yue Shen, Jian Wang, Jinjie Gu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research
- **作者**：Yuyang Wu, Yang Liu, Zequn Xie, Junjie Wang, Dan Yang, Zehao Tan et al.
- **arXiv ID**：2611.17041v1
- **分类**：cs.MA, cs.AI

## 摘要原文

> Multi-agent deep-research systems use delegation to parallelize search and keep long tool traces
> out of the main agent's context. Yet delegation helps only when task allocation and subtask
> execution are coordinated: the main agent must issue useful subtasks, while subagents must
> return reliable evidence. Existing training either optimizes only the main agent or broadcasts
> the same team advantage to all agents, which can reward misleading subagent reports and penalize
> useful ones. We introduce LEAD-RL (Learning Effective Agent Delegation with Reinforcement
> Learning), a joint main-agent-subagent training framework with contribution-aware credit
> assignment. A training-time rubric evaluates the research utility of each subagent report and
> gates its inherited team advantage, while final-answer correctness remains the only team reward;
> no token, step, or speedup reward is used. Across five benchmarks and two model families, LEAD-
> RL improves answer quality. On BrowseComp, it improves accuracy by 2.49 percentage points and
> reduces critical-path cost by 24.5% over joint training with shared team credit. During
> validation, accuracy increases by 6.78 points at approximately constant critical-path cost.
> These results show that contribution-aware credit assignment improves the quality-efficiency
> trade-off of multi-agent deep research.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
