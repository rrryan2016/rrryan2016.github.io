---
title: "Agent Paper | From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems"
date: "2026-11-25"
tags: ["Agent", "cs.MA", "cs.AI"]
paper_title: "From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems"
paper_url: "https://arxiv.org/abs/2611.31063v1"
pdf_url: "https://arxiv.org/pdf/2611.31063v1"
arxiv_id: "2611.31063v1"
authors: "Wenlong Yu, Bingxu Lu, Qilong Wang, Qinghua Hu, Qianru Sun"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems
- **作者**：Wenlong Yu, Bingxu Lu, Qilong Wang, Qinghua Hu, Qianru Sun
- **arXiv ID**：2611.31063v1
- **分类**：cs.MA, cs.AI

## 摘要原文

> In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through
> intermediate messages and compromise final answers. However, outcome-based evaluation obscures
> how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error
> Propagation among Agents (REPA), a structural model that connects measured local responses to
> system-level error propagation. REPA separately estimates input assembly and agent processing
> across multiple error channels, while theoretical analysis relates local modeling errors to
> endpoint prediction error. Experiments span three Qwen base models, six MAS workflows, and ten
> knowledge and reasoning settings in ErrPropBench-10. REPA achieves a mean condition-level
> Spearman correlation of 0.84 across base models, compared with 0.47 for direct regression.
> Controlled experiments also demonstrate its utility for targeted recovery. REPA-guided
> retrieval-augmented generation (RAG) improves accuracy over no retrieval by an average of 19
> percentage points with 16% additional tokens. By linking local agent behavior to system
> susceptibility, REPA provides an interpretable foundation for studying error propagation and
> developing targeted optimization in MAS.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
