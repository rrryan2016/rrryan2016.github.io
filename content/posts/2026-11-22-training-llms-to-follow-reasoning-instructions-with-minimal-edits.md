---
title: "Agent Paper | Training LLMs to Follow Reasoning Instructions with Minimal Edits"
date: "2026-11-22"
tags: ["Agent", "cs.AI"]
paper_title: "Training LLMs to Follow Reasoning Instructions with Minimal Edits"
paper_url: "https://arxiv.org/abs/2611.26342v1"
pdf_url: "https://arxiv.org/pdf/2611.26342v1"
arxiv_id: "2611.26342v1"
authors: "Alexandra Yakovleva, Luat Gia Khoi Nguyen, Juho Kannala, Harri Valpola, Alexander Ilin"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Training LLMs to Follow Reasoning Instructions with Minimal Edits
- **作者**：Alexandra Yakovleva, Luat Gia Khoi Nguyen, Juho Kannala, Harri Valpola, Alexander Ilin
- **arXiv ID**：2611.26342v1
- **分类**：cs.AI

## 摘要原文

> Large language models increasingly rely on extended reasoning traces, yet the training signals
> used to shape this behavior remain coarse. Supervised fine-tuning on full trajectories forces
> the model to imitate an entire demonstration, overconstraining its output distribution, while
> trajectory-level reinforcement learning provides only weak credit assignment, rewarding or
> penalizing whole completions without identifying where they succeed or fail. We propose edit-
> based training, a general framework for learning from a model's own trajectories via localized
> textual corrections. Given a sampled completion, an editor identifies the first point of failure
> under a specified criterion and proposes a minimal replacement span. The model is then
> supervised only on these edited spans. By design, this concentrates supervision where the
> model's reasoning first breaks down and aims to preserve its existing reasoning patterns
> elsewhere. The method applies both offline and online, with the latter continually adapting
> supervision to the model's evolving failure modes. We instantiate this approach on reasoning
> instruction following with Qwen3-32B on the ReasonIF benchmark. Compared to full-trajectory
> imitation and trajectory-level reinforcement learning baselines, edit-based training
> substantially improves compliance with the reasoning instruction while largely preserving the
> model's skills on untargeted tasks. These results suggest that localized correction is an
> effective complement to these approaches for shaping how LLMs reason.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
