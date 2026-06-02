---
title: "Agent Paper | Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling"
date: "2026-06-02"
tags: ["Agent", "cs.CV", "cs.AI"]
paper_title: "Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling"
paper_url: "https://arxiv.org/abs/2606.02578v1"
pdf_url: "https://arxiv.org/pdf/2606.02578v1"
arxiv_id: "2606.02578v1"
authors: "Seojeong Park, Jiho Choi, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling
- **作者**：Seojeong Park, Jiho Choi, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim
- **arXiv ID**：2606.02578v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Recent multimodal large language models have demonstrated strong reasoning ability, yet their
> reliability as automated evaluators remains limited by a critical weakness: when visual evidence
> conflicts with textual cues, MLLM judges tend to reward plausible narratives over perceptually
> correct answers. We identify and systematically analyze this phenomenon, which we term
> Perceptual Judgment Bias. Through controlled visual perturbations, existing multimodal judges
> frequently anchor on the response text instead of their own visual perception, leading to
> inconsistent and non-verifiable evaluations. To address this issue, we introduce the
> Perceptually Perturbed Judgment Dataset, which constructs minimally edited counterfactual
> responses that isolate perceptual errors and enable verifiable supervision. Building on this
> dataset, we develop a unified training framework that combines a structured GRPO-based reward
> with a batch-ranking objective, achieving coherent global ordering without explicit pairwise
> labels. Experiments across diverse MLLM-as-a-Judge benchmarks show that our approach
> substantially improves perceptual fidelity, ranking coherence, and alignment with human
> evaluation. Our results establish a scalable and generalizable pathway for training multimodal
> judges that are perceptually grounded, interpretable, and robust to visual-reasoning conflicts.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
