---
title: "Agent Paper | Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination"
date: "2026-11-16"
tags: ["Agent", "cs.AI", "cs.CL"]
paper_title: "Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination"
paper_url: "https://arxiv.org/abs/2611.18514v1"
pdf_url: "https://arxiv.org/pdf/2611.18514v1"
arxiv_id: "2611.18514v1"
authors: "Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination
- **作者**：Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao
- **arXiv ID**：2611.18514v1
- **分类**：cs.AI, cs.CL

## 摘要原文

> Mechanistic Interpretability (MI) has made significant progress in explaining the internal
> computations of Large Language Models (LLMs); however, these advances have yet to demonstrate
> comparable success in explaining the decision-making processes of LLM-based agents. This paper
> examines the challenges MI tools face when applied to realistic agentic failures. We focus on
> one such failure: web agents hallucinating actions that are not available on a website. We apply
> a series of mechanistic analyzes to Qwen2.5-7B-Instruct as it interacts with live websites. We
> find that a linear probe trained on the last prompt token can predict hallucinations before
> generation begins (0.80 AUC) and steering along a probe direction corrects 85\% of
> hallucinations, but disrupts 7\% of valid actions. However, these results only provide a partial
> explanation of why the agent hallucinates. The probe direction is sensitive to prompt
> formatting, losing much of its steering effect after a minor change to how actions are
> represented. Additionally, circuit identification can be difficult as the computation is
> distributed across multiple components and positions, and the information the agent relies on
> varies across examples. We discuss how these observations challenge the assumptions underlying
> standard MI methods for circuit discovery and feature identification, and outline future
> directions for making these methods better suited to explain failures in LLM-based agents.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
