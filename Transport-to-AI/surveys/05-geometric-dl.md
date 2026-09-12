# 几何深度学习综述：从埃尔朗根纲领到流形上的卷积

> 面向：研二几何分析方向、熟悉黎曼几何/流形上 PDE/调和映射/Ricci 流/极小曲面者
> 关键词：谱图理论、图拉普拉斯、等变性、Ollivier-Ricci 曲率、Heat kernel、Weisfeiler-Lehman 检验

---

## 1. 概述：几何深度学习是什么

几何深度学习 (Geometric Deep Learning, GDL) 把深度学习从欧氏网格数据推广到非欧结构（图、流形、点云、单纯复形）。Bronstein et al. (2017, arXiv:1611.08097) 首次提出该术语；其 2021 年统一框架 (arXiv:2104.13478) 借鉴 Klein 埃尔朗根纲领，把 CNN、GNN、Transformer、LSTM 统一在 **对称性与等变性** 之下：以群 $G$ 作用在域 $\Omega$ 上，网络层是 $G$-等变映射 $f(g\cdot x)=g\cdot f(x)$，卷积=群上互相关，消息传递=局部聚合模板的实例化。核心价值在于：把"归纳偏置"从工程经验提升为表示论的原理性约束，使不同架构成为同一几何原理的特例。

## 2. 已用的数学工具

- **谱图理论**：以图拉普拉斯 $L=D-A$ 的谱分解 $L=\sum_k\lambda_k\varphi_k\varphi_k^\top$ 为图上"傅里叶基"，卷积定义为 $g\star f=\Phi\,g_\theta(\Lambda)\,\Phi^\top f$。Cheeger 不等式 $\lambda_1/2\le h_G\le\sqrt{2\lambda_1}$ 把谱隙与瓶颈连通性挂钩。
- **流形上的卷积（Laplace-Beltrami 特征基）**：紧致黎曼流形 $\mathcal{M}$ 上以 $-\Delta_{\mathcal{M}}$ 特征函数 $\{\phi_k\}$ 为基，流形卷积=谱域滤波 $g(\Delta)$；球面/双曲面上以球面调和构造等变核。
- **等变性/不变性（群表示论）**：$SO(3)$ 表示分解为不可约表示 (irreps) $\ell=0,1,2,\dots$，球面调和 $Y_\ell^m$ 在 Wigner $D$-矩阵下变换；TFN (Thomas et al., 2018, arXiv:1802.08219)、SE(3)-Transformer 据此构造张量积卷积。
- **最优传输 (Monge-Ampère)**：GNN 重布线与图匹配用 OT 度量节点分布距离；Wasserstein 度量与 Ollivier-Ricci 曲率 $\kappa_{OR}(u,v)=1-W_1(\mu_u,\mu_v)/d(u,v)$ 直接关联。
- **离散曲率**：Forman 曲率、Ollivier-Ricci 曲率把光滑 Ricci 张量离散化到边上，刻画局部信息传输效率。
- **Heat kernel on graphs**：$H_t=e^{-tL}=\sum_k e^{-t\lambda_k}\varphi_k\varphi_k^\top$，多尺度扩散描述子，连接流形上热核估计与谱隙。

## 3. 已经做了什么：关键论文时间线

| 论文 | 工具 | 贡献 |
|---|---|---|
| Bruna et al. (2014) | 谱图 | 首个基于拉普拉斯谱的谱 GNN |
| Defferrard et al. (2016, ChebNet) | Chebyshev 多项式 | 把谱卷积局部化为 $K$-hop 多项式 |
| Kipf & Welling (2017, arXiv:1609.02907) | 一阶 Chebyshev | GCN，把谱方法简化为消息传递 |
| Veličković et al. (2018, arXiv:1710.10903) | 注意力 | GAT，聚合权重设为可学习注意力 |
| Thomas et al. (2018, arXiv:1802.08219) | 球面调和/irreps | TFN，首个 SE(3)-等变点云网络 |
| Xu et al. (2019, arXiv:1810.00826) | WL 检验 | GIN，证明消息传递 GNN 表达力 $\le 1$-WL |
| Bronstein et al. (2021, arXiv:2104.13478) | 埃尔朗根纲领 | 统一框架，GDL 的"圣经" |
| Satorras et al. (2021, arXiv:2102.09844) | 相对坐标 | EGNN，$E(n)$-等变且免去球谐的高效实现 |
| Topping et al. (2022, SDRF) | Ollivier-Ricci | 首次用离散曲率解释 over-squashing 并重布线 |
| Nguyen et al. (2023, arXiv:2211.15779) | Ollivier-Ricci | 证明 over-smoothing↔正曲率、over-squashing↔负曲率，提 BORF |

