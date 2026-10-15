---
title: "Agent Paper | Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents"
date: "2026-10-15"
tags: ["Agent", "cs.SE", "cs.AI"]
paper_title: "Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents"
paper_url: "https://arxiv.org/abs/2610.20344v1"
pdf_url: "https://arxiv.org/pdf/2610.20344v1"
arxiv_id: "2610.20344v1"
authors: "Yuyao Ge, Shenghua Liu, Peizhong Gao, Chendi Ge, Chenxu Liu, Yiwei Wang, Lingrui Mei, Baolong Bi, Jiayu Yao, Jiafeng Guo, Xueqi Cheng"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents
- **作者**：Yuyao Ge, Shenghua Liu, Peizhong Gao, Chendi Ge, Chenxu Liu, Yiwei Wang et al.
- **arXiv ID**：2610.20344v1
- **分类**：cs.SE, cs.AI

## 摘要原文

> Agents driven by large language models are increasingly deployed on long-horizon tasks, where
> they use tools and modify real workspaces. How well they perform depends as much on the harness
> around the model as on the model itself. Existing benchmarks measure downstream task success
> under a fixed harness, leaving harness engineering itself unexplored. We propose Doc2Harness, a
> two-stage benchmark that evaluates long-horizon harness engineering directly. In Stage 1, a
> build model operating inside a fixed builder harness receives an interface-only contract
> skeleton and a development document that consolidates behavior across twelve frontier harnesses,
> and then constructs a complete candidate harness in an isolated container. In Stage 2, the
> frozen candidate harness runs in containers separate from the construction environment, one per
> test case, and is driven end to end by a scripted mock model. We score each test case using four
> observable channels, namely the requests sent to the model, the files on disk, the process exit
> code, and the command output; positive controls rule out vacuous passes. Across nineteen
> frontier models, each evaluated with three independent builds on 328 test cases, GPT-6 Astra
> achieves the highest pass rate at 53.05%, while the weakest model reaches 27.44%, a gap of
> roughly twenty-six percentage points. Even the strongest model fails nearly half of the test
> cases, and failures cluster around how cross-cutting functionality is split across modules. To
> our knowledge, Doc2Harness provides the first deterministic benchmark for measuring long-horizon
> harness engineering.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
