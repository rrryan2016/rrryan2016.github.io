---
title: "Agent Paper | Joint Optimization of Tool Creation and Use for Large Language Model Agents"
date: "2026-08-26"
tags: ["Agent", "cs.AI", "cs.SE"]
paper_title: "Joint Optimization of Tool Creation and Use for Large Language Model Agents"
paper_url: "https://arxiv.org/abs/2608.24571v1"
pdf_url: "https://arxiv.org/pdf/2608.24571v1"
arxiv_id: "2608.24571v1"
authors: "Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Joint Optimization of Tool Creation and Use for Large Language Model Agents
- **作者**：Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee
- **arXiv ID**：2608.24571v1
- **分类**：cs.AI, cs.SE

## 摘要原文

> Tool-augmented language models are bounded by the APIs humans bothered to write; existing tool-
> creation systems patch this by prompting a frozen LLM at inference time, leaving the model that
> writes a tool decoupled from the one that uses it, with no signal that the schemas it produces
> are schemas it can invoke. We propose SMITH (Schema-grounded Multi-task Iterative Tool Honing),
> a reinforcement learning framework that jointly trains tool creation and tool use inside a
> single policy. Each rollout is either a build task (write a tool from a few examples) or a use
> task (invoke a pooled tool on a held-out question). Three separate reward axes catch schema,
> code, and outcome failures independently, so each failure mode contributes its own gradient. A
> 4B Qwen3 trained with SMITH on 13 procedural reasoning tasks with exact verifiers reaches 79.8
> macro-average accuracy on held-out tasks, the best across all evaluated methods and ahead of an
> untrained 30B-A3B tool-writer. It also reaches 40.4 on TabMWP-Hard and 42.6 on out-of-domain GQA
> (+7.6 over the best same-backbone inference-time baseline), without any visual or tabular
> training data. Tools written by our 4B models also lifted the performance of LFM-2.5-350M and
> Qwen3-30B-A3B under same reasoning tasks.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
