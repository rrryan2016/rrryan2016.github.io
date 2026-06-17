---
title: "Agent Paper | WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning"
date: "2026-06-17"
tags: ["Agent", "cs.AI"]
paper_title: "WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning"
paper_url: "https://arxiv.org/abs/2606.18147v1"
pdf_url: "https://arxiv.org/pdf/2606.18147v1"
arxiv_id: "2606.18147v1"
authors: "Yuwei Zhang, Tong Xia, Bianca Emmerich, Yu Yvonne Wu, Dimitris Spathis, Xin Liu, Daniel McDuff, Cecilia Mascolo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning
- **作者**：Yuwei Zhang, Tong Xia, Bianca Emmerich, Yu Yvonne Wu, Dimitris Spathis, Xin Liu et al.
- **arXiv ID**：2606.18147v1
- **分类**：cs.AI

## 摘要原文

> Language models are remarkably capable at medical question answering, in some cases surpassing
> the accuracy of general physicians. However, answering questions about wearable health data
> remains challenging and understudied, as these ubiquitous sensors produce continuous, high-
> dimensional, and longitudinal data, which is non-trivial to align with text-centric
> distributions in LLM pretraining. The diversity of sensor modalities and user intents cannot be
> effectively handled by a fixed reasoning workflow or a single pretrained foundation model. To
> address these challenges, we propose WEQA, a query-adaptive agent framework that unifies LLM
> reasoning with specialized wearable analytical and modeling tools. An LLM controller is employed
> to synthesize execution plans and dynamically route each query to the appropriate combination of
> sensor analysis and pretrained models, and perform grounded response auditing with external
> knowledge. We also curate a benchmark spanning four open wearable datasets comprising analytic
> and predictive tasks in three different health domains. Experiments show that our framework is
> 24% more accurate than LLM and agentic baselines, and a blinded study with 12 medical experts
> and 8 users shows substantial gains in usefulness and clinical soundness.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
