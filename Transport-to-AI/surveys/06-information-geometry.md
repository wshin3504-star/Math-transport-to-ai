# 表示学习的信息几何综述：从 Fisher 度量到扩散模型的隐几何

> 面向：研二几何分析方向、熟悉黎曼几何/度量张量/曲率/信息论基础者
> 关键词：Fisher 信息度量、自然梯度、α-联络、KL 散度、对比学习 alignment-uniformity、潜空间 pullback 度量、score-based 黎曼度量

---

## 1. 概述：信息几何能解决什么

信息几何（Amari, 2016）把概率分布族 $\{p_\theta\}$ 视作微分流形——*统计流形*——并在其上赋予由 Fisher 信息矩阵定义的黎曼度量 $g_{ij}(\theta)=\mathbb{E}_{p_\theta}[\partial_i\log p_\theta\,\partial_j\log p_\theta]$。这一视角把"参数空间"从平凡的 $\mathbb{R}^d$ 提升为带内蕴度量的流形，使优化、推断、表示比较都获得几何含义。

在深度学习中，信息几何回应三个核心问题：(i) **优化的"自然"几何**——为何普通梯度下降在参数空间中方向依赖坐标选取？自然梯度 $\tilde{\nabla}=F^{-1}\nabla$ 给出与参数化无关的最速下降方向（Amari, 1998）。(ii) **表示空间的结构**——编码器把数据压入低维潜空间 $\mathcal{Z}$，这空间的几何是什么？是否黎曼的？曲率意味着什么？(iii) **分布间距离的内蕴刻画**——KL 散度虽非度量，但在对偶平坦结构下扮演"发散量"角色，是对比学习、变分推断的天然几何量。

## 2. 已用的数学工具

