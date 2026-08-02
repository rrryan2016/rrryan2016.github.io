---
title: "Agent Paper | ORCA-bench: How Ready Are Language Model Agents for Oncall?"
date: "2026-08-02"
tags: ["Agent", "cs.CL", "cs.AI", "cs.SE"]
paper_title: "ORCA-bench: How Ready Are Language Model Agents for Oncall?"
paper_url: "https://arxiv.org/abs/2607.28545v1"
pdf_url: "https://arxiv.org/pdf/2607.28545v1"
arxiv_id: "2607.28545v1"
authors: "Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：ORCA-bench: How Ready Are Language Model Agents for Oncall?
- **作者**：Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal et al.
- **arXiv ID**：2607.28545v1
- **分类**：cs.CL, cs.AI, cs.SE

## 摘要原文

> Large language models can write, patch, and search code, but oncall root cause analysis (RCA)
> demands something different: reasoning over noisy metrics, logs, traces, and source code,
> starting from ambiguous user-facing reports, often hours after the incident began. We introduce
> ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall
> setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system--exposing six
> days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, and
> OpenSearch via Grafana) and full source-code access--with 1,079 RCA tasks that systematically
> vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth
> symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-
> scored by humans (Cohen's $κ_w=0.90$). Across five frontier agents, the best RCA Accuracy is
> 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard--a gap that
> remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in
> 40% of incident reports, and removing source-code access degrades every metric. Crucially, these
> are performances on a curated 50 GB / six-day testbed with tasks investigated in isolation on a
> system whose code and instrumentation are public. Since real production systems are order of
> magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on
> the engineering investment required before frontier coding agents can be safely entrusted with
> production reliability. We release the public set at
> https://hub.harborframework.com/datasets/orca-bench/ORCA-bench.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
