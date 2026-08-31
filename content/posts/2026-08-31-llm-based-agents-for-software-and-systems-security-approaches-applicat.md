---
title: "Agent Paper | LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment"
date: "2026-08-31"
tags: ["Agent", "cs.CR", "cs.AI"]
paper_title: "LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment"
paper_url: "https://arxiv.org/abs/2608.28490v1"
pdf_url: "https://arxiv.org/pdf/2608.28490v1"
arxiv_id: "2608.28490v1"
authors: "Jingjing Nie, Jiawei Guo, Krishna Meda, Haipeng Cai"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment
- **作者**：Jingjing Nie, Jiawei Guo, Krishna Meda, Haipeng Cai
- **arXiv ID**：2608.28490v1
- **分类**：cs.CR, cs.AI

## 摘要原文

> Software and systems security workflows are typically procedural: analysts inspect heterogeneous
> artifacts, form hypotheses, invoke tools, interpret outputs, and revise plans. Large language
> model (LLM)-based agents, which can plan, use tools, retain state, and revise actions across
> multi-step workflows, are being rapidly adopted to automate this work. Given the consequences of
> delegating security decisions to autonomous systems, understanding how such agents are built,
> used, and assessed is crucial. Yet to this date, there remains a lack of systematic
> understanding of what has been done and how far we are in this field: the term "agent" is
> applied inconsistently, applications differ sharply in risk, and assessment protocols are often
> incomparable. To gain a comprehensive and coherent view of this area hence inform relevant
> future research, this paper provides a systematic literature review of the (1) technical
> approaches, including agent architecture, perception, memory, reasoning and planning, action
> space, orchestration, and self-improvement, (2) applications, with respect to the security tasks
> served, and (3) assessment, including the datasets, outcome and trajectory metrics, safety
> measures, and baselines considered, over the peer-reviewed literature spanning the emergence of
> this area (2023--2026). Our synthesis reveals a field that has built agents able to act but not
> yet agents whose authority is bounded or whose behavior is auditable. In addition to knowledge
> systematization, we also extend our insights into the limitations of and challenges faced by
> current approach, application, and assessment designs, which shed light on potentially promising
> future research directions.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
