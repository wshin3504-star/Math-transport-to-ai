# 扩散模型 / Score-based 模型的数学理论综述

> 面向几何分析背景读者的综述。目标：识别可切入 CCF-A/B 论文的开放问题。
> 涉及工具：SDE、Fokker-Planck、反向 SDE、score function、最优传输、Wasserstein 距离、Girsanov 定理、流形上的热核。

---

## 1. 概述：扩散模型是什么，为什么需要数学理论

扩散模型（Diffusion Models）/ Score-based Generative Models (SGMs) 是当前最强的生成模型之一。其核心是两个随机过程：

- **正向过程**：用 SDE 把数据分布 $p_{\text{data}}$ 逐步加噪到已知先验（通常是高斯）。
- **反向过程**：用 reverse-time SDE 从噪声出发逐步去噪，恢复数据分布。

关键事实（Anderson 1982 的 reverse-time diffusion theorem）：正向 SDE
$$dX_t = f(X_t,t)\,dt + g(t)\,dW_t$$
对应的反向 SDE 为
$$dY_t = \bigl[-f(Y_t,t) + g(t)^2 \nabla_y \log q_{T-t}(Y_t)\bigr]\,dt + g(t)\,d\bar W_t,$$
其中 $q_t$ 是正向过程边际分布，$\nabla \log q_t$ 称为 **score function**。因此只要能估计 score，就能采样。Score 通过 denoising score matching 用神经网络学习。

**为什么需要理论**：实践中扩散模型效果惊人（图像/视频/蛋白质生成），但其成功依赖三件事——(1) score 估计是否准；(2) 离散化反向 SDE 的误差是否可控；(3) 正向过程终时 $T$ 的分布是否接近高斯。这三者的误差如何传播到最终采样分布的距离（KL/Wasserstein/TV），是数学理论的核心问题。直接关系到"为什么扩散模型 work"、"需要多少步采样"、"何时会失效"。

---

## 2. 已用的数学工具及出处

| 数学工具 | 作用 | 代表论文 |
|---|---|---|
| SDE / 反向 SDE (Anderson reverse-time) | 正向加噪 + 反向去噪的核心框架 | Song et al. 2021 (arXiv:2011.13456) |
| Fokker-Planck 方程 | 刻画正向边际密度演化，联系 score 与密度 | De Bortoli et al. 2021 (Schrödinger Bridge, NeurIPS 2021) |
| Score function $\nabla\log p_t$ + Denoising score matching | 训练目标，避免归一化常数 | Song & Ermon 2019; Vincent 2011 |
| Girsanov 定理 | 在路径空间上度量真实反向测度与近似反向测度的 KL 距离 | Chen et al. 2023 (arXiv:2209.11215); Benton et al. 2024 (arXiv:2308.03686) |
| Wasserstein 距离 / KL 散度 | 衡量生成分布与真实分布误差 | 几乎所有收敛性结果 |
| Entropic 最优传输 / Schrödinger Bridge | 给出前向-反向之间的桥接与收敛 | De Bortoli et al. 2021 (NeurIPS 2021) |
| Stochastic localization (Eldan) | 给出 d-线性的收敛界，等价于扩散模型 | Benton et al. 2024 (ICLR 2024) |
| 流形上的热核 / Bochner 技巧 / Li-Yau 估计 | Riemannian 扩散的收敛分析 | De Bortoli et al. 2022 (arXiv:2202.02763); Xu et al. 2026 (arXiv:2601.02499) |
| 高斯过程极值理论 | 流形假设下 score 的高概率界 | Azangulov et al. 2024 (arXiv:2409.18804) |
| Malliavin calculus | 条件化扩散 / 隐变量采样 | Pidstrigach et al. 2025 (arXiv:2504.03461) |
| 无穷维 SDE (Hilbert 空间) | 函数空间扩散模型 | Pidstrigach, Marzouk, Reich, Wang 2024 (JMLR) |

---

## 3. 已经做了什么（关键论文时间线）

