---
title: "Agent Paper | LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems"
date: "2026-06-21"
tags: ["Agent", "cs.CR", "cs.AI"]
paper_title: "LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems"
paper_url: "https://arxiv.org/abs/2606.20408v1"
pdf_url: "https://arxiv.org/pdf/2606.20408v1"
arxiv_id: "2606.20408v1"
authors: "Hanwool Lee, Dasol Choi, Bokyeong Kim, Seung Geun Kim, Haon Park"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems
- **作者**：Hanwool Lee, Dasol Choi, Bokyeong Kim, Seung Geun Kim, Haon Park
- **arXiv ID**：2606.20408v1
- **分类**：cs.CR, cs.AI

## 摘要原文

> Large language model (LLM) agents are increasingly proposed as supervisory components for
> safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure
> remains poorly characterized. We present NRT-Bench, a benchmark for multi-turn red-teaming of
> LLM agents acting as operators of a safety-critical system, instantiated in a simulated nuclear
> power plant control room. A five-role operator team, each backed by a configurable LLM, runs a
> plant governed by six critical safety functions (CSFs), while adversaries inject messages over
> four channels in bounded multi-turn sessions with per-turn feedback. Harm is an objective signal
> rather than LLM-judged text: a run terminates the moment any CSF is lost, attributed to the
> causing message. Evaluating four frontier operator models under a fixed-attack paired-replay
> protocol, we find that adaptive multi-turn attacks reliably push the operator team past a safety
> limit: across the four models, between 8.7% and 12.1% of attack sessions end with the plant
> losing a critical safety function. Although the four models look almost equally robust by this
> aggregate rate, their failures barely overlap: of $149$ sessions, none defeat all four models
> while a third defeat at least one, so vulnerabilities are nearly disjoint across models rather
> than nested. The effect of added defences is strongly model-dependent: the same guardrail stack
> or safety-advisor agent that lowers attack success for one model can raise it for another. We
> release the simulation venue, attack dataset, and replay tooling for reproducible safety
> evaluation of LLM agents.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
