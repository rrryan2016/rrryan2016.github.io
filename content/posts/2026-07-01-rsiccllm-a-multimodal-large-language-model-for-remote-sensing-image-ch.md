---
title: "Remote Sensing Paper | RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning"
date: "2026-07-01"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning"
paper_url: "https://arxiv.org/abs/2606.28266v1"
pdf_url: "https://arxiv.org/pdf/2606.28266v1"
arxiv_id: "2606.28266v1"
authors: "Yelin Wang, Zijia Song, Shuo Ye, Chuanguang Yang, Miaoyu Wang, Yong Xu, Zhulin An, Yongjun Xu, Zitong Yu"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning
- **作者**：Yelin Wang, Zijia Song, Shuo Ye, Chuanguang Yang, Miaoyu Wang, Yong Xu et al.
- **arXiv ID**：2606.28266v1
- **分类**：cs.CV

## 摘要原文

> Remote Sensing Image Change Captioning (RSICC) aims to describe changes between bi-temporal
> remote sensing images and holds significant research and application value. However, most
> existing methods rely on conventional deep learning architectures, and the limited model
> capacity constrains performance. Although large-model post-training techniques have achieved
> great success in general domains, their direct transfer to RSICC remains challenging due to data
> scarcity and the need for fine-grained change understanding. To address this, we propose
> RSICCLLM, the first post-training framework for large vision-language models in RSICC.
> Specifically, we design a data generation paradigm, release the instruction dataset RSICI, and
> establish a task-specific RSICC benchmark. We further introduce Difference-aware Supervised
> Fine-tuning to explicitly extract change representations and guide the model in perceiving and
> understanding temporal differences. In addition, we propose Dual-Negative Preference
> Optimization (DNPO), which employs two complementary negative-sample construction strategies to
> construct the preference dataset RSICP and further refine model performance. Extensive
> experiments validate the superior capability of RSICCLLM, which achieves outstanding results
> with only 7B parameters, surpassing models of substantially larger scales. The code and dataset
> will be made publicly available at https://github.com/keaill/RSICCLLM.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
