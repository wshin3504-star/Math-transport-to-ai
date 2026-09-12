# 转码就业计划：从几何分析到 AI/Agent（修正版）

> 目标：12 个月内产出 1 篇 CCF-A 或 2 篇 CCF-B，同时拿到工业界实习 return offer
> 起点：985 基础数学系研二，几何分析方向，Python 0 基础（2026.09 起步）
> 优势：数学成熟度（流形/PDE/分析）、"懂真数学"本身是稀缺资产

---

## 一、赛道选择（不再绑死 Lean）

### 主线（冲 CCF-A/B）：AI for Math

不局限于形式化证明（Lean），扩展到所有"数学 + AI"交叉点：

| 方向 | 为什么我能做 | 算力需求 | CCF 期望 |
|---|---|---|---|
| **LLM 数学推理** | 设计/评测高难数学数据集，我能判断题目质量 | 低（API 调用为主） | CCF-B 可冲 |
| **定理证明 Agent** | Lean + 几何分析空白 = 护城河 | 低（API + 单卡） | CCF-A 有机会 |
| **数学推理 + RLVR** | 可验证奖励 + 数学题 = 我的交叉点 | 中（7B LoRA） | CCF-A 有机会 |
| **几何深度学习** | 流形上的扩散/最优传输，专业最对口 | 高（多卡） | CCF-B 可冲 |

### 兜底（保就业）：Agent 工程实习

实习目标是 return offer，同时用实验室算力冲论文。实习方向优先：
1. 大模型/Agent 研究实习（字节 Seed、阿里通义、上海实验室、智谱）
2. 量化私募（幻方/DeepSeek、九坤、明汨）——对纯数学背景对口度和薪资都更高

---

## 二、论文产出策略

### 不把 CCF-A 当唯一赌注

| 层次 | 目标 | 秋招认可度 | 把握度 |
|---|---|---|---|
| arXiv 预印本 + 开源代码 | 保底 | 认可 | 高 |
| Workshop（NeurIPS/ICLR AI for Math） | 体面 | 认可 | 中高 |
| CCF-B（EMNLP/COLING/NAACL） | 有竞争力 | 认可 | 中 |
| CCF-A（NeurIPS/ICML/ICLR 主会） | 冲刺 | 强加分 | 中低 |

### 具体选题池（按把握度排序）

1. **数学推理数据集/评测**：几何分析定理的 autoformalization 数据集 + prover benchmark（Mathlib 几何空白 = 直接贡献）
2. **Proof agent 的失败模式分析**：定理证明 agent 的 benchmark / 过程奖励分析
3. **数学推理 + RLVR**：在数学题上做 GRPO/PPO，设计新的奖励信号或课程学习策略
4. **几何深度学习理论**：流形上 attention 的几何性质分析（理论+实验）

---

## 三、12 个月时间线（修正版）

### Phase 0：地基（2026.09–10，进行中）
- [x] Python 环境 + Git 仓库
- [x] micrograd 全 7 SECTION 通关（2026.09.10–11）
- [x] Attention Is All You Need 精读（2026.09.11–12）
- [ ] nanoGPT 跟练
- [ ] 30 篇论文清单每天 1 篇
- [ ] Lean 4 安装 + Natural Number Game

### Phase 1：复现 + 差异化作品（2026.11–12）
- 复现一个 API 驱动的 theorem-proving agent
- 把几何分析入门定理形式化为 Lean（或建独立 repo）
- 投寒假/日常实习

### Phase 2：第一个研究产出（2027.01–04）
- 从选题池选 1–2 个方向深入
- 出 arXiv 预印本 + 开源
- 冲 workshop / CCF-B

### Phase 3：研究实习（2027.03–07）
- 带作品面上实习
- 用实验室算力冲 CCF-A（NeurIPS 2027 截稿 ~5 月）

### Phase 4：秋招（2027.07–11）
- 简历 = 985 数学 + return offer + 论文 + 开源项目

---

## 四、每日节奏

| 时间块 | 内容 | 时长 |
|---|---|---|
| 上午 | 论文精读（每天 1 篇） | 45 min |
| 下午 | 代码实战（nanoGPT → prover agent → 研究代码） | 90–120 min |
| 晚间 | 理论补课（DL/RL/Lean）或 python-basics 刷题 | 45 min |

---

## 五、资源

| 需要什么 | 解法 |
|---|---|
| GPU | AutoDL 租 4090（~2 元/时）；Kaggle 30h/周免费；OpenI 启智社区 |
| API | DeepSeek/Qwen API（百万 token 几块钱），年预算 2000–5000 元 |
| 导师 | 工业界实习 mentor；Lean Zulip 社区；EleutherAI Discord |
| 论文选题 | arXiv cs.AI/cs.CL/cs.LO 每日刷；PutnamBench/miniF2F 榜 |
