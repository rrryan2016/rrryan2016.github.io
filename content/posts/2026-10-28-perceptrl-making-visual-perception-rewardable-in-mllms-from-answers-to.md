---
title: "Agent Paper | PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions"
date: "2026-10-28"
tags: ["Agent", "cs.CV", "cs.AI"]
paper_title: "PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions"
paper_url: "https://arxiv.org/abs/2610.37471v1"
pdf_url: "https://arxiv.org/pdf/2610.37471v1"
arxiv_id: "2610.37471v1"
authors: "Tongkun Guan, Zhibo Yang, Mingkun Yang, Haocheng Wang, Wei Shen, Xiaokang Yang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：PerceptRL: Making Visual Perception Rewardable in MLLMs from Answers to Interactions
- **作者**：Tongkun Guan, Zhibo Yang, Mingkun Yang, Haocheng Wang, Wei Shen, Xiaokang Yang
- **arXiv ID**：2610.37471v1
- **分类**：cs.CV, cs.AI

## 摘要原文

> Fine-grained visual perception remains a bottleneck during post-training of multimodal large
> language models (MLLMs), as perceptual errors can constrain gains from reasoning-focused
> optimization. Although image-caption pre-training improves perception, its influence can weaken
> as subsequent stages change data mixtures and objectives. Continuing caption supervision during
> post-training is challenging because subjective, information-dense descriptions complicate
> verifiable reward design. We present PerceptRL, which strengthens perception at two
> complementary levels. Perception RL uses a multi-agent pipeline to extract verified errors from
> dense image captions and convert the corresponding visual facts into QA pairs with fixed answer
> labels and rule-based rewards. Chain QA links correlated errors, while multiple-choice QA
> combines unrelated errors. A specialized route targets high-error domains with tailored
> verification, and a domain-agnostic general route covers errors beyond these domains. Perception
> Agentic RL addresses fine-grained and dense cases unresolved by single-turn Perception RL
> through multi-turn inspection with visual tools. We observe coordinate drift even in models
> trained to use tools, where incorrect crops or annotations distort evidence and propagate
> errors. Coordinate Injection corrects spatial operations in cold-start trajectories, while a
> grounding-aware process reward supervises intermediate spatial fidelity alongside final-answer
> correctness. Training proceeds through shared cold-start SFT, single-turn Perception RL, and
> multi-turn Perception Agentic RL. Across seven benchmarks under a shared tool-use protocol,
> PerceptRL achieves 71.6% average accuracy, surpassing the base model with the same tools and the
> strongest evaluated frontier VLM by 15.7 and 5.2 percentage points, respectively.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
