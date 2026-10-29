---
title: "Agent Paper | Concordat: Typed Sessions for LLM Agents"
date: "2026-10-29"
tags: ["Agent", "cs.AI", "cs.MA"]
paper_title: "Concordat: Typed Sessions for LLM Agents"
paper_url: "https://arxiv.org/abs/2610.37461v1"
pdf_url: "https://arxiv.org/pdf/2610.37461v1"
arxiv_id: "2610.37461v1"
authors: "Milad Sikaroudi"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Concordat: Typed Sessions for LLM Agents
- **作者**：Milad Sikaroudi
- **arXiv ID**：2610.37461v1
- **分类**：cs.AI, cs.MA

## 摘要原文

> Agents built on large language models are increasingly allowed to take consequential actions:
> cancelling bookings, issuing refunds, changing accounts. The rules that govern those actions,
> such as "obtain the customer's explicit confirmation before changing anything", are usually
> stated in the prompt and followed only as reliably as the model chooses to follow them. We
> present Concordat, a Python library that treats an agent as an object whose interface is a
> finite-state protocol, in the spirit of typestate and session types, and enforces that protocol
> on the model at run time. On every turn the model is offered only the tools that are legal in
> the current protocol state, calls outside that set are rejected before they have side effects,
> decisions reserved for humans can only be requested, and token and tool-call budgets are charged
> and split linearly across handoffs. Protocols are checked when they are defined, and a subclass
> of an agent is rejected if it could bypass its parent's protocol, a behavioural form of Liskov
> substitution. We evaluate a Concordat agent against the standard agent of tau-bench on its 50
> airline tasks, adding simulated customers who pressure the agent to skip confirmation. The
> standard agent made changes without the required "yes" in 13 of 50 tasks with gpt-4.1 and in 29
> of 128 task-runs with Claude Haiku 5.5; the Concordat agent made none, with no significant
> difference in task success. tau-bench's own reward did not detect most of these violations.
> Concordat is open source.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
