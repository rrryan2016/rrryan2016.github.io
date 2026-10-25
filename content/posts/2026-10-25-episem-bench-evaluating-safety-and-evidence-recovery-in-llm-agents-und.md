---
title: "Agent Paper | EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence"
date: "2026-10-25"
tags: ["Agent", "cs.AI", "cs.LG"]
paper_title: "EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence"
paper_url: "https://arxiv.org/abs/2610.31650v1"
pdf_url: "https://arxiv.org/pdf/2610.31650v1"
arxiv_id: "2610.31650v1"
authors: "Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai, Shuang Qiu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence
- **作者**：Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai et al.
- **arXiv ID**：2610.31650v1
- **分类**：cs.AI, cs.LG

## 摘要原文

> Tool-using language model agents rely on environmental facts to decide whether an action is
> permitted. When a tool response omits a safety-relevant fact, an agent may carry out a
> prohibited action even though the user request is benign and every returned statement is true.
> We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety
> boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched
> unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the
> benchmark measures unsafe execution under critical evidence omission and determines the minimum
> observed failure cardinality, including failures with full evidence and cases with no observed
> failure after exhaustive testing. An independent audit tool tests whether agents seek missing
> facts and then withhold prohibited actions while completing permissible tasks. The benchmark
> reveals substantial variation across the ten models in omission robustness, evidence
> acquisition, and appropriate action. Resistance to missing evidence does not necessarily
> translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but
> agents differ in whether they actively obtain the missing facts and use them to act
> appropriately in both worlds.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
