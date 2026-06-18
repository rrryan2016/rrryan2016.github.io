---
title: "Agent Paper | AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces"
date: "2026-06-18"
tags: ["Agent", "cond-mat.mtrl-sci", "cs.AI"]
paper_title: "AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces"
paper_url: "https://arxiv.org/abs/2606.19152v1"
pdf_url: "https://arxiv.org/pdf/2606.19152v1"
arxiv_id: "2606.19152v1"
authors: "Zongmin Zhang, Yuyang Lou, Bowen Zhang, Junwu Chen, Ryo Kuroki, Xuan Vu Nguyen, Edvin Fako, Lixue Cheng, Philippe Schwaller"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：AdsMind: A Physics-Grounded Multi-Agent System for Self-Correcting Discovery of Adsorption Configurations on Heterogeneous Catalyst Surfaces
- **作者**：Zongmin Zhang, Yuyang Lou, Bowen Zhang, Junwu Chen, Ryo Kuroki, Xuan Vu Nguyen et al.
- **arXiv ID**：2606.19152v1
- **分类**：cond-mat.mtrl-sci, cs.AI

## 摘要原文

> Identifying the lowest-energy surface-adsorbate configuration is critical for modeling
> heterogeneous catalysis, yet exhaustive exploration with ab initio calculations is
> computationally prohibitive. Machine-learning force fields (MLFFs) accelerate structural
> relaxation but leave the search over the vast configurational space a major bottleneck, and
> open-loop large language model (LLM) agents lack a physics-grounded feedback mechanism to
> correct erroneous initial guesses. We propose AdsMind (Adsorption configuration discovery with
> Machine intelligence and relaxation feedback), a closed-loop multi-agent framework that enables
> autonomous error correction through MLFF relaxation feedback. Across four LLM backends, AdsMind
> achieves consistently high search reliability, with success rates of 100% and 98.8% on the
> benchmarks AA20 and OCD-GMAE62. Relative to its single-pass (1-Shot) ablation it reduces cross-
> backend energy dispersion, and it uses only 4.11 and 4.67 MLFF relaxations per case,
> respectively -- an approximately 14-fold reduction over heuristic enumeration baselines. Density
> functional theory (DFT) validation using VASP/PBE on six representative AA20 systems shows that
> the reported open-loop Adsorb-Agent outputs exhibit qualitative adsorption-energy sign errors
> for molecular adsorbates, whereas AdsMind preserves the correct sign in all tested cases with
> closer quantitative agreement. AdsMind thus delivers reliability, self-reflection, and
> interpretability simultaneously, supporting more DFT-informed autonomous chemistry workflows.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
