---
title: "Agent Paper | MIRROR: Learning from the Other View for Multi-Modal Reasoning"
date: "2026-07-26"
tags: ["Agent", "cs.AI", "cs.LG"]
paper_title: "MIRROR: Learning from the Other View for Multi-Modal Reasoning"
paper_url: "https://arxiv.org/abs/2607.21552v1"
pdf_url: "https://arxiv.org/pdf/2607.21552v1"
arxiv_id: "2607.21552v1"
authors: "Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：MIRROR: Learning from the Other View for Multi-Modal Reasoning
- **作者**：Wen Ye, Yuxiao Qu, Aviral Kumar, Xuezhe Ma
- **arXiv ID**：2607.21552v1
- **分类**：cs.AI, cs.LG

## 摘要原文

> Unlike large language models (LLMs) that exhibit strong reasoning capabilities, vision-language
> models (VLMs) struggle with visual reasoning, even on geometry problems that admit equivalent
> text, diagram, and combined diagram+text views. We show that these views often elicit different
> behaviors: a model may solve a problem from text but fail on the corresponding diagram, or
> succeed visually while failing textually. This inconsistency suggests that different views
> expose complementary reasoning paths and failure modes that standard multimodal post-training
> does not fully exploit. To study and exploit this phenomenon, we construct ODA-Data, a high-
> quality paired multimodal geometry dataset with text-dominant, image-dominant, and combined
> image+text views of the same problems, together with splits for training and evaluating
> modality-dependent reasoning behaviors. We then develop Modality-Informed Reciprocal Reasoning
> Optimization (MIRROR), a reinforcement learning approach for improving multimodal reasoning via
> self supervision. For each problem, MIRROR evaluates the model under all views, selects the
> best-performing view as a teacher, and trains other views with a reverse-KL objective towards
> the teacher. Across reasoning benchmarks that evaluate on geometry problems, MIRROR improves
> over standard RL and yields more accurate and consistent behavior across modalities

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
