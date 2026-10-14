---
title: "Agent Paper | BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems"
date: "2026-10-14"
tags: ["Agent", "cs.AI", "cs.CL"]
paper_title: "BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems"
paper_url: "https://arxiv.org/abs/2610.18780v1"
pdf_url: "https://arxiv.org/pdf/2610.18780v1"
arxiv_id: "2610.18780v1"
authors: "Xiaoguang Guo, Yaohao Long, Chuxu Zhang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems
- **作者**：Xiaoguang Guo, Yaohao Long, Chuxu Zhang
- **arXiv ID**：2610.18780v1
- **分类**：cs.AI, cs.CL

## 摘要原文

> Large language model multi-agent systems extend individual agents' capabilities through
> collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures
> harder to diagnose: one agent may misinterpret a correct result while others carry the mistake
> forward. Failure attribution therefore seeks to identify the responsible agent and decisive
> error step. Recent methods trace dependencies, but knowing where information came from is not
> the same as knowing where it went wrong. We introduce BLADE (Blame Localization via Audited
> Dependency Evidence), a training-free framework that moves beyond tracing information to
> auditing its use. Using Jev for structured probabilistic judgments, BLADE uses dependency
> probabilities to select relevant source-decision handoffs for auditing. At these handoffs, it
> examines whether receiving decisions use their sources faithfully and within task requirements,
> distinguishing error introduction, propagation, and repair. These findings inform a global
> diagnosis that considers all execution steps. Without reference answers, BLADE achieves the best
> or tied-best step accuracy among eight strategies under a shared Jev decision interface on 1,228
> failed runs across five Who&When and Who&When Pro subsets, outperforming All-at-once by 2.2-11.1
> percentage points. Making responsibility evidence explicit offers a path toward more
> interpretable and reliable agentic systems.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
