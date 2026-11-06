---
title: "Remote Sensing Paper | When GeoFMs Meet VHR: Benchmarking Foundation Models on Very High Resolution Earth Observation Imagery"
date: "2026-11-06"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "When GeoFMs Meet VHR: Benchmarking Foundation Models on Very High Resolution Earth Observation Imagery"
paper_url: "https://arxiv.org/abs/2611.08003v1"
pdf_url: "https://arxiv.org/pdf/2611.08003v1"
arxiv_id: "2611.08003v1"
authors: "Kshitij Raj Sharma, Pierre Adorni, Minh-Tan Pham, Dirk Tiede, Sébastien Lefèvre"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：When GeoFMs Meet VHR: Benchmarking Foundation Models on Very High Resolution Earth Observation Imagery
- **作者**：Kshitij Raj Sharma, Pierre Adorni, Minh-Tan Pham, Dirk Tiede, Sébastien Lefèvre
- **arXiv ID**：2611.08003v1
- **分类**：cs.CV

## 摘要原文

> Geospatial foundation models are a widely adopted starting point for remote sensing tasks. Most
> are pretrained on Sentinel-1/2 and Landsat imagery at a ground sampling distance (GSD) of 10m or
> coarser. Many applications instead rely on very high resolution (VHR) imagery, where individual
> buildings, roads, and amenities are resolved. We study which pretraining regimes transfer well
> to this scale. We introduce VHR-Bench, a benchmark suite of ten datasets at 1.5m GSD or finer
> spanning five task families, eight application domains, and both satellite and aerial platforms.
> We evaluate twelve encoders in three pretraining tiers with frozen backbones at two training-
> data fractions. We find that both pretraining on large natural-image collections and VHR-
> specific pretraining transfer effectively to VHR tasks, with complementary strengths. SkySense
> leads when labels are scarce; at the full label fraction the web-pretrained DINOv3 ViT-L edges
> ahead, with the two close together there. Encoders pretrained only on Sentinel-scale imagery
> transfer least well under RGB input. Guided by these complementary results, we continue the
> self-supervised pretraining of DINOv3 ViT-L on 1.02 million held-out VHR tiles and evaluate the
> resulting encoder without changing the downstream protocol. The continued model gives a clear
> improvement over the released backbone when labels are scarce and a modest one at the full
> fraction, at no increase in inference parameters or compute. These findings support a
> generalize-then-specialize strategy: already strong, broad natural-image pretraining can be
> further improved by a short VHR continuation stage while preserving its general visual features.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
