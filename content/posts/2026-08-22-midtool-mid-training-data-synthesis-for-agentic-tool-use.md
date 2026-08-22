---
title: "Agent Paper | MidTool: Mid-training Data Synthesis for Agentic Tool Use"
date: "2026-08-22"
tags: ["Agent", "cs.AI"]
paper_title: "MidTool: Mid-training Data Synthesis for Agentic Tool Use"
paper_url: "https://arxiv.org/abs/2608.20314v1"
pdf_url: "https://arxiv.org/pdf/2608.20314v1"
arxiv_id: "2608.20314v1"
authors: "Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, Radha Poovendran, Yuxiong He"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：MidTool: Mid-training Data Synthesis for Agentic Tool Use
- **作者**：Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao et al.
- **arXiv ID**：2608.20314v1
- **分类**：cs.AI

## 摘要原文

> Mid-training is increasingly recognized as a critical stage for shaping the capabilities of
> large language models. Recent work has shown that targeted mid-training can strengthen
> reasoning-intensive abilities such as math and science, and can also improve agentic
> capabilities in software-engineering settings. In this work, we study the parallel but less
> explored agentic capability: general tool use. We present MidTool, an open corpus construction
> pipeline for agentic tool-use mid-training that combines large-scale web, PDF, and code data
> with synthesized supervision from real-world tool APIs, MCP skills, and document-grounded
> workflows. MidTool is designed to teach models how to recognize tool affordances, ground
> arguments from context, compose tool call workflow, and recover from incomplete information. We
> mid-train Qwen3-4B-Base and Qwen3-8B-Base on MidTool-Mix, and then apply follow-up post-training
> with both supervised fine-tuning and reinforcement learning. Compared with baselines, MidTool-
> Mix consistently improves downstream performance under both SFT and RL on BFCL, tau2-Bench, and
> MCP Universe. These results suggest that general tool use, like other important LLM
> capabilities, benefits from dedicated mid-training rather than being left entirely to post-
> training.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
