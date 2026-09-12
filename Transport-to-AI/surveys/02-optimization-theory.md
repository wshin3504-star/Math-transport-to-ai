# 深度学习优化理论综述

> 面向读者：研二几何分析方向，熟悉 PDE、梯度流、ODE 长时间行为、凸优化基础。
> 本文聚焦"数学可处理"的那一支理论，刻意略过纯经验性内容。

---

## 1. 概述：为何重要且困难

深度学习优化的中心问题可一句话表述：在一个百万至十亿维、非凸、分段非光滑（ReLU、LayerNorm）的损失景观上，随机梯度下降（SGD）为何能在多项式迭代内找到泛化良好的解？困难有三：

- **非凸性**使经典凸优化工具失效，朴素分析只能保证收敛到一阶稳定点 $\nabla L=0$，无法区分鞍点与极小。
- **过参数化**让 Hessian 高度病态，sharp/flat 与泛化的关系至今无完整刻画（"edge of stability"现象，Cohen et al. arXiv:2107.06289）。
- **真实算法（Adam、momentum、warmup、batch 切换）**的随机性远超 i.i.d. 假设，连续时间极限不显然存在。

理论因此分叉为三大流派：NTK 派（线性化）、mean-field 派（Wasserstein 梯度流）、PL/几何条件派。三者各有"把非凸问题化归为已知可处理结构"的策略：NTK 化归为核回归，mean-field 化归为测度空间凸泛函，PL 化归为带几何结构的非凸优化。三条路径本质上都在用一套连续/极限语言绕开维度灾难，恰是 PDE 与梯度流分析的用武之地。

---

## 2. 已用的数学工具

- **梯度流作为 PDE**：连续时间极限 $\dot\theta_t=-\nabla L(\theta_t)$；当参数被测度化（每个神经元看成 $\mathbb{R}^d$ 上的粒子分布 $\mu_t$），训练成为 Wasserstein 空间 $(\mathcal P_2,W_2)$ 上的梯度流，对应连续性方程 $\partial_t\mu_t+\nabla\cdot(\mu_t v_t)=0$，其中速度场 $v_t=-\nabla \frac{\delta J}{\delta\mu}$；加入 SGD 噪声后变为 McKean-Vlasov 型 Fokker-Planck 方程。这正是 Ambrosio-Gigli-Savaré 风格的度量空间梯度流，与最优传输、能量不等式（EVI）、过渡解集天然相连——读者熟悉的整套弱几何分析语言可直接搬运。
- **NTK（Neural Tangent Kernel）**：无限宽极限下网络在训练中近似线性（参数几乎不动，即"lazy"），损失被定常核 $K_\infty$ 控制，问题退化为核岭回归，收敛率由 $K_\infty$ 的最小特征值 $\lambda_{\min}>0$ 主导。
- **Mean-field / Chizat-Bach CK 理论**：把两层网络参数看作 $\mathbb{R}^d$ 上测度 $\mu$，损失成为测度空间上的（一般非凸）泛函 $J(\mu)=R(\int\phi\,d\mu)+G(\mu)$，训练是 $W_2$ 梯度流；关键在于 $J$ 在测度空间上可写成凸泛函复合线性算子，从而绕开参数空间的非凸。
- **PL 条件**（Polyak-Łojasiewicz）：$\tfrac12\|\nabla L\|^2\ge\mu(L-L^\*)$，弱于凸但足以给线性收敛率；在过参数化网络中可被证明**局部**成立，是连接非凸实践与凸分析结论的桥梁。
- **Lipschitz / 光滑性**：网络输出关于参数的 Lipschitz 常数与 Hessian 范数控制是 over-parameterization 证明的定量钥匙，宽度 $m$ 需达到多少才能使这些量"足够小"是核心 trade-off。
- **动力系统理论**：LaSalle 不变性原理、$\omega$-极限集、线性化稳定性、不变流形与中心流形，用于隐式偏置与长时间行为刻画；Adam 的 loss spike 与退化方向收敛分析正回归到这套离散/连续动力系统局部稳定性语言。

---

## 3. 已经做了什么（关键论文时间线）

