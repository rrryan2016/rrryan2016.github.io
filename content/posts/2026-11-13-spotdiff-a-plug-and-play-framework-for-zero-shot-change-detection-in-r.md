---
title: "Remote Sensing Paper | SpotDiff: A Plug-and-Play Framework for Zero-Shot Change Detection in Remote Sensing Imagery"
date: "2026-11-13"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "SpotDiff: A Plug-and-Play Framework for Zero-Shot Change Detection in Remote Sensing Imagery"
paper_url: "https://arxiv.org/abs/2611.17172v1"
pdf_url: "https://arxiv.org/pdf/2611.17172v1"
arxiv_id: "2611.17172v1"
authors: "Anit Upadhyaya, Ata Akbari Asanjan, Chaitanya Jalluri, Subash Yeggina, Jeremy Kravitz"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：SpotDiff: A Plug-and-Play Framework for Zero-Shot Change Detection in Remote Sensing Imagery
- **作者**：Anit Upadhyaya, Ata Akbari Asanjan, Chaitanya Jalluri, Subash Yeggina, Jeremy Kravitz
- **arXiv ID**：2611.17172v1
- **分类**：cs.CV

## 摘要原文

> Remote sensing change detection usually relies on large collections of temporally aligned,
> pixel-level annotations, which limits its scalability across regions, imaging platforms and
> application domains. Recent zero-shot approaches reduce the need for supervision, but they often
> localize fine-grained changes poorly because their features are coarse or inconsistent across
> time. We present SpotDiff, a training-free, plug-and-play framework for zero-shot change
> detection built by composing complementary vision foundation models. SpotDiff uses DINOv3 for
> semantically robust features, AnyUp to reconstruct them at pixel resolution, and SAM 3 for text-
> guided region-of-interest proposals, which an inference-time multi-scale strategy (SWIMS) makes
> reliable on small objects. Change is then measured by comparing the reconstructed features of
> the two dates inside the proposed regions, with no learnable components, fine-tuning or change
> labels. To our knowledge, SpotDiff is the first change detection method to use a universal
> feature upsampler, which alone adds 13.8 F1 over bilinear upsampling of the same features. On
> LEVIR-CD, SpotDiff reaches 82.46 F1, 2.06 points above the strongest prior training-free method,
> and on the multi-class SECOND benchmark it improves building change detection by 10.3 IoU and
> the six-class average by 2.2 IoU. Qualitative results on PlanetScope (3 m) and Sentinel-2 (10 m)
> imagery show that the same pipeline transfers across resolutions without modification. Our
> results indicate that composing modern foundation models is an effective route to scalable,
> label-free change detection.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