1. **Song et al. 2021** (arXiv:2011.13456, ICLR Outstanding Paper)：提出统一 SDE 框架，用连续时间 SDE 统一 DDPM (Ho et al. 2020) 与 NCSN (Song & Ermon 2019)，给出 predictor-corrector 采样与 probability flow ODE。理论部分用 Anderson 反向公式，未给非渐近收敛界。

2. **De Bortoli, Thornton, Heng, Doucet 2021** (NeurIPS 2021)：用 Schrödinger Bridge 给出扩散模型与 entropic OT 的联系，首 个在有限步下指数级（$e^{-cT}$）收敛证明，但要求 score 是 $L^\infty$-accurate。

3. **De Bortoli 2022** (arXiv:2208.05314, TMLR)：首个在 **manifold hypothesis** 下的收敛结果——数据集中在低维子流形上。用 $L^\infty$ score 误差，得到 Wasserstein 误差界，但步长须指数小。

4. **Pidstrigach 2022** (NeurIPS 2022)：证明"Score-based 模型会自动检测流形"——score 在小噪声时指向流形方向，为 manifold convergence 提供机制解释。

5. **Chen, Chewi, Li, Li, Salim, Zhang 2023** (arXiv:2209.11215, ICLR 2023)：里程碑式工作。在**仅假设 $L^2$-accurate score + 二阶矩有界**下，对任意（多峰）分布给出多项式收敛界，复杂度 $\tilde O(d^2 \varepsilon^{-2} \log(1/\delta))$（$d$ 维，$\delta$ early-stopping）。用 Girsanov 定理在路径测度上控制 KL。是后续所有工作出发点。

6. **Chen, Lee, Lu 2023** (arXiv:2211.01916, ICML 2023)：在最小光滑性假设下给出 user-friendly 改进界。

7. **Benton, De Bortoli, Doucet, Deligiannidis 2024** (arXiv:2308.03686, ICLR 2024)：**首个 d-线性**（对数因子内）收敛界。定理（简化）：设数据有有限二阶矩，early-stopping at $\delta$，score $L^2$ 误差 $\le \varepsilon_{\text{score}}$，则只需
$$N = \tilde O\!\Bigl(\frac{d\,\log^2(1/\delta)}{\varepsilon^2}\Bigr)$$
步即可在 KL 内逼近到 $\varepsilon^2$。关键技术是 stochastic localization 的微分不等式。

8. **Azangulov, Deligiannidis, Rousseau 2024** (arXiv:2409.18804)：流形假设下证明 score 学习速率与 ambient 维度无关，采样复杂度在 KL 中与 ambient 维 $D$ 无关、Wasserstein 中为 $O(\sqrt D)$。用高斯过程极值理论。

9. **Potaptchik, Azangulov, Deligiannidis 2024** (arXiv:2410.09046)：证明流形假设下采样步数对**内在维 $d$** 是线性的，且该界 sharp。

10. **Xu, Zhang, Nakahira, Qu, Chi 2026** (arXiv:2601.02499)：Riemannian 扩散模型的首个**多项式收敛**结果。用 Li-Yau 估计 + Minakshisundaram-Pleijel 热核渐近，在 $L^2$ score 下得到 TV 距离界，不要求分布光滑或严格正。

---

## 4. 达到了什么结果（定理级摘要）

- **Euclidean，一般分布**（Chen 2023 / Benton 2024）：在 $L^2$ score 误差 + 二阶矩有界下，DDPM/SGM 的采样复杂度为 $\tilde O(d\,\varepsilon^{-2})$（Benton 2024 的 d-线性），在 KL 中达到 $\varepsilon^2$ 误差。该界与 Langevin diffusion 的最优离散化复杂度匹配（在 score 充分准时）。具体地，Benton 2024 主定理（简化表述）：

  > **Theorem (Benton et al. 2024)**：设 $p_{\text{data}}$ 在 $\mathbb R^d$ 上有有限二阶矩，score 估计 $\hat s$ 满足 $\int_0^T \mathbb E\|\hat s_t - \nabla\log q_t\|^2 dt \le \varepsilon_{\text{score}}^2$，则在 early-stopping 时间 $\delta$ 处，离散反向 SDE 经 $N$ 步后输出分布 $\hat p$ 满足
  > $$\mathrm{KL}(p_{\text{data}} * \mathcal N(0,\delta I)\,\|\,\hat p) \le \underbrace{C_1\, d\, N^{-2}\log^2(1/\delta)}_{\text{离散化误差}} + \underbrace{C_2\,\varepsilon_{\text{score}}^2}_{\text{score 误差}} + \underbrace{C_3\, e^{-2T}}_{\text{前向收敛残余}}.$$
  > 取 $N = \tilde O(d\,\varepsilon^{-2}\log^2(1/\delta))$ 即可使总误差 $\le \varepsilon^2$。

