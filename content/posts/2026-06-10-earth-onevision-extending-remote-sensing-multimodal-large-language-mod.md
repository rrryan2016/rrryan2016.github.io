---
title: "Remote Sensing Paper | Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks"
date: "2026-06-10"
tags: ["Remote Sensing", "cs.CV", "cs.AI"]
paper_title: "Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks"
paper_url: "https://arxiv.org/abs/2606.10819v1"
pdf_url: "https://arxiv.org/pdf/2606.10819v1"
arxiv_id: "2606.10819v1"
authors: "Miaoxin Cai, Guanqun Wang, Wei Zhang, Guangyao Zhou, Yin Zhuang, Tong Zhang, Hao Wang, He Chen, Jun Li"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks
- **作者**：Miaoxin Cai, Guanqun Wang, Wei Zhang, Guangyao Zhou, Yin Zhuang, Tong Zhang et al.
- **arXiv ID**：2606.10819v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> RS-MLLMs enable natural-language understanding and spatial reasoning over earth observation
> imagery. However, existing models support only a narrow range of sensor types and tasks,
> yielding a fragmented view of the earth and leaving cross-modal geoscientific knowledge largely
> unexploited. This work presents Earth-OneVision, a 2B RS-MLLM that unifies six sensor modalities
> (i.e., optical, SAR, infrared, multispectral, temporal, and video) and cross-sensor fusion
> across 9 task categories within a single autoregressive framework. Three dedicated mechanisms
> address three bottlenecks. Full-Granularity Vision-Language Alignment (FGVLA) aligns multi-level
> visual features with the multi-dimensional language space. Spatial-Linguistic Isomorphic
> Serialization (SLIS) unifies heterogeneous spatial outputs as autoregressive tokens. Progressive
> Cross-Modality Adaptation (PCMA) decomposes the compound domain gap into sequential stages,
> tackling the viewpoint and imaging physics gaps in turn. To support joint training, MMRS-
> OneVision is constructed with ~34M QA pairs spanning all six sensor modalities and cross-sensor
> fusion across 9 task categories, substantially exceeding existing RS multimodal instruction
> datasets. With only 2B parameters, Earth-OneVision achieves competitive or state-of-the-art
> results across extensive benchmarks, consistently matching or outperforming 4B-72B RS-MLLMs. It
> achieves 87.52% P@0.5 on the OPT-RSVG testset for optical visual grounding and 80.68% on the SAR
> VQA benchmark SARLANG-Bench, exceeding 7B models by over 7%. It further achieves 75.74% recall
> on the BigEarthNet-MS testset for multispectral classification, and 81.94% MCQ accuracy on
> EarthMind-Bench for cross-modality reasoning.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
