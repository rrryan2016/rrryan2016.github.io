---
title: "Agent Paper | Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems"
date: "2026-06-19"
tags: ["Agent", "cs.LG", "cs.AI", "cs.MA"]
paper_title: "Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems"
paper_url: "https://arxiv.org/abs/2606.20493v1"
pdf_url: "https://arxiv.org/pdf/2606.20493v1"
arxiv_id: "2606.20493v1"
authors: "Zewen Liu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems
- **作者**：Zewen Liu
- **arXiv ID**：2606.20493v1
- **分类**：cs.LG, cs.AI, cs.MA

## 摘要原文

> When large language models serve as evaluators in multi-agent systems, their systematic
> evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal
> framework for measuring how evaluator biases spread across interacting LLM agents. In a
> controlled 3-agent experiment using DeepSeek-chat with three distinct evaluator bias profiles
> (structured, balanced, evidence-based), we measure the Cross-Agent Contagion Matrix Gamma_3 and
> find that evaluator biases consistently propagate between agents (gamma in [0.157, 0.352]), even
> within the same underlying model. We identify three propagation regimes governed by the spectral
> radius rho(Gamma_N), and demonstrate that homogeneous-model agents produce contagion
> coefficients 3-5x weaker than cross-model coefficients observed in prior work (MM-EPC: gamma
> approx 0.85-1.3), placing them in the suppression regime. We show that increasing evaluator
> committee size from k=1 to k=3 reduces effective contagion by 72.4%, providing an actionable
> mitigation strategy. We release the open-source Contagion Network experimental framework.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