- **流形假设下**（Azangulov 2024 / Potaptchik 2024）：若数据支撑在 $d$-维 $C^2$ 紧子流形 $M\subset\mathbb R^D$ 上，则采样步数线性于内在维 $d$（对数因子内），与 ambient 维 $D$ 无关（KL 散度下），且该界 tight。

- **Riemannian 扩散**（Xu 2026）：在紧 Riemannian 流形上，$L^2$ score + 曲率假设下，反向 SDE 离散化的 TV 误差有多项式界，步长只须多项式小（此前 De Bortoli 2022 需指数小步长）。

- **Minimax 最优性**（Oko et al. 2023, arXiv:2301.06384）：在某些 Sobolev 类下，扩散模型在 density estimation 上达到 minimax 速率。

- **概率流 ODE**（Chen, Chewi, Lee, Li, Lu, Salim 2023, NeurIPS 2023）：probability flow ODE 也有 $\tilde O(d)$ 级复杂度，证明确定性采样器不慢于随机采样器。

---

## 5. 有什么局限性（理论 gap）

1. **score 近似误差的传播尚无 tight bound**：现有结果都假设 score 误差 $\varepsilon_{\text{score}}$ 作为 $L^2$ 上界给定，但神经网络训练后实际 score 误差如何随数据复杂度、网络容量、样本数变化，尚无紧界。Chen 2023 自承"Theorem 6 的 $L^\infty$ 界远非 tight"。

2. **流形假设下理论仍不完整**：
   - De Bortoli 2022 需分布严格正且光滑；Azangulov 2024 对 Wasserstein 仍有 $\sqrt D$ 残余。
   - 当流形有边界、非紧、曲率无界时无结果。
   - 流形的 reach（条件数）对界的依赖尚未精确刻画。

3. **非各向同性扩散分析缺失**：现有多数结果用 OU 过程（各向同性加噪）。实践中 variance-exploding / variance-preserving / 非 isotropic noise 的相对优劣，缺乏理论区分（Yang et al. NeurIPS 2024 才首次对 VE 给出多项式界）。

4. **early-stopping 的不精确性**：所有界都引入 $\delta$-early-stopping（不采样到 $t=0$），最终还需"denoising step"恢复，该步的误差在低维流形上因 score 在 $\delta\to 0$ 时 blow-up（量级 $\sim 1/\sqrt\delta$ 沿法向）而难控。Conforti, Durmus, Silveri (arXiv:2308.12240) 证明有限 Fisher 信息可免 early-stopping，但仅限特定类。

5. **条件生成 / classifier-free guidance 理论薄弱**：guidance 的作用机制（Bradley & Nakkiran 2024 才给出最简设置的分析）缺乏一般理论。

6. **Riemannian 情形只对紧流形**：非紧、带边界、以及热核无显式的流形（一般情况）上无法训练。PINN 近似（Ko & Lee 2026, arXiv:2605.31106）刚起步。

---

## 6. 局限性正在被谁解决（2024–2026 前沿）

- **score 紧界 / 流形检测**：Pidstrigach (Oxford) 系列工作——"Score-Based Models Detect Manifolds"(NeurIPS 2022) 与 log-domain smoothing 几何自适应性（Farghly, Potaptchik, Pidstrigach 2025, arXiv:2510.02305），把 score 与流形几何显式联系。

