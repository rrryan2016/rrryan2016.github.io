---
title: "Agent Paper | Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash"
date: "2026-10-24"
tags: ["Agent", "cs.SE", "cs.AI", "cs.MA"]
paper_title: "Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash"
paper_url: "https://arxiv.org/abs/2610.31351v1"
pdf_url: "https://arxiv.org/pdf/2610.31351v1"
arxiv_id: "2610.31351v1"
authors: "Atharv Chandratre, Jai Datar"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash
- **作者**：Atharv Chandratre, Jai Datar
- **arXiv ID**：2610.31351v1
- **分类**：cs.SE, cs.AI, cs.MA

## 摘要原文

> Feature flags are runtime configuration mechanisms used for gradual feature rollouts,
> experimentation, and kill switches. Once a feature is fully rolled out, the flag and its gated
> code become technical debt and can introduce operational risk through inadvertently enabling
> dormant code paths. At DoorDash, over 56,000 feature flags span 623 repositories, with 1,659
> currently stale as of May 2026, with internal estimates of one to two hours per manual cleanup.
> Existing rule-based cleanup tools proved insufficient in DoorDash's codebases. Our contribution
> is an end-to-end automated LLM-based feature flag cleanup system that integrates querying live
> feature flag rollout data using MCP, Jira ticket processing, and end-to-end pull request
> creation. Our system successfully produced engineer-approved flag removal PRs for 45 (90%) of
> the 50 stale flags it was evaluated on, proving the system's operational viability at scale with
> each cleanup averaging only $4.79 and 13.8 minutes. We evaluated the system's quality and
> reliability boundary based on success rates, cost per cleanup and time metrics. Furthermore, we
> discuss our lessons learned when architecting this system, to provide practical guidance for
> developing similar multi-agent systems.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
