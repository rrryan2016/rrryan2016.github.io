---
title: "Agent Paper | Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks"
date: "2026-07-24"
tags: ["Agent", "cs.AI", "cs.CL"]
paper_title: "Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks"
paper_url: "https://arxiv.org/abs/2607.21482v1"
pdf_url: "https://arxiv.org/pdf/2607.21482v1"
arxiv_id: "2607.21482v1"
authors: "Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd, David Bann"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks
- **作者**：Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd et al.
- **arXiv ID**：2607.21482v1
- **分类**：cs.AI, cs.CL

## 摘要原文

> Large language models (LLMs) and agents are now widely used tools in code development, with data
> typically sent to third-party cloud-based models. Their adoption in research using personal data
> is constrained by governance requirements that typically prohibit data transmission to external
> services. Locally deployable open-weight models offer an alternative since sensitive data never
> leave the local environment. We introduce an open-source framework for evaluating the efficacy
> of AI agents powered by open-weight LLMs on one of the most persistent bottlenecks in research
> on longitudinal population studies: data preparation. The framework comprises: a curated ground-
> truth dataset (cleaning scripts preparing six sweeps of data from a British cohort study), task
> definitions encompassing tasks such as category harmonization and multi-wave merging, and
> automated routines for evaluating the LLM-produced R code and outputted data. We benchmark LLMs
> across the (consumer grade) deployment spectrum to assess their efficacy in 20 data preparation
> tasks (creation of 102 variables). Current state-of-the-art, 31-35B parameter models almost
> saturated our benchmark ("average task completion" up to 87.9%). The performance of open-weight
> LLMs running on consumer-grade hardware shows promise of a viable path toward AI-assisted data
> preparation in governance-restricted research settings. Our framework is publicly available at:
> https://github.com/UCL-ARC/RRBench.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
