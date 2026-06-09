---
title: "Agent Paper | SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks"
date: "2026-06-09"
tags: ["Agent", "cs.AI", "cs.CL"]
paper_title: "SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks"
paper_url: "https://arxiv.org/abs/2606.09669v1"
pdf_url: "https://arxiv.org/pdf/2606.09669v1"
arxiv_id: "2606.09669v1"
authors: "Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
- **作者**：Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao et al.
- **arXiv ID**：2606.09669v1
- **分类**：cs.AI, cs.CL

## 摘要原文

> Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to
> perceive and operate within the physical world. However, existing benchmarks predominantly rely
> on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess
> general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark
> designed specifically for evaluating the interactive spatial understanding of multimodal agents
> in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared,
> simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse
> domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under
> vision-only partial observability, actively gathering egocentric visual evidence and expressing
> decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation,
> each task includes a human-validated initial state, a reference trajectory, and a terminal-state
> verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains
> challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only
> 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a
> clear mismatch between task success and execution efficiency, alongside substantial domain-
> specific performance variations. These bottlenecks in active exploration and long-horizon
> planning position SpatialWorld as a rigorous testbed for future spatial agents.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
