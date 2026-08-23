---
title: "Agent Paper | PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents"
date: "2026-08-23"
tags: ["Agent", "cs.AI", "cs.CL", "cs.LG"]
paper_title: "PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents"
paper_url: "https://arxiv.org/abs/2608.19861v1"
pdf_url: "https://arxiv.org/pdf/2608.19861v1"
arxiv_id: "2608.19861v1"
authors: "Seongjae Kang, Taehyung Yu, Sung Ju Hwang"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents
- **作者**：Seongjae Kang, Taehyung Yu, Sung Ju Hwang
- **arXiv ID**：2608.19861v1
- **分类**：cs.AI, cs.CL, cs.LG

## 摘要原文

> Customer-service LLM agents must follow organizational policy when acting on a user's behalf.
> Compliance failures arise from either forbidden actions, such as granting an ineligible change,
> or omitted procedural requirements, such as identification or confirmation. Runtime safeguards
> can intervene on risky actions, but action-local checks do not guide an agent through a multi-
> step procedure. Workflow-following systems support prescribed process execution, but primarily
> target workflow completion rather than safeguarding agent behavior. PolicyGuide instead compiles
> each domain policy into a workflow graph and invokes a proactive verifier at user-turn
> boundaries. From persisted graph state, the verifier reconciles open requests and returns step-
> specific remediation along a policy-compliant path. Across the $τ^2$-bench airline, retail, and
> telecom domains with a GPT-5.4 agent and verifier, PolicyGuide raises mean $\mathrm{Pass}^4$
> from $0.42$ to $0.62$, with the largest gain on telecom ($0.19$ to $0.61$), the most workflow-
> structured domain. The same workflows transfer to Claude Sonnet 4.6 and Gemini 2.5 Pro agents.
> Complementary evaluations find the lowest observed attack-success rate under adversarial users
> and the strongest procedural compliance in an author-designed workflow-level validation.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
