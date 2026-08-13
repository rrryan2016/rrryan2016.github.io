---
title: "Agent Paper | DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation"
date: "2026-08-13"
tags: ["Agent", "cs.CV", "cs.AI"]
paper_title: "DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation"
paper_url: "https://arxiv.org/abs/2608.12308v1"
pdf_url: "https://arxiv.org/pdf/2608.12308v1"
arxiv_id: "2608.12308v1"
authors: "Yan Deng, Fei Xu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation
- **作者**：Yan Deng, Fei Xu
- **arXiv ID**：2608.12308v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Aerial vision-language navigation (VLN) requires an embodied agent to integrate visual evidence
> over time, plan future actions, and determine when it has reached a navigation goal under
> partial observability. Although recent VLA models offer a promising perception-to-action
> paradigm, adapting them to aerial navigation remains challenging due to limited historical
> context, short planning horizons, and unreliable implicit termination. To address these
> challenges, we propose DreamFly, a diffusion-based aerial VLN framework built on Dream-VLA.
> DreamFly introduces a causally aligned historical memory that augments the current visual
> representation using only observations preceding the current decision step, enabling temporal
> reasoning without future information leakage. We further formulate navigation as receding-
> horizon diffusion planning, where the policy predicts a $K$-step action chunk but executes only
> the first action before replanning. This plan-$K$, execute-one strategy uses future actions as
> auxiliary planning targets while preserving closed-loop visual feedback. Finally, LiteStop
> estimates the stop probability directly from action logits at the initial all-mask state,
> decoupling explicit termination from action generation. Experiments on the OpenFly benchmark
> demonstrate consistent improvements in seen and unseen environments. DreamFly achieves
> 32.04%/29.46% SR and 28.22%/23.54% SPL on the test-seen/test-unseen splits, respectively,
> outperforming all compared methods on both metrics while attaining the lowest navigation error.
> These results demonstrate the effectiveness of jointly modeling historical context, future
> action structure, and explicit termination for aerial VLN.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
