---
title: "Remote Sensing Paper | GeoThreat: Transferable Targeted Adversarial Attacks on Large Vision-Language Models for Remote Sensing Image Interpretation"
date: "2026-07-25"
tags: ["Remote Sensing", "cs.CV"]
paper_title: "GeoThreat: Transferable Targeted Adversarial Attacks on Large Vision-Language Models for Remote Sensing Image Interpretation"
paper_url: "https://arxiv.org/abs/2607.21036v1"
pdf_url: "https://arxiv.org/pdf/2607.21036v1"
arxiv_id: "2607.21036v1"
authors: "Yimin Fu, Yuefeng Bai, Baicheng Pan, Zhunga Liu, Michael K. Ng"
summary_model: "fallback-llm-error"
---
## 论文速览

这篇论文属于 **Remote Sensing** 方向。由于当前环境没有配置 `OPENAI_API_KEY` 或 `LLM_API_KEY`，本文先保存 arXiv 元数据和摘要，方便你后续人工润色或重新运行大模型摘要生成。

- **论文标题**：GeoThreat: Transferable Targeted Adversarial Attacks on Large Vision-Language Models for Remote Sensing Image Interpretation
- **作者**：Yimin Fu, Yuefeng Bai, Baicheng Pan, Zhunga Liu, Michael K. Ng
- **arXiv ID**：2607.21036v1
- **分类**：cs.CV

## 摘要原文

> Adversarial attacks against large vision-language models (LVLMs) serve as an effective means of
> assessing their robustness in cross-modal semantic understanding. Existing studies mainly focus
> on corrupting visual inputs to induce predefined erroneous responses in general vision-language
> tasks, whereas corresponding investigations in remote sensing fields remain largely
> underexplored. Compared with natural image understanding, remote sensing image interpretation
> requires joint reasoning over local discriminative cues and global scene context. This poses
> additional challenges to achieving transferable semantic manipulation toward specified responses
> under black-box settings. To tackle these challenges, we propose GeoThreat, a transferable
> targeted adversarial attack method against LVLMs for remote sensing image interpretation.
> Specifically, GeoThreat modulates adversarial representations in accordance with the target
> content at both conceptual and perceptual levels. The class tokens from surrogate image encoders
> are employed as conceptual representations, while perceptual representations are distilled from
> patch tokens of the adversarial example through collaborative importance estimation. Beyond
> merely rolling out attention scores across layers, we incorporate adversarial-target similarity
> gradients to more faithfully characterize the relevance of local visual cues to the intended
> semantic manipulation. The perceptual representations are then dynamically aligned with target
> patch tokens in a cross-attentive manner, facilitating the adaptation of local cues toward
> designated semantic details. Finally, adversarial perturbations are iteratively updated via
> ensemble-based joint optimization of conceptual calibration and perceptual adaptation. Extensive
> experiments across diverse LVLMs demonstrate the superiority of GeoThreat in both
> transferability and controllability.

## 阅读提示

建议重点检查论文是否提供了新的任务设定、数据集、模型结构、评测协议或 Agent 工作流设计。如果它只提出概念性框架，需要进一步阅读正文确认实验强度和可复现性。

## 对我的研究启发

由于当前文章是 fallback 摘要，还没有调用大模型进行个性化分析。建议人工阅读时重点判断它是否能迁移到遥感变化检测、变化描述、遥感 VLM 或 Agent 科研流程中，例如是否能改进双时相特征对齐、变化区域解释、跨模态指令数据构造、工具调用式误差分析或自动实验编排。

## 可实践方案

- 将论文中的核心建模思路映射到双时相遥感输入，设计一个最小可行 baseline。
- 检查是否能构造变化检测/变化描述指令数据，用于 VLM 微调或评测。
- 设计一组消融实验，比较原始方法、遥感适配版本和现有变化检测模型。
- 如果论文涉及 Agent，将其拆解为数据检索、模型推理、结果评估、错误归因等可调用工具链。
