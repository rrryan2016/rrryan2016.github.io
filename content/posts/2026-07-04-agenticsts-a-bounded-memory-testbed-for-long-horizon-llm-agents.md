---
title: "Agent Paper | AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents"
date: "2026-07-04"
tags: ["Agent", "cs.AI", "cs.CL"]
paper_title: "AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents"
paper_url: "https://arxiv.org/abs/2607.02255v1"
pdf_url: "https://arxiv.org/pdf/2607.02255v1"
arxiv_id: "2607.02255v1"
authors: "Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, Zizhen Li, Chuanhao Li, Xiangcheng Cao, Yihao Liu, Fanrui Zhang, Li Jin, Kaipeng Zhang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents
- **作者**：Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, Zizhen Li, Chuanhao Li, Xiangcheng Cao et al.
- **arXiv ID**：2607.02255v1
- **分类**：cs.AI, cs.CL

## 摘要原文

> Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to
> see. The simplest contract appends past observations, tool calls, and reflections to every
> prompt, which makes prior context easy to access but also turns it into a jumbled mixture in
> which the effect of any single memory component is hard to isolate. We introduce and instrument
> an alternative bounded contract: every decision is made from a fresh user message assembled by
> typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded
> across runs of any length, and any single layer can be ablated in isolation. We instantiate the
> contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require
> hundreds of tactical and strategic decisions. A public online benchmark of frontier LLMs on the
> same game reports zero wins at the lowest difficulty across five configurations, and the
> developer-reported human win rate at the same difficulty is 16%; the task is hard but not
> saturated. Within our harness, a fixed-A0 ablation shows the largest observed difference when
> triggered strategic skills are enabled: the no-store baseline wins 3/10 games and adding the
> skill layer 6/10. At this sample size the comparison is directional rather than statistically
> decisive (Fisher exact p\approx0.37); a cross-backbone probe and public accumulating-context
> baselines are reported as operational comparisons rather than controlled tests of the contract
> variable itself. We release a reproducible testbed: 298 completed trajectories with condition
> tags, frozen memory/skill snapshots, prompt records, and analysis scripts -- an agent design and
> a validated, reusable methodology for studying how explicit memory layers shape long-horizon
> LLM-agent decisions.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
