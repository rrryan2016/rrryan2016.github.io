---
title: "Agent Paper | Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents"
date: "2026-09-12"
tags: ["Agent", "cs.SE", "cs.AI"]
paper_title: "Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents"
paper_url: "https://arxiv.org/abs/2609.11677v1"
pdf_url: "https://arxiv.org/pdf/2609.11677v1"
arxiv_id: "2609.11677v1"
authors: "Ruiqing Yue, Yu Cui, Zhuoyu Sun, Sicheng Pan, Xianhong Xue, Tingyu Li, Ting Li, Wenzhuo Zhu, Yi Chen, Yifei Liu, Baohan Huang, Zhe Cui, Haibin Zhang, Cong Zuo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents
- **作者**：Ruiqing Yue, Yu Cui, Zhuoyu Sun, Sicheng Pan, Xianhong Xue, Tingyu Li et al.
- **arXiv ID**：2609.11677v1
- **分类**：cs.SE, cs.AI

## 摘要原文

> Self-evolving runtime harnesses can substantially improve the capabilities of large language
> model (LLM) agents and provide a promising paradigm for optimizing agent execution. Existing
> harness evolution methods typically rely on iterative search, repeatedly evaluating and revising
> candidate harnesses based on execution feedback from task instances. While this paradigm enables
> continuous harness optimization, it incurs substantial time overhead due to repeated agent
> executions and code modifications, and may overfit to observed tasks and specific failure
> patterns, resulting in degraded generalization to unseen tasks. We identify the lack of
> principled failure diagnosis as a key bottleneck in harness evolution: an observed failure can
> reflect either model-specific deficiencies or systematic harness deficiencies, and directly
> optimizing against individual failures can lead to unnecessary model-specific accommodation. We
> therefore propose Ecdysis, an efficient and effective framework that distinguishes model-
> specific accommodation from harness-level repair and biases adaptation toward systematic harness
> deficiencies by identifying recurring cross-task failure patterns. Ecdysis adopts a batch-level
> cross-instance failure aggregation paradigm to jointly analyze failure evidence from multiple
> task instances and further introduces Failure-Driven Collaborative Refinement to diagnose
> failure causes and iteratively refine harness modification specifications. By combining cross-
> instance failure analysis with multi-role diagnosis, Ecdysis enables more effective harness
> evolution with lower training time. Experiments show that Ecdysis achieves up to a 1.84x speedup
> in harness training compared with existing harness evolution methods, while improving the
> reasoning accuracy of the resulting harnesses by 18.56%.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
