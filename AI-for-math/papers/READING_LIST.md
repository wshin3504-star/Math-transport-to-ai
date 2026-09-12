# 30 篇精读论文清单（Phase 0，约 6–8 周完成）

> 节奏：每天 1 篇，精读 45 分钟。笔记写到 `papers/notes/NN-短名.md`。
> 笔记模板：**问题 → 方法 → 关键实验/结果 → 对我项目的启发 → 疑问**。
> 标了 ⭐ 的是「必须能对别人 5 分钟讲清楚」的核心论文。
> 没有 arXiv 号的按标题在 Google Scholar / arXiv 搜索。

## Tier A：LLM 与 Agent 打底（Week 1–2）

| # | 论文 | 出处 | 为什么读 / 重点 |
|---|---|---|---|
| 1 ⭐ | Attention Is All You Need | NeurIPS 2017, arXiv:1706.03762 | 一切的地基。重点：self-attention 公式逐行推一遍（你对二次型很熟，会很快） |
| 2 | Language Models are Few-Shot Learners (GPT-3) | NeurIPS 2020, arXiv:2005.14165 | 理解 in-context learning 与 scaling 曲线；只精读 1–2 章 |
| 3 ⭐ | Training LMs to follow instructions with human feedback (InstructGPT) | arXiv:2203.02155 | RLHF 三段式（SFT→RM→PPO），后训练范式鼻祖 |
| 4 | LoRA | ICLR 2022, arXiv:2106.09685 | 低秩适配——你没算力时唯一的微调方式，必须会用 |
| 5 ⭐ | Chain-of-Thought Prompting | NeurIPS 2022, arXiv:2201.11903 | 推理范式的起点，看测试时计算的开端 |
| 6 ⭐ | ReAct: Synergizing Reasoning and Acting | ICLR 2023, arXiv:2210.03629 | **Agent 开山作**，你未来面试必讲；思考-行动交替的 agent loop |
| 7 | Toolformer | NeurIPS 2023, arXiv:2302.04761 | 模型自学调工具；与 Lean verifier 调用对照看 |
| 8 | Reflexion | NeurIPS 2023, arXiv:2303.11366 | 语言反馈作为强化信号；prover 失败修复的思想来源 |

## Tier B：形式化定理证明主线（Week 3–5，你的主战场）

| # | 论文 | 出处 | 为什么读 / 重点 |
|---|---|---|---|
| 9 | miniF2F | NeurIPS 2021 Datasets, arXiv:2109.00110 | 领域标准 benchmark，看懂评測口径 |
| 10 | Generative Language Modeling for ATP (GPT-f) | arXiv:2009.03393 | OpenAI 早期尝试，了解搜索+采样范式起源 |
| 11 ⭐ | HyperTree Proof Search (HTPS) | NeurIPS 2022, arXiv:2205.11491 | MCTS 式证明搜索经典；理解值网络/策略网络分工 |
| 12 ⭐ | LeanDojo / ReProver | NeurIPS 2023, arXiv:2306.15626 | **你的第一优先复现对象**：开源 Lean 交互环境+检索增强证明 |
| 13 | Draft, Sketch, and Prove (DSP) | ICLR 2023, arXiv:2210.12283 | 非正式→正式的两级证明范式（DeepSeek-Prover-V2 子目标分解的前身） |
| 14 | Baldur: Whole-Proof Generation and Repair | arXiv:2303.04910 | 整证明生成+错误修复循环，工程上最接近 agent 的形态 |
| 15 | Prover-Verifier Games | arXiv:2109.12265 | 可验证性思想，对应现在的 R1 可读性奖励 |
| 16 ⭐ | DeepSeek-Prover V1 | arXiv:2405.14333 | 大规模合成数据 + Lean 验证闭环；精读数据管线设计 |
| 17 | LLEMMA / Proof-Pile-2 | arXiv:2310.10631 | 数学预训练语料怎么建，autoformalization 数据从哪来 |
| 18 ⭐ | AlphaProof | Nature 2025, doi:10.1038/s41586-025-09833-y（正式版 2025.11 发表，Hubert et al.） | IMO 银牌系统；重点看 Lean 环境如何接入 RL。**PDF 未入库**：nature.com 反爬，浏览器打开 https://www.nature.com/articles/s41586-025-09833-y.pdf 手动保存为 `18-alphaproof-nature2025.pdf` |
| 19 ⭐ | DeepSeek-Prover-V2 | arXiv:2504.21801 | 子目标分解 + 冷启动 + RL 的完整配方，当前最强开源 prover |
| 20 | BPT: Best-first Panther Tree Search (DeepSeek) | arXiv 2502.18076（搜标题确认） | 搜索预算分配——你未来做 API 预算分配研究的直接参照 |

## Tier C：前沿拓展与就业接口（Week 6–8）

| # | 论文 | 出处 | 为什么读 / 重点 |
|---|---|---|---|
| 21 ⭐ | AlphaGeometry | Nature 2024, doi:10.1038/s41586-023-06747-5 | 符号引擎+LLM 混合架构，**几何**证明——离你专业最近。**PDF 未入库**：浏览器打开 https://www.nature.com/articles/s41586-023-06747-5.pdf 手动保存为 `21-alphageometry-nature2024.pdf` |
| 22 | Lean-STaR | arXiv:2407.04051 | 思维轨迹+自举训练在证明上的应用 |
| 23 | Lean Copilot | arXiv 2406.06913（搜标题确认） | Lean 内的 LLM 辅助证明工具链，直接可上手玩 |
| 24 | PutnamBench | arXiv 2410.15794（搜标题确认） | Putnam 题 benchmark；将来你的 prover 就在这里刷榜 |
| 25 | ProofNet | arXiv 2302.13333（搜标题确认） | 本科数学 autoformalization 评测——你的几何数据集的直接先例 |
| 26 | Kimina-Prover Preview | arXiv 2504.01995（搜标题确认） | 2025 年国内工业界 prover，看工程化差距 |
| 27 ⭐ | DeepSeek-R1 | arXiv:2501.12948 | 可验证奖励 RL（GRPO）的里程碑，Agentic RL 次选线的核心 |
| 28 | SubgoalXL | arXiv 2405.07079（搜标题确认） | 子目标式示范学习，与 V2 对照 |
| 29 | Formal Mathematics Statement Curriculum Learning (Polu et al.) | arXiv:2302.12414 | 课程学习怎么选难题——你出「几何分析定理集」时的方法论 |
| 30 | SWE-agent | arXiv:2405.15793 | 从数学 prover 到 code agent 的接口，对准 GLM-Code Agent 这类 JD |

## 备选 / 追踪（不占 30 篇名额）

- DeepSeekMath (GRPO 出处)，arXiv:2402.03300 — 读 27 之前先扫一眼 ✅ `31-deepseekmath-2402.03300.pdf`
- Lean Agent (agentic RL, arXiv 2408.06628) ✅ `32-lean-agent-2408.06628.pdf`
- **AlphaProof Nexus**（arXiv:2605.22763，2026.06）：AlphaProof 团队的后续——大规模评估形式化证明搜索解决开放问题（9/353 Erdős 问题、44/492 OEIS），已部署于组合/优化/代数几何/量子光学研究 ✅ `33-alphaproof-nexus-2605.22763.pdf`
- 持续跟踪：PutnamBench leaderboard、miniF2F 榜、AITP 会议（AI for Theorem Proving）、NeurIPS "AI for Math" workshop

> **文件对照**：`papers/NN-短名-arXiv号.pdf` 与上表编号一一对应；18、21 两篇 Nature 论文需按表内链接手动下载。
