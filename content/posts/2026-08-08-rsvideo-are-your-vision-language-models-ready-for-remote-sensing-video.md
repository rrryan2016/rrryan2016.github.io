---
title: "Remote Sensing Paper | RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?"
date: "2026-08-08"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?"
paper_url: "https://arxiv.org/abs/2608.02039v2"
pdf_url: "https://arxiv.org/pdf/2608.02039v2"
arxiv_id: "2608.02039v2"
authors: "Hongjie Zhou, Shiqin Wang, Haoyang Chen, Haonan Guo, Di Wang, Juhua Liu, Fu Lin, Yong Luo"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：RSVideo: Are Your Vision-Language Models Ready for Remote Sensing Videos?
- **作者**：Hongjie Zhou, Shiqin Wang, Haoyang Chen, Haonan Guo, Di Wang, Juhua Liu et al.
- **arXiv ID**：2608.02039v2
- **分类**：cs.CV

## 摘要原文

> Remote-sensing videos enable real-time observation of changes in target attributes, short-term
> activities, and scene evolution. They record motion, actions, interactions, and scene changes
> that cannot be captured by isolated images. Existing models primarily target single images or
> discrete temporal observations spanning a long time range. However, a unified evaluation setting
> for assessing vision-language models on continuous remote-sensing video understanding remains
> lacking. We introduce RSVideo-10K, a remote-sensing video dataset comprising 10,773 instances,
> 1.47 million frames, and 17.02 hours of footage, containing both unmanned aerial vehicles and
> satellite platforms. Its fixed evaluation benchmark, RSVideo-Bench, contains 2,731 test
> instances and evaluates two complementary aspects of remote-sensing video understanding: L1
> Perception and L2 Reasoning, spanning seven capability groups and 17 tasks. Evaluations show
> that current vision-language models still struggle to recover small local evidence, track short-
> lived states, and use scene-constrained spatial relations. Based on this analysis, we further
> propose RSVideo, a reinforcement learning framework for small-target spatiotemporal focusing
> that selects question-relevant regions across frames and suppresses redundant background tokens.
> RSVideo achieves a maximum absolute improvement of 9.01% with InternVL3.5-14B and attains the
> highest accuracy of 40.63% with Qwen3.6-27B across 26 open-source vision-language backbones.
> Codes will be available at https://github.com/HongjieZhou0329/RSVideo.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
