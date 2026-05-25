---
title: "Remote Sensing Paper | SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining"
date: "2026-05-25"
tags: ["Remote Sensing", "cs.CV", "cs.LG"]
paper_title: "SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining"
paper_url: "https://arxiv.org/abs/2605.21075v1"
pdf_url: "https://arxiv.org/pdf/2605.21075v1"
arxiv_id: "2605.21075v1"
authors: "Nassim Ait Ali Braham, Aaron Banze, Conrad M. Albrecht, Julien Mairal, Jocelyn Chanussot, Xiao Xiang Zhu"
summary_model: "fallback-no-api-key"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining
- **作者**：Nassim Ait Ali Braham, Aaron Banze, Conrad M. Albrecht, Julien Mairal, Jocelyn Chanussot, Xiao Xiang Zhu
- **arXiv ID**：2605.21075v1
- **分类**：cs.CV, cs.LG

## 摘要原文

> Earth observation (EO) foundation models (FMs) are increasingly trained on multisensor data,
> spanning multispectral imagery (MSI), synthetic aperture radar (SAR), and derived geospatial
> layers, but hyperspectral imagery (HSI) remains underrepresented. Conversely, existing
> hyperspectral FMs are trained on HSI alone, leaving joint pretraining and fusion of HSI with co-
> located EO sensors unexplored. We introduce SpectralEarth-FM, a hierarchical transformer for
> multisensor EO input with heterogeneous spectral dimensionality. The architecture combines
> spectral tokenization for hyperspectral inputs, sensor-specific encoders, a cross-sensor fusion
> module, and a shared hierarchical encoder, enabling joint processing of HSI and lower-channel
> observations. To pretrain SpectralEarth-FM, we curate SpectralEarth-MM, a dataset that co-
> locates HSI from three spaceborne sensors (EnMAP, EMIT, DESIS) with Sentinel-2, Landsat-8/9
> optical imagery, Landsat land surface temperature (LST), and Sentinel-1 SAR, over common
> geographic footprints. It comprises approximately 2M globally distributed locations, 25M
> georeferenced patches, and over 40TB of data. Pretraining uses a Joint-Embedding Predictive
> Architecture (JEPA)-style objective that matches representations between global views and
> single-sensor local views from the same location. We evaluate SpectralEarth-FM on hyperspectral
> downstream tasks and standard EO benchmarks following the PANGAEA protocol, achieving state-of-
> the-art results across both evaluation settings.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。
