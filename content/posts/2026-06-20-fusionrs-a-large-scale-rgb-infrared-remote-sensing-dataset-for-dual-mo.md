---
title: "Remote Sensing Paper | FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models"
date: "2026-06-20"
tags: ["Remote Sensing", "cs.CV", "cs.AI"]
paper_title: "FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models"
paper_url: "https://arxiv.org/abs/2606.17020v1"
pdf_url: "https://arxiv.org/pdf/2606.17020v1"
arxiv_id: "2606.17020v1"
authors: "Jiaju Han, Ben Zhang, Xuemeng Sun, Qike Zhang, Yuxian Dong, Chengyin Hu, Fengyu Zhang, Yiwei Wei, Jiujiang Guo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models
- **作者**：Jiaju Han, Ben Zhang, Xuemeng Sun, Qike Zhang, Yuxian Dong, Chengyin Hu et al.
- **arXiv ID**：2606.17020v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Remote sensing vision-language models have advanced Earth observation understanding, but most
> existing work remains centered on RGB imagery, leaving the complementary information in infrared
> data underexplored. Infrared images provide distinctive cues, including thermal intensity
> structures, object boundaries, and illumination-invariant scene features, which can enrich
> visual-language learning beyond conventional RGB observations. However, a large-scale RGB-
> infrared-text dataset for remote sensing vision-language modeling is still absent. To address
> this gap, we introduce FusionRS, the first large-scale RGB-infrared-text dataset designed for
> dual-modal vision-language learning in remote sensing. FusionRS is constructed by translating
> diverse public RGB remote sensing images into infrared-style counterparts, forming aligned RGB-
> IR image pairs. Each pair is associated with conventional scene captions and IR-aware captions
> that explicitly describe infrared-specific visual properties while preserving semantic content.
> Based on FusionRS, we train dual-modal vision-language foundation models for RGB-IR joint
> understanding. We first train CLIP-style models for RGB-IR-text alignment, and then fine-tune
> generative VLMs for dual-modal RGB-IR captioning. Experiments show that FusionRS improves RGB-IR
> alignment, infrared-to-text retrieval, and dual-modal captioning over RGB-only and non-IR-aware
> training settings. Ablation studies further verify that IR-aware captions are crucial for
> strengthening infrared-language alignment, highlighting the importance of modality-specific
> textual supervision for more scalable RGB-infrared remote sensing vision-language representation
> learning.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
