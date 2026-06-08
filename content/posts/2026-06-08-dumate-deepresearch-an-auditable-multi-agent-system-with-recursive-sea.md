---
title: "Agent Paper | DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning"
date: "2026-06-08"
tags: ["Agent", "cs.AI"]
paper_title: "DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning"
paper_url: "https://arxiv.org/abs/2606.07299v1"
pdf_url: "https://arxiv.org/pdf/2606.07299v1"
arxiv_id: "2606.07299v1"
authors: "Lingyong Yan, Can Xu, Yukun Zhao, Wenxuan Li, Qingyang Chen, Jiulong Wu, Wenli Song, Xiangnan Li, Weixian Shi, Yiqun Chen, Xuchen Ma, Yuchen Li, Jiashu Zhao, Shuaiqiang Wang, Jianmin Wu, Dawei Yin"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：DuMate-DeepResearch: An Auditable Multi-Agent System with Recursive Search and Rubric-Grounded Reasoning
- **作者**：Lingyong Yan, Can Xu, Yukun Zhao, Wenxuan Li, Qingyang Chen, Jiulong Wu et al.
- **arXiv ID**：2606.07299v1
- **分类**：cs.AI

## 摘要原文

> Deep Research (DR) has emerged as a new agentic paradigm to tackle complex, open-ended research
> tasks, demanding systems that can iteratively frame problems, acquire evidence, verify sources,
> and synthesize long-form reports. In practice, however, current DR systems are constrained by
> four interrelated limitations: long-horizon planning over an underspecified scope, the
> bottleneck of decomposing and scheduling such tasks within a single agent, hallucination risk in
> long-form synthesis, and limited process auditability. This technical report presents DuMate-
> DeepResearch, a multi-agent DR framework built on the Qianfan Agent Foundry. The framework
> decouples the Agent Core, which handles task understanding, planning, and scheduling, from an
> extensible Tool Ecosystem for retrieval, evidence acquisition, and report rendering, making
> every intermediate decision and tool invocation explicitly traceable. Building on this
> infrastructure, DuMate-DeepResearch further introduces three mechanisms: (i) a graph-based
> dynamic planning strategy expands the research roadmap coarse-to-fine and continuously revises
> it through reflection, re-planning, backtracking, and parallel branching; (ii) a recursive two-
> level execution design delegates each complex search sub-task to an inner Search Agent that runs
> its own planning loop, isolating noisy retrieval and stabilizing long-horizon execution; (iii) a
> rubric-based test-time optimization mechanism dynamically generates task-specific quality
> criteria and uses them as live reasoning scaffolds for evidence-grounded synthesis and adaptive
> stopping. Across two deep research benchmarks, DuMate-DeepResearch establishes new state-of-the-
> art results: the best overall score (58.03%) on DeepResearch Bench, and the best overall score
> (61.95%) on DeepResearch Bench II while ranking first in information recall and analysis.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