## 4. 达到了什么结果

- **表达力上界**：消息传递 GNN 的区分能力严格不超过 $1$-WL 检验 (Xu 2019; Morris 2019)，无法区分所有非同构图。$k$-WL/$k$-GNN 给出严格递增层级但代价 $O(n^k)$。
- **过平滑的谱刻画**：层数 $\to\infty$ 时节点特征趋于常数，等价于 Dirichlet 能量 $E(H,A)=\frac1N\sum_{u,v}a_{uv}\|h_u-h_v\|^2$ 指数衰减。Operator semigroup 视角 (arXiv:2402.15326) 证明过平滑本质是扩散算子的遍历性 (ergodicity)。
- **等变网络表达力**：连续域上通用等变网络可逼近任意等变连续函数，但离散实现受 irreps 截断与局部帧完备性约束。Du et al. (arXiv:2110.14811) 用局部完整正交帧构造高效 SE(3)-等变 GNN。
- **曲率-瓶颈定理**：负 Ollivier-Ricci 边对应信息瓶颈 (over-squashing)，正曲率边对应塌缩 (over-smoothing)，给出统一局部几何诊断 (arXiv:2211.15779)。

## 5. 局限性

1. **流形假设与实际数据的 gap**：理论分析默认数据采样自光滑紧致流形，但真实图（社交网、分子）常带噪声、悬空点、奇异结构；"图-流形"离散化误差几乎无人系统分析。
2. **离散化误差分析缺失**：图拉普拉斯 $L$ 收敛到 $\Delta_{\mathcal{M}}$ 的速率（$h^2$ 收敛、点云密度假设）在 GNN 文献中极少出现，多数只做图谱层面启发式论证。
3. **高曲率流形上的数值稳定性**：曲率重布线（SDRF/BORF）在高负曲率区域反复加边易退化；Ricci 流数值格式在离散图上无收敛性保证。
4. **GNN 表达力受限于 1-WL**：消息传递天然无法捕捉三角形/环等高阶结构；对 SAT 等问题证明 WL 层级整体不足 (arXiv:2602.08745)，谱位置编码能否突破仍存疑 (arXiv:2605.23446)。
5. **等变约束与优化的张力**：严格等变损失景观含伪极小、优化困难，大规模上反不如放松约束的网络 (arXiv:2605.27662)。

## 6. 怎么解决的：2024–2026 最新工作

- **统一过平滑/过压缩**：Arroyo et al. (2025, arXiv:2502.10818, Bronstein 团队) 把两者统一到 vanishing gradients，借线性控制论/state-space 模型同时缓解，揭示雅可比谱的主导作用。
- **曲率驱动重布线**：PIORF (arXiv:2504.04052) 把 Ollivier-Ricci 流与物理场耦合用于 mesh GNN；DeepRicci (arXiv:2401.12780) 提出反向 Ricci 流 + 可微曲率自监督精修结构；CurvGIB (arXiv:2412.19993) 把 Ricci 流与变分信息瓶颈融合，学任务相关最优传输结构。
- **拓扑+几何融合**：ETNN (ICLR 2025, arXiv:2405.15429) 在组合复形上做 $E(n)$-等变消息传递，几何不变量（距离、体积）作特征；Heat Kernel Goes Topological (arXiv:2507.12380) 用组合复形拉普拉斯的热核描述子避免高阶消息传递。
- **分数阶/非局部扩散**：Fractional Heat Kernel (arXiv:2510.04440) 用 $(-\Delta)^s$ 的分数热核增强小样本半监督 GNN 的多跳扩散。
- **重新审视基本问题**：Kormann et al. (2026, arXiv:2601.07419) 立场论文指出 over-smoothing/over-squashing 在实测中影响被高估，准确率与 Dirichlet 能量多不相关，呼吁转向"信息定位"统计量。

