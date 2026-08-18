---
title: "Remote Sensing Paper | SA-GEM: Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning for Efficient Remote Sensing Large Vision-Language Models"
date: "2026-08-18"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "SA-GEM: Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning for Efficient Remote Sensing Large Vision-Language Models"
paper_url: "https://arxiv.org/abs/2608.15075v1"
pdf_url: "https://arxiv.org/pdf/2608.15075v1"
arxiv_id: "2608.15075v1"
authors: "Kexin Ma, Jing Xiao, Bowen Xing, Liang Liao, Chia-Wen Lin"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：SA-GEM: Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning for Efficient Remote Sensing Large Vision-Language Models
- **作者**：Kexin Ma, Jing Xiao, Bowen Xing, Liang Liao, Chia-Wen Lin
- **arXiv ID**：2608.15075v1
- **分类**：cs.CV

## 摘要原文

> RS-LVLMs have advanced multimodal understanding of Earth observation imagery, yet their
> performance is fundamentally constrained by high-resolution processing, as visual token counts
> grow quadratically with linear input resolution while important visual evidence is inherently
> sparse and increasingly diluted across the expanded sequence. Existing token pruning methods
> largely rely on scale-agnostic resolution policies and isolated importance cues, limiting task-
> aligned granularity adaptation and holistic evidence preservation. To address this, we present
> Scale-Adaptive and Geospatial Evidence-Modulated Token Pruning (SA-GEM), a plug-and-play
> framework that unifies task-adaptive token granularity allocation with holistic geospatial token
> importance modulation. Specifically, a lightweight router selects the resolution based on query-
> dependent token granularity, while a token importance modulator jointly models task relevance,
> spatial structure, and local redundancy to preserve holistic geospatial evidence. We show that
> higher resolution is not universally beneficial and, once sufficient granularity is reached,
> token quality matters more than token quantity. Experiments across various benchmarks
> demonstrate that SA-GEM achieves consistent gains in both accuracy and efficiency over existing
> pruning methods. On XLRS-Bench, it surpasses GeoLLaVA-8K by 2.3% in accuracy with a 2.4 times
> total inference speedup.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