- **Fisher 信息度量**：统计流形 $\mathcal{M}=\{p_\theta\}$ 上的黎曼度量，$g_{ij}=\mathbb{E}[\partial_i\log p\,\partial_j\log p]$。对指数族退化为 Hessian $\partial_i\partial_j \Phi(\theta)$，即 *Hessian 度量*。
- **自然梯度**：黎曼梯度 $F^{-1}\nabla L$，是 KL 散度意义下的最速下降方向；与坐标无关，渐近 Fisher 有效。
- **α-联络（Amari）**：单参数族仿射联络 $\nabla^{(\alpha)}$，满足 $\alpha\leftrightarrow -\alpha$ 对偶；$\alpha=+1$ 为 $e$-联络（指数族自然投影），$\alpha=-1$ 为 $m$-联络，$\alpha=0$ 退化为 Levi-Civita 联络。给出对偶平坦结构 $(g,\nabla^{(e)},\nabla^{(m)})$。
- **KL 散度作为发散量**：$D_{\rm KL}[p_\theta\|p_{\theta'}]$ 非对称、非负，在对偶平坦流形上分解为两个 Bregman 散度之差，是广义勾股定理的基础。
- **对比学习的 alignment-uniformity 框架**（Wang & Isola, 2020, arXiv:2005.10242）：在单位超球面 $\mathbb{S}^{d-1}$ 上，对比损失在负样本 $\to\infty$ 极限分解为 $\mathcal{L}_{\rm align}=\mathbb{E}_{(x,y)\sim p_{\rm pos}}\|f(x)-f(y)\|_2^\alpha$ 与 $\mathcal{L}_{\rm uniform}=\log\mathbb{E}_{x,y\sim p_{\rm data}}e^{-t\|f(x)-f(y)\|_2^2}$；后者等价于球面上对数势能，极小元为归一化面积测度 $\sigma_d$。
- **Pullback 度量**：对解码器 $g:\mathcal{Z}\to\mathcal{X}$，潜空间度量 $G(z)=J_g(z)^\top J_g(z)$，把欧氏度量从数据空间拉回到潜空间；为 VAE/GAN 潜空间提供黎曼结构。

## 3. 已经做了什么：关键论文

| 论文 | 工具 | 贡献 |
|---|---|---|
| Amari (1998), Neural Comp. 10(2):251–276 | 自然梯度 | 证明自然梯度 Fisher 有效，消除多层感知机的 plateau 现象 |
| Amari & Nagaoka (2000) | α-联络、对偶平坦 | 系统建立信息几何的联络结构 |
| Martens & Grosse (2015), ICML | K-FAC | Kronecker 分解近似 Fisher，使自然梯度可扩展到深度网络 |
| George et al. (2018), NeurIPS | EKFAC | 特征基 Kronecker 分解，进一步降低计算代价 |
| Wang & Isola (2020), arXiv:2005.10242 | alignment-uniformity | 对比损失几何分解，球面上均匀分布最优性严格证明 |
| Arvanitidis et al. (2018), ICLR | pullback + Riemannian | GAN 潜空间曲率分析，发现线性插值偏离测地线 |
| Arvanitidis et al. (2021), AISTATS | 几何富化潜空间 | 通过 Riemannian 度量改善潜空间插值与聚类 |
| Arvanitidis et al. (2024), arXiv:2106.05367 | Fisher-Rao pullback | 把解码器分布族视为 $\mathcal{H}$ 中流形，推广到非高斯解码器 |

## 4. 达到了什么结果

- **自然梯度的收敛性**：Amari 证明在线自然梯度学习是 Fisher 有效的——渐近协方差达到 Cramér-Rao 下界，等价于最优批估计。plateau 现象被归因于参数空间的"病态几何"，自然梯度消除之。K-FAC/EKFAC 使之在百万参数网络实际可用。
- **对比学习的几何刻画**：alignment-uniformity 框架把 InfoNCE 损失分解为超球面上的两个可优化标量，证明 $\sigma_d$ 为 uniformity 唯一极小元；直接优化二指标可达到或超越对比学习下游性能。把"表示质量"从模糊概念变为可测几何量。
- **潜空间的黎曼结构**：pullback 度量给出可计算的 $G(z)$，使测地线插值显著优于线性插值；测地线长度作为内蕴距离，解决潜空间"可辨识性"难题（不同训练得到的潜空间可通过等距变换对齐）。Fisher-Rao 拉回把适用范围从高斯解码器扩展到几乎任意分布族。

## 5. 局限性

1. **Fisher 矩阵计算代价**：$F\in\mathbb{R}^{d\times d}$，$d\sim10^7$–$10^{14}$，存储 $O(d^2)$、求逆 $O(d^3)$ 完全不可行。K-FAC 的 Kronecker 假设忽略层间耦合，在 Transformer 注意力层近似质量下降。
2. **理论与大模型的 gap**：信息几何假设模型族 $\{p_\theta\}$ 构成光滑流形，但过参数化网络的可辨识性、损失景观的非凸尖点、相变使统计流形可能 *奇异*（Fisher 矩阵退化），经典光滑假设失效。
3. **表示空间曲率意义不明**：潜空间 $G(z)$ 的截面曲率 $K(\sigma)$ 是 pullback 诱导的，与表示的"语义质量"无直接对应。曲率高表示插值弯曲，但是否对应泛化、鲁棒性、可辨识性缺乏理论桥梁。
4. **对比学习几何的局限**：alignment-uniformity 仅刻画超球面分布的渐近行为，忽略有限负样本、批内耦合；非球面（如 VI 能量表示）无对应框架。

## 6. 怎么解决的：2023–2026 最新工作

- **扩散模型的 score-based 黎曼度量**：Azeglio et al. (2025, arXiv:2505.11128) 与 Saito & Matsubara (2025, arXiv:2504.20288) 用 Stein score $s(x)=\nabla_x\log p(x)$ 直接在数据空间构造度量 $g(x)=I+\lambda s s^\top$——垂直于数据流形的距离被拉伸、切向被保持，测地线自然沿流形走，**绕过潜空间参数化**。Stable Diffusion 上插值显著优于 DDIM/slerp。
- **扩散模型的"时空"信息几何**：Karczewski et al. (2026, arXiv:2505.17517) 把去噪分布族 $\{p(x_t|x_0)\}$ 视为以 $(x_0,t)$ 为坐标的统计流形，Fisher-Rao 度量在 $(t,x_0)$ "时空"上定义；证明纯 pullback 几何会塌缩，引入 information geometry with denoising decoders 给出非平凡度量，提出 Diffusion Edit Distance。
- **潜空间 Hessian 几何与相变**：Lobashev et al. (2025, arXiv:2506.10632, ICML) 通过重构 log-partition 函数重建 Fisher 度量，在扩散模型潜空间发现 *分形相变结构*——Fisher 度量在相边界突变，Lipschitz 常数发散，揭示潜空间非光滑。
- **非参数潜流形的测地线微积分**：Hartwig et al. (2026, arXiv:2510.09468) 用投影算子隐式定义潜流形，发展离散测地线、指数映射的通用算法，不依赖特定自编码器族。
- **损失景观曲率的可测代理**：Dexter et al. (2024, arXiv:2401.12332, ICLR) 引入 Hessian 相干性度量刻画 SGD 线性稳定性；Merullo et al. (2025, arXiv:2510.24256) 用 K-FAC 谱分解把曲率与"记忆 vs 推理"对应——低曲率方向承载记忆、高曲率方向承载泛化，可定向剪枝抑制记忆。
- **几何感知 PEFT**：GRIT (2026, arXiv:2601.21626) 把 K-FAC 作为自然梯度代理注入 LoRA，周期性把低秩基重投影到 Fisher 主特征方向，参数量减约 46% 且不损性能；Liao et al. (2026, arXiv:2603.29108) 把 K-FAC 推广到双层优化的超梯度。
- **跨模型潜几何对齐**：Yu et al. (2025, arXiv:2506.01599) 假设不同模型参数化同一流形，用 pullback 度量构造 *相对测地线表示*，在视觉基础模型上实现 zero-shot 模型拼接。

## 7. 切入建议：黎曼几何/曲率工具何处最锋利

对几何分析背景者，三条路径最值得下注：

1. **潜空间的截面曲率与表示质量**：现有 pullback 度量 $G(z)=J^\top J$ 的截面曲率 $K$ 几乎未被理论刻画。可问：高 $K$ 的潜空间是否对应更鲁棒的表示？曲率发散是否对应相变/记忆崩溃？Lobashev (2025) 已在扩散模型发现 Fisher 度量在相边界突变——把这种发散与 Ricci 曲率、共轭点、测地线聚焦联系起来，是经典比较定理的直接应用。从 $G$ 的二阶导数 $\nabla_i\nabla_j G_{kl}$ 出发，可重做 Cartan-Hadamard 型判断。

2. **α-联络在表示学习中的角色**：信息几何的对偶平坦结构 $(g,\nabla^{(e)},\nabla^{(m)})$ 在表示学习中几乎未被利用。自然梯度只用 $g$，忽略了仿射联络。对深度网络的 *函数空间*（而非参数空间）流形，可定义 $\alpha$-联络族，研究 $\alpha$ 对优化轨迹、表示对齐的影响——尤其是 $e$-投影 vs $m$-投影在对比学习中的几何解释。这是把 Amari 的对偶几何真正引入表示学习的主线。

3. **扩散模型隐流形的曲率与采样动力学**：score-based 度量 $g=I+\lambda s s^\top$ 的曲率结构决定了测地线、并行移动（视频编辑应用）。可研究：曲率符号与数据流形拓扑（孔洞、瓶颈）的关系；热核估计 $\mathcal{M}$ 上的扩散过程与 PF-ODE 的对应；$\sigma\to0$ 极限度量的收敛阶——这直接对接你熟悉的 heat kernel 估计与 Weyl 定律。

**推荐首个工作**：选一个已知 ground-truth 流形的数据集（嵌入球、torus、Möbius 带），训练小型 VAE/扩散模型，计算 pullback/score 度量的截面曲率与 Ricci 标量，比对真实曲率。若能证明 *学到的度量的曲率符号/渐近阶与真流形一致*，就是 ICML/NeurIPS workshop 级结果，并通向表示学习几何的主线。

---

## 关键 arXiv 速查

- 2005.10242 (Wang-Isola 2020, alignment-uniformity)
- 2106.05367 (Arvanitidis 2024, pulling back information geometry / Fisher-Rao)
- 2407.11244 (Kim 2024, deep generative geodesics)
- 2401.12332 (Dexter 2024, SGD stability & loss surface geometry, ICLR)
- 2504.20288 (Saito-Matsubara 2025, score-based Riemannian metric for diffusion)
- 2505.11128 (Azeglio 2025, score-based metric to explore data manifold)
- 2505.17517 (Karczewski 2026, spacetime of diffusion models, info-geometry)
- 2506.01599 (Yu 2025, relative geodesic representations across models)
- 2506.10632 (Lobashev 2025, Hessian geometry of latent space, ICML)
- 2510.09468 (Hartwig 2026, geodesic calculus on implicit latent manifolds)
- 2510.24256 (Merullo 2025, memorization vs reasoning, K-FAC curvature spectrum)
- 2601.21626 (GRIT 2026, geometry-aware PEFT with K-FAC)
- 2603.29108 (Liao 2026, KFAC bilevel optimization hypergradients)
