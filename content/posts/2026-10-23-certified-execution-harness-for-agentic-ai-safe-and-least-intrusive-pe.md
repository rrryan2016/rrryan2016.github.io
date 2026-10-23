---
title: "Agent Paper | Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action"
date: "2026-10-23"
tags: ["Agent", "cs.AI", "eess.SY"]
paper_title: "Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action"
paper_url: "https://arxiv.org/abs/2610.31376v1"
pdf_url: "https://arxiv.org/pdf/2610.31376v1"
arxiv_id: "2610.31376v1"
authors: "Chao Gu, Quanyan Zhu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action
- **作者**：Chao Gu, Quanyan Zhu
- **arXiv ID**：2610.31376v1
- **分类**：cs.AI, eess.SY

## 摘要原文

> This paper studies the problem of safe tool execution for large language model (LLM) agents
> under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and
> its tools as a supervisory control problem, in which marks represent capabilities, approvals and
> budgets. Since a transition fires only if the marks it needs are present, an injected request
> whose preconditions are unmet or already spent is refused regardless of its wording. Treating
> tool outcomes as uncontrollable, we enforce safety by the conventional maximally permissive
> supervisor, and this safety transfers to the running system under four assumptions. Moreover, to
> capture an agent that may propose again after a refusal, we introduce the notion of a replanning
> closed loop, in which each retry costs an inference call. We show that, in this loop, the
> conventional supervisor can be arbitrarily more intrusive than a stricter safe one. Furthermore,
> for a given proposer model, the maximally permissive least-intrusive supervisor is characterized
> as a value-threshold refinement of the conventional one. Under precise conditions, this
> refinement orders two concurrent actions by at most one monitor place. On an autonomous release
> agent, we find by synthesis that safe deployment requires a step that the supervisor can refuse
> after a rollout starts.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
