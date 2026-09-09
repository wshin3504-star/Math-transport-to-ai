# Transport to AI — 几何分析 → AI/Agent 转行学习仓库

985 基础数学系研二学生（几何分析方向），目标 2027 秋招 AI/Agent 算法岗。
主打方向：**LLM × 形式化数学 / 定理证明 Agent（Lean 4）**，次选 Agentic RL。

完整方案见《几何分析转AI_Agent就业方案.docx》。

## 目录结构

```
Transport_to_AI/
├── README.md              # 本文件：仓库说明 + 打卡规则
├── PROGRESS.md            # 每日打卡日志（核心文件）
├── papers/
│   ├── READING_LIST.md    # 30 篇精读论文清单（按周排序）
│   └── notes/             # 每篇论文的笔记，命名如 01-attention.md
├── karpathy/              # Karpathy "Neural Networks: Zero to Hero" 跟练
│   └── 01-micrograd/      # 第 1 课：手写反向传播
├── d2l/                   # 《动手学深度学习》笔记与代码
├── lean/                  # Lean 4 学习（NNG 截图、Mathematics in Lean 练习）
└── docs/                  # 环境安装指引等
```

## 每日节奏（Phase 0，约 3.5 小时）

| 模块 | 时长 | 内容 |
|---|---|---|
| 代码 | 90 min | Karpathy 跟练（主线，必做） |
| 论文 | 45 min | 按 READING_LIST 每天 1 篇，写笔记进 papers/notes/ |
| 理论 | 45 min | 《动手学深度学习》对应章节 + Transformer/RL 基础 |
| Lean | 30 min | Natural Number Game → Mathematics in Lean |

## 打卡规则（从第一天起执行）

1. 每天学习结束时，在本仓库 `git commit` 一次，message 格式：

   ```
   study: day<N> <模块> <内容摘要>
   例：study: day1 micrograd Value类+手推反向传播; paper#1 attention
   ```

2. 同步在 `PROGRESS.md` 末尾追加一行日志。
3. 断卡不断更：哪怕只学了 30 分钟，也要 commit——**保连续性，不求完美**。

## 里程碑（Phase 0 出口标准）

- [ ] Karpathy 全部课程跟完，micrograd / makemore / nanoGPT 代码全部自己敲一遍并跑通
- [ ] 30 篇论文笔记齐全，能对每篇 5 分钟讲清「问题—方法—贡献」
- [ ] Lean 完成 Natural Number Game + Mathematics in Lean 前几章
- [ ] PyTorch 能独立写训练循环（d2l 配套）
