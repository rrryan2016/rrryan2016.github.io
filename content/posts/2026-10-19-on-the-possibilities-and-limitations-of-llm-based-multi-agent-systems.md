---
title: "Agent Paper | On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management"
date: "2026-10-19"
tags: ["Agent", "math.OC", "cs.AI", "cs.MA"]
paper_title: "On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management"
paper_url: "https://arxiv.org/abs/2610.23673v1"
pdf_url: "https://arxiv.org/pdf/2610.23673v1"
arxiv_id: "2610.23673v1"
authors: "Marco Boresta, Tommaso Giovannelli, Sepehr Namirad, Giulia Riccardi"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria decision-making in healthcare operations management
- **作者**：Marco Boresta, Tommaso Giovannelli, Sepehr Namirad, Giulia Riccardi
- **arXiv ID**：2610.23673v1
- **分类**：math.OC, cs.AI, cs.MA

## 摘要原文

> Multi-criteria models for healthcare operations need weights that express how stakeholders trade
> off patient waiting time, provider workload, and operating cost, but these weights are difficult
> to quantify. Teams of large language model (LLM) agents, each prompted to represent a
> stakeholder, have been used to supply them. We propose a framework for assessing the reliability
> of LLM-generated preferences as inputs to multi-objective optimization and quantifying how their
> uncertainty affects decisions. We study explicit preferences by asking agents to rate the
> importance of the criteria in an outpatient appointment scheduling problem, and implicit
> preferences by inferring trade-offs from the agents' pairwise choices between emergency
> department configurations. The computational experiments show that the explicit preferences
> respond to the clinic's operating conditions and differ across roles, but deliberation among the
> agents can erase these differences, whereas simple averaging preserves them. The pairwise
> choices used to reveal the agents' implicit preferences depend largely on which option is
> presented first, and we find limited evidence that a statistical model using contextual
> information alongside presentation order predicts the agents' choices on new comparison pairs
> better than a model using presentation order alone. We then formulate robust weighted-sum
> optimization models to account for preference uncertainty. In most cases, these models select
> different schedules or configurations from those obtained using average preference weights.
> These results indicate that LLM-generated preferences need an audit of this kind before they are
> used as optimization weights in healthcare decision support.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
