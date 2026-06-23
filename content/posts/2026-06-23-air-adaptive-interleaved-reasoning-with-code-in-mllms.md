---
title: "Agent Paper | AIR: Adaptive Interleaved Reasoning with Code in MLLMs"
date: "2026-06-23"
tags: ["Agent", "cs.CV", "cs.AI"]
paper_title: "AIR: Adaptive Interleaved Reasoning with Code in MLLMs"
paper_url: "https://arxiv.org/abs/2606.23678v1"
pdf_url: "https://arxiv.org/pdf/2606.23678v1"
arxiv_id: "2606.23678v1"
authors: "Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：AIR: Adaptive Interleaved Reasoning with Code in MLLMs
- **作者**：Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
- **arXiv ID**：2606.23678v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Following the paradigm shift initiated by OpenAI o3, interleaved reasoning with code to enhance
> multimodal large language models (MLLMs) has become a pivotal research frontier. The existing
> literature focuses primarily on tool-use within vision-perception tasks. However, such
> approaches typically rely on predefined heuristics for visual manipulation and are inherently
> incapable of addressing numerical computation problems due to their exclusive focus on visual
> operations. This paper empowers MLLMs with adaptive interleaved reasoning capabilities through
> extended reinforcement learning training on code-augmented complex numerical computation tasks.
> To this end, we propose a comprehensive three-component solution consisting of: a two-stage
> cold-start data construction pipeline, data filtering strategies for RL dataset curation, and an
> adaptive tool-invocation strategy leveraging a group-constrained reward function for interleaved
> reasoning trajectories. Extensive experiments demonstrate that after Reinforcement Learning
> training with the group-constrained reward function, performance improves by an average of 6.1
> percentage points (pp) on evaluation benchmarks. Specifically, the accuracy for interleaved
> reasoning samples increases by 9.9 pp, and the overall success rate of tool-use exceeds 95%. Our
> data and code are available at: https://github.com/CongHan0808/AIR.git.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
