---
title: "Agent Paper | Candidate supply and answer selection shape the value of LLM judging in multi-agent systems"
date: "2026-08-28"
tags: ["Agent", "cs.AI", "cs.MA"]
paper_title: "Candidate supply and answer selection shape the value of LLM judging in multi-agent systems"
paper_url: "https://arxiv.org/abs/2608.25937v1"
pdf_url: "https://arxiv.org/pdf/2608.25937v1"
arxiv_id: "2608.25937v1"
authors: "Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：Candidate supply and answer selection shape the value of LLM judging in multi-agent systems
- **作者**：Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan
- **arXiv ID**：2608.25937v1
- **分类**：cs.AI, cs.MA

## 摘要原文

> Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still
> report a wrong answer. Explaining this outcome is difficult because generation, communication
> and final answer-selection rules usually change simultaneously. We conceptualize multi-agent
> reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal
> selection, wherein consensus without quality control can exhibit patterns of memetic drift. We
> study two questions: (1) when an LLM judge provides effective selection pressure by supplying a
> signal of answer correctness for candidates generated in a multi-agent system, and (2) when
> using that signal improves the reported answer. To map judge reliability, we analysed 15,336
> questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed
> separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278
> questions across five benchmarks. We report three findings. (1) A correct answer is often
> already present among the generated candidates, but the system can still converge on and report
> a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the
> task, the generator and how rare the correct answer is. (3) Combining answer frequency with the
> judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82%
> to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors.
> In the systems studied here, the value of generating more candidates depends on whether those
> extra samples make correct answers present, frequent or recognisable. By isolating generation,
> recognition and selection, these findings establish a diagnostic basis for designing multi-agent
> architectures that protect generated correct answers from being lost.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