- **2018 NTK**：Jacot-Gabriel-Hongler, *Neural Tangent Kernel*（arXiv:1806.07566），证明无限宽网络训练被定常 NTK 控制。
- **2018 Mean-field**：Chizat-Bach, *On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport*（arXiv:1805.09545），把两层网络训练写成 $W_2$ 梯度流；Mei-Montanari-Nguyen, *A mean field view of the landscape of two-layer neural networks*（PNAS 2018），用非线性 PDE（distributional dynamics）描述 SGD。
- **2019 过参数化**：Du-Lee-Tian-Singh-Póczos, *Gradient Descent Finds Global Minima of Deep Neural Networks*（arXiv:1811.03804）；Du-Zhai, *On the Global Convergence of Training Deep ReLU Nets*（arXiv:1902.02984），证明足够过参数化下线性收敛到零损失。
- **2018-2019 Double descent**：Belkin-Hsu-Mitra, *Reconciling modern ML and the bias-variance trade-off*（arXiv:1812.11151）。
- **PL 系统化**：Karimi-Nutini-...-Schmidt, *On the Suboptimality of Gradient Descent for the PL Condition*（arXiv:1908.00467）。
- **ResNet 的 PDE/mean-field**：Ding-Chen-Li-Wright, *On the Global Convergence of GD for Multi-Layer ResNets in the Mean-Field Regime*（arXiv:2110.02926）——把 ResNet 训练翻译为梯度流 PDE，这是少数由数学系（UW-Madison）完成的工作，方法上最贴近读者背景。

---

## 4. 达到了什么结果

- **NTK regime 的全局收敛**：在 $m\to\infty$（$m$ 为宽度）极限下，训练动力学被线性核方程控制，损失以 $1-e^{-\lambda t}$ 速率下降到全局极小，$\lambda$ 由 $K_\infty$ 的最小特征值给出；泛化由核岭回归偏差-方差分析给出，且核极限与核岭回归严格等价（Mei-Misiakiewicz-Montanari, arXiv:1902.06015）。
- **过参数化下的线性收敛**：在 $m\gtrsim \text{poly}(n,1/\epsilon)$ 宽度下，有限步 GD 以 $1-\eta\lambda$ 速率达零训练损失（Du et al.）；宽度需求与样本数 $n$ 的多项式关系是 NTK 证明的代价。
- **mean-field 全局最优（渐近）**：在无限粒子极限 + 充分支撑初始化下，$W_2$ 梯度流收敛到 $J$ 的全局极小（Chizat-Bach）；Ding-Chen-Li-Wright 把 ResNet 的深度与宽度对精度/置信度的依赖压到代数级。
- **隐式正则化的刻画**：在过参数化线性网络/对角线性网络下，GD/SGD 隐式偏好最小 $\ell_2$/最稀疏解；带 label noise 的 SGD 在极小流形附近做布朗运动并最小化 Hessian 迹 $\mathrm{tr}(H)$（sharpness）。
- **PL 条件下的率**：在局部 PL + $L$-光滑下，GD 线性收敛 $L(\theta_t)-L^\*\le(1-\mu/L)^t(L(\theta_0)-L^\*)$；SGD 为 $\mathcal{O}(1/t)$；PL 把"非凸但够好"问题归约为已知率。

---

## 5. 局限性

- **NTK 假设不现实**：要求宽度 $m\to\infty$ 且参数几乎不动（lazy regime），与真实训练中"特征被学习、参数大幅漂移"矛盾；NTK regime 解释不了 feature learning，且核极限预测的泛化常显著弱于真实网络。
- **mean-field 的工程 gap**：收敛结论是渐近的（$N\to\infty$），定量收敛率长期缺失；且 Chizat-Bach 的全局收敛**假设**了流收敛（被广泛批评为非平凡假设，因动力学在无穷维空间，存在性/唯一性/收敛三者相互牵制）。
- **非全局收敛分析缺失**：现实深度网络不在 NTK/mean-field 严格 regime，是否能达全局极小无保证；鞍点逃逸、spurious 局部极小、loss spike 的定量刻画薄弱，多停留在现象学。
- **Adam 的理论远不如 SGD**：Adam 缺乏干净的连续时间极限，长期只有 AMSGrad 弱收敛，对隐式偏置、为何优于 SGD 几乎无解释——这正是 2024-2026 集中突破的痛点（见下节）。
- **离散化 gap**：mean-field PDE ↔ 真实 SGD 之间的粒子离散化、时间离散化、随机性误差定量控制仍弱；步长/噪声尺度进入常数的方式常常粗糙。

