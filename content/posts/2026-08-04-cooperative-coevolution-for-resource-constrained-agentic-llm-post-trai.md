---
title: "Agent Paper | Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training"
date: "2026-08-04"
tags: ["Agent", "cs.AI", "cs.LG"]
paper_title: "Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training"
paper_url: "https://arxiv.org/abs/2608.02391v1"
pdf_url: "https://arxiv.org/pdf/2608.02391v1"
arxiv_id: "2608.02391v1"
authors: "Zhiyuan Wang, Shengcai Liu, Jiahao Wu, Ning Lu, Hui Ouyang, Shaofeng Zhang, Haoze Lv, Ke Tang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training
- **作者**：Zhiyuan Wang, Shengcai Liu, Jiahao Wu, Ning Lu, Hui Ouyang, Shaofeng Zhang et al.
- **arXiv ID**：2608.02391v1
- **分类**：cs.AI, cs.LG

## 摘要原文

> Tool-using large language model (LLM) agents produce long, multi-turn trajectories, making
> gradient-based post-training memory-intensive. Evolution strategies (ES) enable memory-efficient
> full-parameter post-training without backpropagation and can eventually match the performance of
> gradient-based reinforcement learning (RL). However, resource-constrained settings typically
> offer only a few GPUs, so the high GPU-hour requirements of ES translate into prohibitively long
> training times. To address this, we introduce Cooperative Parameter-subspace Evolution Strategy
> (CoPES), a cooperative coevolutionary method that decomposes the full parameter space into
> lower-dimensional subspaces and searches over them cooperatively to improve optimization
> efficiency. We post-train a Qwen3.5-4B tool-using agent for the math task and evaluate it on
> five benchmarks of varying difficulty. Under the GPU-hour budget of full-parameter GRPO's best
> validation checkpoint, CoPES recovers 92% of GRPO's validation-accuracy gain, versus 67% for
> standard ES, while its theoretical GPU memory requirement is less than one-eighth that of full-
> parameter GRPO. It consistently outperforms standard ES and LoRA-based GRPO on all evaluated
> pass@k metrics across the five benchmarks. Additional experiments further show the advantage of
> CoPES on the question-answering task. These results demonstrate an improved trade-off between
> memory requirements and training time for agentic LLM post-training under resource constraints.
> The code is open-sourced in https://github.com/MetaronWang/CoPES

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
