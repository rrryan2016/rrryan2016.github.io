---
title: "Agent Paper | MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents"
date: "2026-07-14"
tags: ["Agent", "cs.CV", "cs.AI"]
paper_title: "MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents"
paper_url: "https://arxiv.org/abs/2607.11818v1"
pdf_url: "https://arxiv.org/pdf/2607.11818v1"
arxiv_id: "2607.11818v1"
authors: "Kaixin Ma, Di Feng, Alexander Metz, Jiarui Lu, Eshan Verma, Afshin Dehghan"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents
- **作者**：Kaixin Ma, Di Feng, Alexander Metz, Jiarui Lu, Eshan Verma, Afshin Dehghan
- **arXiv ID**：2607.11818v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-
> calling agents. The framework provides a stateful execution environment spanning 500+ tools
> across 16 application domains, supporting multi-image, multi-turn tasks where agents must ground
> progressively arriving visual inputs into executable tool calls while handling realistic
> conversational phenomena (goal revisions, error corrections, state mutations). An automated
> scenario generation pipeline produces diverse, visually grounded scenarios through information-
> flow-guided planning and multi-stage quality filtering, yielding 258 human-verified nominal
> scenarios and 50 variants targeting interactive UI applications. Evaluating 12 state-of-the-art
> models, from 4B open-weight to frontier proprietary systems, shows that current models still
> lack robust visual tool-calling capability: even the best model achieves below 50% success rate.
> Our failure analysis further reveals that visual precision, not only planning, is a primary
> bottleneck for capable models: 53% of failures stem from incorrect information extraction from
> images despite otherwise correct task workflows. A planning-to-precision crossover emerges with
> scale: smaller models fail at deciding what to do, while larger models fail at perceiving what
> they see, suggesting fundamentally different research directions for improving models at
> different capability levels. The framework and the benchmark are publicly available at
> https://github.com/apple/ml-mmtoolsandbox

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
