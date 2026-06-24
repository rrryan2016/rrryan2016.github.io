---
title: "Agent Paper | DeepBD: A Grounded Agentic Workflow for Variant Prioritization and Diagnosis of Genetic Birth Defects"
date: "2026-06-24"
tags: ["Agent", "q-bio.GN", "cs.AI"]
paper_title: "DeepBD: A Grounded Agentic Workflow for Variant Prioritization and Diagnosis of Genetic Birth Defects"
paper_url: "https://arxiv.org/abs/2606.24779v1"
pdf_url: "https://arxiv.org/pdf/2606.24779v1"
arxiv_id: "2606.24779v1"
authors: "Shiyu Li, Ziqi Yan, Zhihao Wu, Jielong Lu, Weiran Liao, Jiajun Yu, Genjie Li, Zeyu Chu, Jiajun Bu, Haishuai Wang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：DeepBD: A Grounded Agentic Workflow for Variant Prioritization and Diagnosis of Genetic Birth Defects
- **作者**：Shiyu Li, Ziqi Yan, Zhihao Wu, Jielong Lu, Weiran Liao, Jiajun Yu et al.
- **arXiv ID**：2606.24779v1
- **分类**：q-bio.GN, cs.AI

## 摘要原文

> Birth defects are a major cause of fetal loss, neonatal morbidity and long-term disability. In
> the subset with suspected genetic etiologies, exome and genome sequencing have moved many cases
> from variant detection to post-sequencing interpretation: clinicians must rank patient-specific
> candidate variants under incomplete fetal or infant phenotypes and heterogeneous evidence from
> population genetics, variant-effect prediction, gene-disease validity, phenotype ontologies,
> cellular and pathway context, protein structure and clinical literature. We present DeepBD, a
> grounded agentic workflow for variant prioritization and diagnostic interpretation of genetic
> birth defects. DeepBD organizes the workflow into LLM-assisted case structuring, a pretrained
> evidence engine, specialist evidence modules and a grounded diagnostic review layer. The
> evidence engine learns patient-specific variant scores from structured rule evidence, sequence
> and variant-effect representations and phenotype-conditioned biological context, whereas
> specialist modules and the agentic layer provide tool-based refinement, candidate-pool review
> and diagnosis-oriented synthesis from ranked candidates. Developed using an in-house fetal and
> infant cohort comprising 18,622 cases, DeepBD achieved Recall@1/3/5/10 of
> 0.658/0.882/0.912/0.929 on an internal held-out solved-case benchmark, outperforming standalone
> Exomiser, DeepRare and prompted LLM reranking baselines evaluated on Exomiser-derived top-20
> candidate variants. Ablation and overlap analyses show that rule evidence, mechanistic context,
> and specialist refinement provide complementary signals. These findings support a grounded
> agentic workflow that separates evidence integration, tool-based refinement, and LLM-assisted
> diagnostic review for retrospective variant prioritization in genetic birth defects.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