- **流形收敛**：Azangulov–Deligiannidis–Rousseau (Oxford/Dauphine, 2024) 用高斯过程极值理论；Potaptchik–Azangulov–Deligiannidis (2024) 把界降到内在维线性。Oxford 统计组（Deligiannidis, Doucet, Benton）是目前流形收敛最活跃力量。

- **Riemannian 多项式收敛**：Xu, Zhang, Nakahira, Qu, Chi (CMU/Yale, 2026, arXiv:2601.02499) 用 Li-Yau 与热核 parametrix 突破；Ko & Lee (KAIST, 2026) 用 PINN 处理一般流形。

- **无穷维扩散**：Pidstrigach, Marzouk, Reich, Wang (JMLR 2024) 建立 Hilbert 空间扩散理论；Rowbottom 等 (2026, arXiv:2605.03497) 用 FEM 处理不规则区域。

- **非各向同性 / VE 模型**：Yang, Wang, Jiang, Li (NeurIPS 2024) 对 VE-SDE 给出首个多项式界，设计 drifted VE 让前向收敛达 $e^{-T}$。

- **Malliavin 视角的条件化**：Pidstrigach, Baker, Domingo-Enrich, Deligiannidis, Nüsken (2025, arXiv:2504.03461) 用 Malliavin calculus 统一处理 diffusion conditioning。

- **最优传输视角**：Cheng, Lu, Tan, Xie (arXiv:2310.17582) 用 Wasserstein 空间的 proximal gradient descent 分析 flow-based 模型。

---

## 7. 对几何分析背景的人的切入建议

你的流形/PDE/SDE/泛函分析训练，正好对应本方向**最稀缺的技能组合**。CCF-A/B 可切入的具体问题：

**(A) Riemannian 扩散的收敛与几何依赖（强推荐）**
现状只对紧流形 + 曲率假设有多项式界（Xu 2026）。开放问题：
- 当 Ricci 曲率有下界但非紧时（Li-Yau 已给你工具），能否得到收敛界？
- 收敛常数对 reach、injectivity radius、第二基本型的显式依赖？这本质是几何分析问题。
- 带边流形、cone singularities 上的热核行为——你熟悉流形上 PDE，直接对口。

切入文献：精读 Xu et al. 2026 (arXiv:2601.02499) + De Bortoli et al. 2022 (arXiv:2202.02763)。这是 CCF-A 候选（NeurIPS/ICML 主会接受纯理论工作）。

**(B) Score 在流形近邻的渐近行为（理论 + 实验）**
Pidstrigach 2022 证明 score 指向流形。开放：score 在 reach 邻域内的 blow-up rate 与法丛几何的关系？这联系到你熟悉的 tubular neighborhood / Weyl tube formula（Farghly et al. 2025 已用到）。可以写一篇"score 的管邻域渐近 + 收敛改进"。

**(C) 非各向同性 / 流形自适应前向过程设计**
现有理论默认 OU 过程。能否设计"沿流形切丛的前向扩散"使其复杂度显式依赖 $d$ 而非 $D$？这需要 Riemannian 几何 + SDE。Yang et al. NeurIPS 2024 的 drifted VE 是欧氏版，流形版完全空白。

**(D) 无穷维 / 函数空间扩散的收敛理论**
Pidstrigach–Marzouk 2024 (JMLR) 给了无穷维框架但收敛界粗糙。若你有 Hilbert 空间 Sobolev 嵌入 / 紧算子背景，可给紧收敛界，用于 PDE 反问题的生成模型——这是科学计算 + AI 交叉点，CCF-B 易中。

**最低门槛切入**：先复现 Benton 2024 的 Girsanov 证明骨架（约 20 页，纯 SDE + 测度论），再选 (A) 或 (B)。你的几何分析成熟度足以在 6 个月内产出一篇有定理的 workshop paper，12 个月冲 CCF-B 主会现实可行。理论 + 少量实验（synthetic manifold）即可投稿，算力门槛低。
