---
title: "Agent Paper | PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving"
date: "2026-09-09"
tags: ["Agent", "cs.AI", "cs.CL", "cs.RO"]
paper_title: "PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving"
paper_url: "https://arxiv.org/abs/2609.08965v1"
pdf_url: "https://arxiv.org/pdf/2609.08965v1"
arxiv_id: "2609.08965v1"
authors: "Yuan Gao, Sebastian Müller, Mattia Piccinini, Marc Kaufeld, Yuchen Zhang, Finn Rasmus Schäfer, Qunying Song, Johannes Betz"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in Autonomous Driving
- **作者**：Yuan Gao, Sebastian Müller, Mattia Piccinini, Marc Kaufeld, Yuchen Zhang, Finn Rasmus Schäfer et al.
- **arXiv ID**：2609.08965v1
- **分类**：cs.AI, cs.CL, cs.RO

## 摘要原文

> Ensuring the safety of autonomous driving is a critical challenge. Scenario-based testing is a
> systematic process used to validate Autonomous Driving Systems (ADSs), but it remains a
> fragmented modular pipeline in which scenario generation, retrieval, modification, ADS
> execution, and results analysis are performed by separate tools with little interaction. Large
> Language Model (LLM) agents have shown promise across ADS sub-systems such as perception,
> planning, and control. However, no prior work covers the whole scenario-based testing pipeline
> for ADSs with a unified LLM-agent framework. We present PlannerForge, an LLM-agent framework
> that extends all scenario-based testing stages (from Scenario Generation to ADS Assessment) and
> adds two further LLM-enhanced stages: ADS Enhancement and ADS Benchmarking. We evaluate
> PlannerForge with 10 off-the-shelf LLMs across all tasks (Generation, Selection, Modification,
> Module Routing, Planner Testing, and Enhancement) under 5 prompt conditions. Best-per-task
> scores range from 0.88 to 1.00, and open-source 20-35B backends match commercial APIs on most
> tasks. Open-source models such as Qwen3.6:35B match commercial APIs on three of the five tasks.
> Chaining the modules end-to-end retains 83% / 78% of seed queries (commercial / open). It
> outperforms Scenario Factory 2.0 (Finkeldei et al., 2025) on natural-language generation (193
> vs. 144 executable of 200) and realises 92-96% of requested city, road and vehicle attributes.
> It outperforms BM25 (Robertson and Zaragoza, 2009) at rank 1 selection (92.0% vs. 67.5%) and
> From-Words-to-Collisions (Gao et al., 2025) on physically valid edits (>=94% vs. 31%). At N=400,
> cost-tuning lifts planner success from 50.4% to 70.2% and cuts collisions from 19.0% to 8.4%,
> without domain-specific fine-tuning.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
