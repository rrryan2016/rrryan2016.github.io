---
title: "Agent Paper | SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning"
date: "2026-06-14"
tags: ["Agent", "cs.CV", "cs.AI"]
paper_title: "SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning"
paper_url: "https://arxiv.org/abs/2606.13673v1"
pdf_url: "https://arxiv.org/pdf/2606.13673v1"
arxiv_id: "2606.13673v1"
authors: "Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee, Chan Hee Song, Sifei Liu, Subhashree Radhakrishnan, Seungryong Kim, Yu-Chiang Frank Wang, Min-Hung Chen"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning
- **作者**：Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee, Chan Hee Song et al.
- **arXiv ID**：2606.13673v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Spatial reasoning, the ability to determine where objects are, how they relate, and how they
> move in 3D, remains a fundamental challenge for vision-language models (VLMs). Tool-augmented
> agents attempt to address this by augmenting VLMs with specialist perception modules, yet their
> effectiveness is bounded by the action interface through which those tools are invoked. In this
> work, we study how the design of this interface shapes the agent's capacity for open-ended
> spatial reasoning. Existing spatial agents either employ single-pass code execution, which
> commits to a full analysis strategy before any intermediate result is observed, or rely on a
> structured tool-call interface that often offers less flexibility for freely composing
> operations or tailoring the analysis to each task. Both designs offer limited flexibility for
> open-ended, complex 3D/4D spatial reasoning. We therefore propose SpatialClaw, a training-free
> framework for spatial reasoning that adopts code as the action interface. SpatialClaw maintains
> a stateful Python kernel pre-loaded with input frames and a suite of perception and geometry
> primitives, letting a VLM-backed agent write one executable cell per step conditioned on all
> prior outputs, enabling the agent to flexibly compose and manipulate perception results and
> adapt its analysis to both intermediate text and visual observations and the demands of each
> problem. Evaluated across 20 spatial reasoning benchmarks spanning a broad range of static and
> dynamic 3D/4D spatial reasoning tasks, SpatialClaw achieves 59.9% average accuracy,
> outperforming the recent spatial agent by +11.2 points, with consistent gains across six VLM
> backbones from two model families without any benchmark- or model-specific adaptation.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
