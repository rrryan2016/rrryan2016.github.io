---
title: "Agent Paper | Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs"
date: "2026-11-12"
tags: ["Agent", "cs.AI"]
paper_title: "Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs"
paper_url: "https://arxiv.org/abs/2611.14122v1"
pdf_url: "https://arxiv.org/pdf/2611.14122v1"
arxiv_id: "2611.14122v1"
authors: "Federico Ravenda, Mirko Cesarini, Daniele Montagnani, Volodymyr Karpenko, Antonietta Mira, Andrea Raballo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Hx2Dx: From Anamnesis to Diagnosis - A Multimodal Arena for Conversational Clinical Reasoning in LLMs
- **作者**：Federico Ravenda, Mirko Cesarini, Daniele Montagnani, Volodymyr Karpenko, Antonietta Mira, Andrea Raballo
- **arXiv ID**：2611.14122v1
- **分类**：cs.AI

## 摘要原文

> Large language models (LLMs) achieve expert-level diagnostic accuracy in static evaluations,
> where the model receives a curated vignette or case report that already condenses the
> diagnostically relevant findings. Such evaluations measure inference over already selected
> evidence; the evaluations do not account for the inquiry used to obtain it. In clinical
> practice, however, diagnosis is an iterative process of inquiry. Clinicians take the patient's
> history, or anamnesis (Hx), through targeted questioning, examine the patient, and request and
> interpret tests, progressively narrowing the differential until they reach a final diagnosis
> (Dx). We introduce Hx2Dx ARENA, an interactive benchmark of 1'000 clinical cases from the New
> England Journal of Medicine (NEJM). Each case is a simulated encounter that proceeds from
> initial presentation through history taking and physical examination to diagnostic workup. We
> evaluate open- and closed-source LLMs under multiple configurations. Performance varies
> considerably across models in the interactive setting, and every model loses diagnostic accuracy
> relative to the static setting, where the full case is presented upfront. The ability to ask the
> right questions accounts for much of both the gap between models and the loss of accuracy:
> diagnosis improves as questions become more targeted and build a more complete clinical picture.
> LLMs thus reason well once the relevant data are available but remain limited in hypothesis-
> driven information gathering, in knowing what to ask in order to know. Closing this gap is a
> prerequisite for their safe integration into real-world diagnostic workflows.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
