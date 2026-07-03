---
title: "Agent Paper | Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study"
date: "2026-07-03"
tags: ["Agent", "cs.SE", "cs.AI"]
paper_title: "Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study"
paper_url: "https://arxiv.org/abs/2607.02436v1"
pdf_url: "https://arxiv.org/pdf/2607.02436v1"
arxiv_id: "2607.02436v1"
authors: "Achint Mehta"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Reasoning effort, not tool access, buys first-try reliability in agentic code generation: an observational study
- **作者**：Achint Mehta
- **arXiv ID**：2607.02436v1
- **分类**：cs.SE, cs.AI

## 摘要原文

> Agentic coding assistants are increasingly given extra capabilities, such as browser based
> testing tools and design oriented system prompts, on the assumption that more capability yields
> better software. This study tested that assumption directly. Ninety independent agent runs built
> the same application, a real time retrospective board, from one detailed specification, each
> scored on a fixed 14 criterion functional rubric (42 point maximum) and a visual quality review.
> The runs spanned several model generations, two agent harnesses, two reasoning effort levels, a
> testing tool, and two design oriented prompts. Capability tier dominated: frontier models
> clustered near the ceiling while a low cost local model fell to 24 to 37 points. A criterion
> level analysis revealed what run totals conceal. Container deployment was the dominant defect,
> failing first try in 44 percent of runs, with its failure rate shifting sharply across model
> generations while mean totals moved less than a point. The testing tool raised cost by 42 to 68
> percent without improving functional score or reliability, even on interface visible criteria.
> Raising reasoning effort from High to xHigh lifted first try perfect runs from 28 percent to 89
> percent and cut corrective prompts about five fold, for 9 to 29 percent more cost. A design
> oriented prompt raised visual quality, 4.5 versus 3.0 on a 5 point scale, without lifting
> function, and a one paragraph paraphrase of its directive reproduced the entire lift. The
> practical lesson is to match the fix to the failure: most first run failures came from weak
> reasoning, which a stronger model or more effort prevents, not from visible flaws a checking
> tool would catch.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