---

## 6. 怎么解决的：最新工作（2023-2026）

- **mean-field 的定量率**：Zhang-Huang, *Mean-Field Analysis of Two-Layer NN: Global Optimality with Linear Convergence Rates*（arXiv:2205.09860）用 log-Sobolev 不等式首次给出 mean-field 的线性收敛率；Takakura-Suzuki, *Mean-field Analysis ... from a Kernel Perspective*（arXiv:2403.14917）用两时间尺度极限把特征学习与核方法统一。
- **多层 mean-field 严格化**：Nguyen-Pham (2020) 给出多层网络 mean-field 极限的严格框架，填补了"两层→多层"的可处理性鸿沟。
- **Adam 的动力系统刻画（2025-2026，井喷）**：
  - Li-Wen-Lyu, *Adam Reduces a Unique Form of Sharpness*（arXiv:2511.02773）：用 SDE 证明 Adam 在极小流形附近最小化 $\mathrm{tr}(\mathrm{Diag}(H)^{1/2})$，与 SGD 的 $\mathrm{tr}(H)$ 严格分离。
  - Jin-Liang-Zou, *Why Adam Can Beat SGD: Second-Moment Normalization Yields Sharper Tails*（arXiv:2603.03099，2026）：用停时+鞅框架首次证明 Adam 高概率界 $\tilde O(1/\sqrt{\delta T})$ 优于 SGD 的 $\delta^{-1}$ 依赖。
  - SJTU 徐振宇组：*Adaptive Preconditioners Trigger Loss Spikes in Adam*（arXiv:2506.04805）与 *Towards Understanding Adam Convergence on Highly Degenerate Polynomials*（arXiv:2603.09581）——用动力系统局部稳定性 + 相图刻画 loss spike 与高阶退化方向上的局部线性收敛。
- **edge of stability 的刻画**：Cohen et al.（arXiv:2107.06289）及后续工作，把"训练自然发生在 sharpness 阈值 $2/\eta$ 边缘"作为现象学，催生一系列 sharpness-aware 分析。

---

## 7. 切入建议：PDE / 梯度流工具最对口的几个问题

1. **mean-field PDE 的长时间收敛"证明而非假设"**。Chizat-Bach 把"$W_2$ 梯度流收敛到全局极小"当作假设——这恰是 PDE 长时间行为的主场。用 Lyapunov 泛函 + LaSalle 不变性原理 + $\omega$-极限集刻画，去**证**而非**假设**收敛，并给出定量率（log-Sobolev、HWI、渐近稳定性）。这是几何分析人的强项，且 Zhang-Huang 已用 log-Sobolev 开了头，可推广到更一般激活/正则。
2. **多层网络 mean-field PDE 的严格长时间分析**。Nguyen-Pham 2020 框架只给出极限存在；长时间行为、收敛率、与两层的差异分析开放。读者熟悉的 propagation of chaos、紧性论证、唯一性正则性可切入。
3. **Adam 的连续时间极限与稳定性**。Adam 缺干净连续极限，2025-2026 的工作正用 SDE/局部动力系统补这块。读者擅长的 ODE 线性化稳定性、不变流形、Lyapunov 指数正好对口；SJTU 徐振宇组是国内典型，可作 collaborator 候选。
4. **离散化 gap 的定量 PDE 估计**。mean-field PDE ↔ SGD 的误差 = 粒子离散化 + 时间离散 + 噪声。数值 PDE（稳定性/相容性/收敛三件套）+ 鞅 + 混沌传播是天然工具组合，论文产出空间大。
5. **流形上/几何深度学习的优化**。数据或参数空间具流形结构时，Ricci 曲率下界 → log-Sobolev → 收敛率，是几何分析人最直接对口的赛道（PLAN.md 中"几何深度学习"选题）。

> 优先级建议：1、2 用纯数学工具直接产出（理论+实验双轨），把握度高；3 有现成国内合作组且方向正热；4、5 偏长期。建议从 (1) 起步：选一个具体激活（softplus/sigmoid，已有 Villani 函数结构，见 arXiv:2210.11452）作为玩具模型，用 PDE 长时间行为给出 Chizat-Bach 假设的首个证明。
