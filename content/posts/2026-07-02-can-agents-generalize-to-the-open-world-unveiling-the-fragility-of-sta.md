---
title: "Agent Paper | Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use"
date: "2026-07-02"
tags: ["Agent", "cs.AI"]
paper_title: "Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use"
paper_url: "https://arxiv.org/abs/2607.01084v1"
pdf_url: "https://arxiv.org/pdf/2607.01084v1"
arxiv_id: "2607.01084v1"
authors: "Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, Lan-Zhe Guo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Can Agents Generalize to the Open World? Unveiling the Fragility of Static Training in Tool Use
- **作者**：Song-Lin Lv, Weiming Wu, Rui Zhu, Zi-Jian Cheng, Lan-Zhe Guo
- **arXiv ID**：2607.01084v1
- **分类**：cs.AI

## 摘要原文

> While Large Language Model (LLM) agents demonstrate proficiency in static benchmarks, their
> deployment in real-world scenarios is hindered by the dynamic nature of user queries, tool sets,
> and interaction dynamics. To address this generalization gap, we formalize OpenAgent (Tool-Use
> Agent in Open-World), a problem setting characterized by distributional shifts across query,
> action, observation, and domain dimensions. To systematically diagnose its impact, we construct
> a controlled sandbox environment where we define fine-grained environmental shifts across a
> four-tier hierarchy, Perception, Interaction, Reasoning, and Internalization, and conduct a
> comprehensive series of experiments. Our analysis yields a series of key insights, demonstrating
> that agents trained via both Supervised Fine-Tuning(SFT) and Reinforcement Learning suffer from
> varying degrees of performance degradation when confronting open environmental shifts. Building
> on these insights, we propose Perturbation-Augmented Fine-Tuning, a disturbance-based
> intervention strategy for SFT that lays the foundation for enhancing agent robustness and
> utility in realistic environments. Our code will be released at: https://github. com/LAMDA-
> NeSy/OpenAgent.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
