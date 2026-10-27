---
title: "Agent Paper | EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation"
date: "2026-10-27"
tags: ["Agent", "cs.AI", "cs.MA"]
paper_title: "EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation"
paper_url: "https://arxiv.org/abs/2610.35690v1"
pdf_url: "https://arxiv.org/pdf/2610.35690v1"
arxiv_id: "2610.35690v1"
authors: "Yitao Xiao, Xu Zhang, Ye Cheng, Shaoyong Guo, Yan Sun, Ziyue Zhu, Sitao Xie, Guo Tong, Haoran Luo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：EvoRouter: Cost-Efficient Multi-Agent Routing via Insight-Guided On-Policy Distillation
- **作者**：Yitao Xiao, Xu Zhang, Ye Cheng, Shaoyong Guo, Yan Sun, Ziyue Zhu et al.
- **arXiv ID**：2610.35690v1
- **分类**：cs.AI, cs.MA

## 摘要原文

> Serving web queries at scale with multi-agent systems requires jointly configuring large
> language models, collaboration modes, agent counts, interaction rounds, and skills. However, the
> resulting configuration space grows combinatorially, while sparse execution rewards provide
> limited fine-grained supervision for interdependent planning decisions. We propose EvoRouter, a
> self-evolving multi-agent routing framework driven by insight-guided on-policy distillation. A
> dedicated expert periodically synthesizes performance-cost feedback from configuration
> trajectories across tasks into reusable conditional routing insights about capability
> requirements, returns from resource scaling, and interactions among configuration choices. A
> privileged teacher combines these evolving insights with current execution feedback to provide
> dense token-level supervision for the router's own planning trajectories through on-policy
> distillation. Cost-aware reinforcement learning jointly optimizes task performance and
> computational cost. Together, these training signals internalize execution insights into the
> routing policy. The updated policy generates new trajectories that support subsequent insight
> extraction, forming an execution-driven self-improvement loop. We evaluate EvoRouter on 19 in-
> domain datasets spanning five domains and two out-of-domain benchmarks. EvoRouter achieves an
> average in-domain accuracy of 68.69%, outperforming the strongest routing baseline by 7.23
> percentage points while reducing inference compute cost by 50.95%. Our code is open-sourced at
> https://github.com/CenYangtze/EvoRouter.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