## 7. 对几何分析背景者的切入建议

四条路径最适合用几何分析工具切入，且与 CCF-A/B 主线对齐：

1. **离散 Ricci 流的收敛性与数值分析**（最直接）：现有 BORF/SDRF/PIORF/DeepRicci 把光滑 Ricci 流 $\partial_t g=-2\mathrm{Ric}$ 离散到图上，但**无收敛性证明、无与 Hamilton 短时间解的逼近定理**。几何分析者熟悉 Ricci 流的正则性、爆破分析与收敛条件，可严格刻画"图上 Ricci 流何时收敛到正曲率图"，给出重布线算法的停止准则与稳定性——这是当前文献的真空地带。

2. **调和映射能量作为 GNN 损失/正则**：GNN 过平滑等价于 Dirichlet 能量趋零；调和映射 $u:\mathcal{M}\to\mathcal{N}$ 的能量 $E(u)=\int|du|^2$ 正是其连续类比。可把"防过平滑"重述为"约束特征映射为非平凡调和映射"，用 $\alpha$-调和映射（含 $p$-Laplacian）给出能量下界，连接到热方程的 Li-Yau 估计。

3. **极小曲面/平均曲率流处理高维嵌入**：GNN 过压缩本质是远端信息被"压扁"。极小曲面方程 $\mathrm{H}=0$ 与平均曲率流提供"最小面积嵌入"的变分结构，可用来设计保证嵌入维度与瓶颈鲁棒性的位置编码。

4. **流形上热核估计驱动 GNN 设计**：几何分析有成熟的热核渐近 $K_t(x,y)\sim (4\pi t)^{-m/2}e^{-d^2/4t}(\theta_0+\cdots)$，而 GNN 文献仅用谱截断。可把 Li-Yau / Grigor'yan 热核界用于图拉普拉斯，给出比 Cheeger 不等式更细的传输界，统一刻画谱隙-曲率-瓶颈。

**推荐首个工作**：在 toy 图族（环、格点、双曲嵌入图）上严格证明离散 Ollivier-Ricci 流的收敛条件与收敛速率，并与连续 Ricci 流短时间解做逼近误差界。这是纯几何分析能直接产出、且填补 GDL 理论真空的结果，适合 NeurIPS/ICML workshop 起步，通往 ICLR/ICML 正会的理论主线。

---

## 关键 arXiv 速查

- 1611.08097 (Bronstein 2017, going beyond Euclidean data)
- 2104.13478 (Bronstein 2021, 统一框架)
- 1609.02907 (Kipf-Welling, GCN)
- 1710.10903 (Veličković et al., GAT)
- 1810.00826 (Xu et al., GIN / How powerful are GNNs)
- 1802.08219 (Thomas et al., TFN)
- 2102.09844 (Satorras et al., EGNN)
- 2110.14811 (Du et al., SE(3) local frames)
- 2211.15779 (Nguyen et al., Ollivier-Ricci over-smoothing/squashing)
- 2402.15326 (operator semigroup oversmoothing)
- 2502.10818 (Arroyo et al., vanishing gradients, Bronstein)
- 2404.04612 (spectral graph pruning)
- 2504.04052 (PIORF, Ollivier-Ricci flow for mesh)
- 2401.12780 (DeepRicci, backward Ricci flow)
- 2412.19993 (CurvGIB, Ricci flow + VIB)
- 2405.15429 (ETNN, E(n)-equivariant topological NN)
- 2507.12380 (heat kernel topological)
- 2510.04440 (fractional heat kernel)
- 2601.07419 (position: don't fear over-smoothing)
- 2602.08745 (GNNs for SAT, WL limits)
- 2605.23446 (WL incomplete on simple spectrum)
- 2605.27662 (optimizer shapes equivariant NN)
