---
title: "Remote Sensing Paper | Towards Label-Efficient Geospatial Foundation Model Adaptation via Positive-Unlabeled Learning for Building Damage Mapping"
date: "2026-11-09"
tags: ["Remote Sensing", "cs.CV", "cs.AI"]
paper_title: "Towards Label-Efficient Geospatial Foundation Model Adaptation via Positive-Unlabeled Learning for Building Damage Mapping"
paper_url: "https://arxiv.org/abs/2611.08561v1"
pdf_url: "https://arxiv.org/pdf/2611.08561v1"
arxiv_id: "2611.08561v1"
authors: "Hengwei Zhao, Qirui Wang, Zhuo Zheng, Xiaoyan Lu, Rusty Feagin, Wenzhe Jiao"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Towards Label-Efficient Geospatial Foundation Model Adaptation via Positive-Unlabeled Learning for Building Damage Mapping
- **作者**：Hengwei Zhao, Qirui Wang, Zhuo Zheng, Xiaoyan Lu, Rusty Feagin, Wenzhe Jiao
- **arXiv ID**：2611.08561v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Geospatial foundation models (GFMs) are reshaping remote sensing by shifting the field from
> task-specific modeling toward general-purpose geospatial intelligence. Mapping the damage to
> buildings stands to benefit substantially from this shift, as GFMs pretrained on large-scale
> Earth observation data provide generalizable geospatial representations that can facilitate
> effective responses to sudden-onset disasters. Although parameter-efficient fine-tuning (PEFT)
> facilitates GFM adaptation, parameter efficiency does not necessarily translate into label
> efficiency. Building damage mapping remains challenging due to scarce pre-existing labeled data
> or limited time for annotation. When weak supervision is introduced to alleviate the labeling
> bottleneck, we identify the difficulty of learning sufficiently discriminative representations
> as a key challenge for label-efficient GFM adaptation. To address this challenge, we propose a
> Positive-Unlabeled GFM Adaptation (PUMA) framework that requires annotations for only a small
> number of damaged buildings. More specifically, PUMA integrates non-contrastive weakly
> supervised representation refinement to mitigate the impact of noisy supervision on
> representation learning from a gradient perspective, and latent-state-based label disambiguation
> to enable reversible supervision refinement without requiring class prior estimation. Extensive
> experiments on disaster benchmark datasets from around the world demonstrated the effectiveness
> and robustness of PUMA. A real-world application to the 2025 Los Angeles wildfires further
> highlighted its potential to accurately map damage under highly limited supervision. More
> broadly, these findings suggest that weakly supervised PEFT offers a label-efficient pathway
> from GFMs to real-world applications.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
