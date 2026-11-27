---
title: "Remote Sensing Paper | WINSO: A Large-Size Very-High-Resolution Remote Sensing Dataset for Wind Turbine Detection and Solar Panel Segmentation"
date: "2026-11-28"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "WINSO: A Large-Size Very-High-Resolution Remote Sensing Dataset for Wind Turbine Detection and Solar Panel Segmentation"
paper_url: "https://arxiv.org/abs/2611.27241v1"
pdf_url: "https://arxiv.org/pdf/2611.27241v1"
arxiv_id: "2611.27241v1"
authors: "Di Wang, Ke Li, Zhaokun Li, Weiping Ni, Junzheng Wu, Yahu Liu, Quan Wang, Xinbo Gao"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：WINSO: A Large-Size Very-High-Resolution Remote Sensing Dataset for Wind Turbine Detection and Solar Panel Segmentation
- **作者**：Di Wang, Ke Li, Zhaokun Li, Weiping Ni, Junzheng Wu, Yahu Liu et al.
- **arXiv ID**：2611.27241v1
- **分类**：cs.CV

## 摘要原文

> Wind and solar energy are central to the global transition toward net-zero emissions and
> sustainable development. Accurate spatial inventories of wind and solar facilities are essential
> for future energy planning. Satellite remote sensing provides a practical and efficient means to
> acquire such geospatial data at scale. However, reliable facility mapping from large-size
> satellite images remains constrained by the scarcity of carefully annotated datasets and the
> lack of systematic evaluation protocols. To address these limitations, we introduce
> \textbf{WINSO}, a large-scale wind and solar benchmark based on very-high-resolution (VHR)
> satellite imagery with ground sampling distances (GSDs) of 0.5--0.7\,m. WINSO comprises 10,962
> large-size images sampled from diverse geographic locations across the Asia-Pacific region,
> covering at least 71,600\,$\text{km}^2$ and totaling 286.36 gigapixels, with individual image
> dimensions reaching 44,032$\times$62,208 pixels. Through manual annotation and expert
> verification, a total of 166,473 instances are labeled using horizontal bounding boxes (HBBs)
> for wind turbines and polygon masks for solar panels. To build baselines for clean-energy
> facility mapping, we evaluate state-of-the-art detection and segmentation models, specialized
> ultra-high-resolution (UHR) architectures, and vision-language models across different inference
> strategies. Furthermore, cross-dataset evaluations on two external public datasets illustrate
> the strong generalization capability of the WINSO. WINSO establishes a standardized benchmark to
> advance automated clean-energy mapping, paving the way for wide-area monitoring of the clean-
> energy transition.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
