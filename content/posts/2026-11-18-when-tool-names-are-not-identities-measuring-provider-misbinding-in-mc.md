---
title: "Agent Paper | When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents"
date: "2026-11-18"
tags: ["Agent", "cs.CR", "cs.AI"]
paper_title: "When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents"
paper_url: "https://arxiv.org/abs/2611.21577v1"
pdf_url: "https://arxiv.org/pdf/2611.21577v1"
arxiv_id: "2611.21577v1"
authors: "Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Agent** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents
- **作者**：Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani
- **arXiv ID**：2611.21577v1
- **分类**：cs.CR, cs.AI

## 摘要原文

> Large language model (LLM) applications increasingly act as agents that select and invoke
> external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing
> clients to compose tools advertised by multiple servers. However, tool metadata used for
> discovery and selection is not, by itself, necessarily bound to a verified provider identity.
> This paper studies this gap as tool-provider misbinding: a failure in which a request intended
> for a legitimate provider is instead resolved to an attacker-controlled tool. The attacker does
> not compromise the host, LLM, legitimate server, or network channel; it only operates another
> MCP server that advertises tools with chosen metadata. We formulate tool provider misbinding as
> an attacker-controlled tool-selection optimization problem and evaluate it in a controlled MCP
> environment across five LLM-based clients. The results show that interactions drive misbinding.
> The strongest failures occur when exact-name collision, task-aligned description, and compatible
> schema reinforce one another, but authority-enhanced descriptions with compatible schema can
> also cause wrong-provider execution or unresolved provider ambiguity without name collision.
> Different models expose the same provider-binding weakness differently, including attacker-
> controlled provider selection, clarification requests, and unstable or inconsistent provider
> resolution.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
