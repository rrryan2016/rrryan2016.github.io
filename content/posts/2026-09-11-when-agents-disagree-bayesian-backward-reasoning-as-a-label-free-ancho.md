---
title: "Agent Paper | When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making"
date: "2026-09-11"
tags: ["Agent", "cs.AI", "cs.MA"]
paper_title: "When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making"
paper_url: "https://arxiv.org/abs/2609.11709v1"
pdf_url: "https://arxiv.org/pdf/2609.11709v1"
arxiv_id: "2609.11709v1"
authors: "Ken Chen, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making
- **作者**：Ken Chen, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge
- **arXiv ID**：2609.11709v1
- **分类**：cs.AI, cs.MA

## 摘要原文

> When multiple LLM agents yield conflicting answers, the decision-making process dictates whether
> agent diversity improves performance or merely compounds shared errors. Existing collective
> decision-making methods, including voting, electoral rules, and LLM judges, rely on forward
> reasoning: they map evidence to labels in one direction. Although these methods can combine
> diverse forward traces, they still aggregate estimates that share this evidence-to-label
> factorization and can inherit correlated errors within the forward pool. We therefore construct
> a reverse posterior for each instance through Bayesian backward reasoning from an explicit
> likelihood. The forward and reverse posteriors provide differently factorized approximations of
> the underlying posterior. Because estimates from different factorizations may tend to share the
> same error less often, we use Jensen-Shannon divergence to rank agents by cross-path
> consistency. This cross-path consistency signal underlies three strategies: hard selection
> (MinJS), soft reweighting (FwdJS), and log-linear fusion (LogLin). Evaluated on DDXPlus across
> five LLM backbones, our proposed strategies show consistent improvements: MinJS outperforms
> random selection across all backbones, FwdJS generally improves over the strongest baseline, and
> LogLin achieves the best performance among the evaluated methods, with its largest gains on the
> subset where the agents disagree. Despite its weaker standalone accuracy, the reverse posterior
> serves as a more useful anchor than forward-only alternatives, providing complementary
> information for collective decision-making. When labeled data are available, a lightweight two-
> stage calibration can further refine the reverse anchor and improve aggregation performance.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
