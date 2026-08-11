---
title: "Agent Paper | SHE: Trajectory-driven Safety Harness Evolution for LLM Agents"
date: "2026-08-11"
tags: ["Agent", "cs.AI", "cs.CV"]
paper_title: "SHE: Trajectory-driven Safety Harness Evolution for LLM Agents"
paper_url: "https://arxiv.org/abs/2608.09885v1"
pdf_url: "https://arxiv.org/pdf/2608.09885v1"
arxiv_id: "2608.09885v1"
authors: "Wanying Qu, Qinghua Mao, Yu Li, Jiyao Liu, Xin Zhang, Dadi Guo, Yanxu Zhu, Qingyu Liu, Leitao Yuan, Xi Lin, Shanfeng Zhu, Yanwei Fu, Jing Shao, Xia Hu, Dongrui Liu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：SHE: Trajectory-driven Safety Harness Evolution for LLM Agents
- **作者**：Wanying Qu, Qinghua Mao, Yu Li, Jiyao Liu, Xin Zhang, Dadi Guo et al.
- **arXiv ID**：2608.09885v1
- **分类**：cs.AI, cs.CV

## 摘要原文

> The safety of large language model (LLM) agents depends not only on model weights but also on
> the agent harness that manages context, memory, tools, permissions, and runtime control.
> Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting
> their ability to evolve with emerging risks. Moreover, coupled functions across harness
> components obscure safety responsibility attribution, making localized evolution difficult. We
> propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from
> rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety
> responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy,
> defining clear functional boundaries for localized evolution. Based on this decomposition, SHE
> introduces an attribution-guided evolution loop that converts trajectory failures into
> structured diagnoses, learns artifact-specific boundary refinements, and selects evolved
> harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that
> SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction
> compared with static SafeHarness, while also improving benign utility. The evolved harness
> further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across
> agent models without additional evolution.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
