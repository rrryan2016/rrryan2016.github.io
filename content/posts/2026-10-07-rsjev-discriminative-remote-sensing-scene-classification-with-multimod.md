---
title: "Remote Sensing Paper | RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models"
date: "2026-10-07"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models"
paper_url: "https://arxiv.org/abs/2610.08539v1"
pdf_url: "https://arxiv.org/pdf/2610.08539v1"
arxiv_id: "2610.08539v1"
authors: "Dongchen Si, Di Wang, Mingzhen Xu, Jing Zhang, Bo Du, Liangpei Zhang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models
- **作者**：Dongchen Si, Di Wang, Mingzhen Xu, Jing Zhang, Bo Du, Liangpei Zhang
- **arXiv ID**：2610.08539v1
- **分类**：cs.CV

## 摘要原文

> Remote sensing scene classification is a fundamental task in Earth observation and geospatial
> analysis. Existing approaches mainly follow three paradigms: task-specific visual
> classification, vision-language similarity matching, and autoregressive multimodal generation.
> However, visual classifiers rely on predefined label spaces, CLIP-based methods perform
> recognition through static image-text alignment, and multimodal large language models (MLLMs)
> introduce unnecessary token-level generation for classification tasks with explicit candidate
> categories. To address these limitations, we propose RSJEV, a one-pass multimodal decision
> framework for remote sensing scene classification. Unlike conventional MLLMs that formulate
> classification as autoregressive text generation, RSJEV reformulates scene classification as a
> candidate-conditioned multimodal discriminative decision process, where visual representations,
> task instructions, and candidate category semantics are jointly modeled. Specifically, we
> introduce a OnePass Decider that extracts multimodal decision states and directly estimates
> category probabilities within the candidate category space, eliminating autoregressive decoding
> while preserving vision-language interactions. Extensive experiments on three widely used remote
> sensing scene classification benchmarks, including UC Merced, AID, and NWPU-RESISC45,
> demonstrate that RSJEV achieves superior classification performance compared with representative
> CNN-, Transformer-, Mamba-, CLIP-, and MLLM-based methods. Moreover, RSJEV significantly reduces
> inference costs and achieves a better accuracy-efficiency trade-off with only a compact
> 0.8B-parameter model. These results demonstrate the effectiveness of state-conditioned
> multimodal decision making for efficient remote sensing image understanding. The code will be
> available at https://github.com/Dongtcs/RSJEV.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
