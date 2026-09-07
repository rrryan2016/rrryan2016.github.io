---
title: "Agent Paper | Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness"
date: "2026-09-07"
tags: ["Agent", "cs.AI", "cs.CL", "eess.SY"]
paper_title: "Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness"
paper_url: "https://arxiv.org/abs/2609.05314v1"
pdf_url: "https://arxiv.org/pdf/2609.05314v1"
arxiv_id: "2609.05314v1"
authors: "Alexander Neubauer, Tianzhen Hong, Han Li, Mengbo Yu, Amin Darbandi, Yannick Fürst, Martin Kriegel"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Large Language Models for HVAC Operations in Building Energy Systems: A Critical Review of Methods, Applications, and Deployment Readiness
- **作者**：Alexander Neubauer, Tianzhen Hong, Han Li, Mengbo Yu, Amin Darbandi, Yannick Fürst et al.
- **arXiv ID**：2609.05314v1
- **分类**：cs.AI, cs.CL, eess.SY

## 摘要原文

> Building automation systems generate rich sensor data yet remain insight-poor because
> heterogeneous point naming, missing metadata, and fragmented documentation obstruct their
> operational use. This systematic review analyses and codes 66 peer-reviewed studies on large
> language models (LLMs) for HVAC operations published between 2023 and March 2026. Each study is
> classified across five application families and three LLM method families and assessed for
> evidence realism, deployment readiness, and the responsibility boundary between the LLM and
> physical HVAC decisions. The corpus is concentrated in building energy modelling (BEM, 32 of 66
> papers), while load forecasting remains too sparse for subfield-level conclusions. Only four
> studies reach pilot-level evidence, and none reports sustained operational deployment. No study
> was classified as ready-now for industry adoption; three were near-term and 63 research-only.
> Nevertheless, several bounded, human-in-the-loop uses merit near-term trials, including point-
> name normalisation, document-grounded operator support, BEM workflow assistance, and advisory
> interfaces around physics-based controllers. Conventional machine learning (ML), model
> predictive control (MPC), reinforcement learning (RL) and ontology-based tools remain more
> adopted for high-frequency control, short-horizon numerical forecasting, and well-posed ontology
> mapping, while autonomous agentic operation and unvalidated occupant proxies remain research-
> stage. Current evidence therefore supports LLMs primarily as semantic and workflow layers rather
> than autonomous HVAC controllers. Future work should prioritise field-validated benchmarks,
> orchestration evaluation under operational constraints, and LLM-MPC/RL architectures with
> bounded latency and verifiable safety properties.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
