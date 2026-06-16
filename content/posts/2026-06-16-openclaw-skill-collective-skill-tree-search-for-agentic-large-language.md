---
title: "Agent Paper | OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models"
date: "2026-06-16"
tags: ["Agent", "cs.AI", "cs.CL"]
paper_title: "OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models"
paper_url: "https://arxiv.org/abs/2606.16774v1"
pdf_url: "https://arxiv.org/pdf/2606.16774v1"
arxiv_id: "2606.16774v1"
authors: "Tianyi Lin, Chuanyu Sun, Jingyi Zhang, Changxu Wei, Huanjin Yao, Shunyu Liu, Xikun Zhang, Liu Liu, Jiaxing Huang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models
- **作者**：Tianyi Lin, Chuanyu Sun, Jingyi Zhang, Changxu Wei, Huanjin Yao, Shunyu Liu et al.
- **arXiv ID**：2606.16774v1
- **分类**：cs.AI, cs.CL

## 摘要原文

> Equipping Large Language Model (LLM) agents with effective skills is crucial for solving complex
> tasks in real-world systems like OpenClaw. In this work, we aim to develop a framework that
> automatically constructs such reusable skills to enhance LLMs in tool use, multi-step reasoning,
> and dynamic environment interaction. To this end, we propose Collective Skill Tree Search
> (CSTS), a novel tree-search-based skill construction framework that constructs structured,
> diverse and generalizable tree of skills. The core idea of CSTS is to leverage collective
> intelligence to jointly search, identify and compose effective skills via two iterative phases:
> Collective Skill Node Generation (CSN-Gen) and Collective Skill Node Assessment (CSN-Assess).
> CSN-Gen exploits collective knowledge from multiple models to explore diverse candidate skills
> for each subtask, enabling comprehensive skill exploration. CSN-Assess employs multiple models
> as judges to evaluate and select skill nodes with two scoring mechanisms: (1) collective quality
> scoring that aggregates independent evaluations to produce a robust estimate of skill
> effectiveness, and (2) collective transferability scoring that explicitly verifies whether a
> skill generalizes well across different models. With CSTS, we construct a set of comprehensive
> tree of skills along with skill-augmented training data, enabling models to effectively learn
> and utilize skills. Besides, we introduce Collective Skill Reinforcement Learning, which
> actively selects multiple relevant skills from the tree to broaden solution-space exploration,
> avoid being trapped by a single skill and its resulting homogeneous or suboptimal solutions. As
> a result, our trained model, OpenClaw-Skill, exhibits outstanding agentic capabilities in long-
> horizon planning, tool use and generalization over challenging benchmarks.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
