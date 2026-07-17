---
title: "Agent Paper | Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents"
date: "2026-07-17"
tags: ["Agent", "cs.CL", "cs.AI", "cs.MA"]
paper_title: "Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents"
paper_url: "https://arxiv.org/abs/2607.15095v1"
pdf_url: "https://arxiv.org/pdf/2607.15095v1"
arxiv_id: "2607.15095v1"
authors: "Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents
- **作者**：Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel
- **arXiv ID**：2607.15095v1
- **分类**：cs.CL, cs.AI, cs.MA

## 摘要原文

> The formation of political coalitions is a complex negotiation driven by both concrete policy
> objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new
> avenues for computational political science, the neutrality and helpfulness biases instilled by
> Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast
> partisan behaviour. We present a multi-agent framework that reconciles factual grounding with
> ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization
> (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas,
> while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We
> operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a
> hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation
> interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces
> every clause in the final agreement back to its manifesto origin and classifies it into five
> provenance states, a Coalition Influence Score (CIS) that aggregates these traceable
> contributions to identify which party shaped the agreement, and a real-world grounding pass that
> benchmarks each simulated provision against the historically adopted coalition agreement. Across
> three independent simulations the framework yields a stable winner and ranking (N-VA ahead of
> CD\&V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization
> whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-
> ante exploration of party compatibility and formateur-mediated compromise.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
