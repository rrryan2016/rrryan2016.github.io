---
title: "Agent Paper | Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching"
date: "2026-09-02"
tags: ["Agent", "cs.RO", "cs.AI"]
paper_title: "Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching"
paper_url: "https://arxiv.org/abs/2609.01404v1"
pdf_url: "https://arxiv.org/pdf/2609.01404v1"
arxiv_id: "2609.01404v1"
authors: "Jaewoo Park, Minyoung Lee, Sukmin Seo, Moonbin Yim, Hyunwook Yoon, Dohoon Ryu, Daehee Kim, Myungseo Song, Jihyuk Byun, Seunggyu Chang, Taeho Kil, Jiseob Kim, Bado Lee, Geewook Kim"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching
- **作者**：Jaewoo Park, Minyoung Lee, Sukmin Seo, Moonbin Yim, Hyunwook Yoon, Dohoon Ryu et al.
- **arXiv ID**：2609.01404v1
- **分类**：cs.RO, cs.AI

## 摘要原文

> Multimodal Large Language Models (MLLMs) are strong perceivers of images and video. We ask how
> far that reach extends into acting: dropping an MLLM directly into a drone's control loop, with
> its entire action space declared solely in the prompt. Recent systems approach this setting but
> increasingly narrow the model's decision-making. We widen it back. We introduce DroneCATS-Agent,
> an architecture where the MLLM is a swappable component, and DroneCATS, a benchmark treating the
> model as the independent variable. Beyond merely flying toward a pixel, our agent entrusts the
> model to yaw and search, deliberate when unsure, and self-declare arrival---all without fine-
> tuning or function-calling schemas. Evaluating frontier and open models across four core
> capabilities---approaching a visible target, tracking a moving one, searching outside the
> initial view, and commanding a multi-drone fleet---reveals that even the simplest embodied
> settings are far from solved. Crucially, to identify what breaks first at the edge, our roster
> scales down to 2B parameters. The findings expose a stark paradox: it is not the flying that
> fails. Small open models often navigate into the success radius more reliably than frontier
> models, yet lose the episode by declaring arrival prematurely or not at all. Multi-drone
> commanding amplifies this divide, with small models failing by blindly copying a single
> coordinate across distinct views. Viewed as vision-language-action agents, the models' spatial
> perception holds up, but their action protocol does not. What separates a deployable edge model
> from a frontier model is not navigation, but the discipline to sustain a declared protocol and
> emit the correct terminating action. The open problem is closing this gap at onboard compute
> costs---yielding a fast model that plans persistently and knows exactly when it is done---and
> DroneCATS is built to measure that distance.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
