# -*- coding: utf-8 -*-
"""
Day 1–4 任务卡：跟练 Karpathy《The spelled-out intro to neural networks and
backpropagation: building micrograd》（YouTube/B站 搜 "karpathy micrograd"，约 2.5h）

规则（重要）：
1. 先看视频对应段落，然后**关掉视频自己敲**，不看源码——你的数学直觉是优势，
   但代码手感只能靠敲出来。
2. 每个 SECTION 是一个检查点：通过底部对应的 check_xxx() 才能进入下一节。
3. 每天 90 分钟：Day1 完成 SECTION 1–2，Day2 完成 SECTION 3–4，
   Day3 完成 SECTION 5–6，Day4 完成 SECTION 7 + 总复习。
4. 全部通过后，与官方仓库对比差异：github.com/karpathy/micrograd
   （对照是为了理解，不是为了搬运）。

数学视角提示：
- backward() 本质是「计算图上的 Jacobian-vetor 积」的逆序应用——
  你学的链式法则在流形/切空间的语言下就是这件事，试着在 notes 里写下对应关系。
- tanh 的梯度 ((1-t^2)) 是为什么激活函数要可微且导数不消失的直观案例。

运行自检：
    .venv\Scripts\python karpathy\01-micrograd\micrograd_starter.py
"""

import math


# ═══════════════════════════════════════════════════════════════
# SECTION 1：Value 类 —— 标量自动微分的基本单元
# 视频 0:00–1:00:00 段落
# ═══════════════════════════════════════════════════════════════

class Value:
    """存储一个标量值及其计算图信息。"""

    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0          # d(output)/d(self)，反向传播时填
        self._backward = lambda: None   # 该节点如何把梯度传给 children
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad}, label='{self.label}')"

    # TODO 1.1 __add__：构造新 Value，记录 children=(self, other) 和 op='+'
    #   提示：返回 Value(self.data + other.data, (self, other), '+')
    def __add__(self, other):
        pass  # ← 替换这行

    # TODO 1.2 __mul__：同理，op='*'
    def __mul__(self, other):
        pass  # ← 替换这行

    # TODO 1.3 __neg__、__sub__（用 __add__ 和 __neg__ 组合）
    def __neg__(self):
        pass  # ← 替换这行

    def __sub__(self, other):
        pass  # ← 替换这行


def check_section1():
    a = Value(2.0, label='a')
    b = Value(-3.0, label='b')
    c = Value(10.0, label='c')
    e = a * b; e.label = 'e'
    d = e + c; d.label = 'd'
    assert abs(d.data - 4.0) < 1e-9, "d 应为 2*(-3)+10 = 4"
    assert d._prev == {e, c}, "d 的 children 应包含 e 和 c"
    assert d._op == '+'
    f = d - 1.0
    assert abs(f.data - 3.0) < 1e-9, "__sub__ 应可用"
    print("[OK] Section 1: Value 类基础运算通过")


# ═══════════════════════════════════════════════════════════════
# SECTION 2：手动反向传播 —— 理解 _backward 闭包
# 视频 1:00:00–1:20:00 段落（先手动，再抽象）
# ═══════════════════════════════════════════════════════════════

def manual_backprop_demo():
    """
    构造 L = (a*b + c) * f，手动推导并填 grad。
    数学上：dL/da = b * f（乘积法则 + 链式法则）。
    返回 (L, a, b, c, f)，并断言各梯度正确。
    """
    a = Value(2.0, label='a')
    b = Value(-3.0, label='b')
    c = Value(10.0, label='c')
    f = Value(-2.0, label='f')

    # TODO 2.1 逐步构造 d = a*b + c，L = d * f
    d = None  # ← 替换：d = a*b + c
    L = None  # ← 替换：L = d * f

    # TODO 2.2 手动填梯度（直接赋值 .grad）：
    #   dL/dL = 1; dL/df = d; dL/dd = f;
    #   dL/dc = f; dL/de = f; dL/da = ?; dL/db = ?
    # 把每个节点的 .grad 填上（用数值：上面例子的具体值）。
    # 注意 a.grad 与 b.grad 要用「乘积法则」：先算 dL/de，再乘 de/da = b。
    raise NotImplementedError("SECTION 2：完成上面 TODO 后删掉这行")

    # 断言（填完后取消注释）：
    # assert abs(a.grad - (-2.0 * -3.0)) < 1e-9, "dL/da 应为 f*b"
    # assert abs(b.grad - (-2.0 * 2.0)) < 1e-9, "dL/db 应为 f*a"
    # assert abs(c.grad - (-2.0)) < 1e-9
    # return L, a, b, c, f


# ═══════════════════════════════════════════════════════════════
# SECTION 3：自动反向传播 —— 把手动步骤写进 Value
# 视频 1:20:00–1:45:00 段落
# ═══════════════════════════════════════════════════════════════

def _install_add_backward(self, other, out):
    """TODO 3.1：为 + 定义 out._backward 闭包。
    规则：每个输入的梯度 += 输出的梯度（加号是恒等路由，注意是 += 不是 =）。"""
    pass  # out._backward = lambda: ...


def _install_mul_backward(self, other, out):
    """TODO 3.2：为 * 定义 out._backward。
    规则：self.grad += other.data * out.grad; other.grad += self.data * out.grad"""
    pass


# 在 SECTION 5 你会回来扩展 __add__/__mul__ 调用上面两个函数，
# 但现在先把逻辑直接写进 __add__/__mul__（与视频一致）：
#   __add__ 里：out._backward = lambda: (self.grad += out.grad, other.grad += out.grad)
#   __mul__ 里：out._backward = lambda: (self.grad += other.data*out.grad,
#                                        other.grad += self.data*out.grad)

def backward(self):
    """TODO 3.3：完整反向传播。
    步骤：
      1) self.grad = 1.0
      2) 拓扑排序：DFS 后序收集所有节点到 topo 列表
      3) 逆序遍历 topo，逐节点调用 node._backward()
    """
    # topological order
    topo = []
    visited = set()
    # TODO: 写一个 build_topo(v) 递归函数
    raise NotImplementedError("SECTION 3：完成拓扑排序 + 逆序 _backward 调用")


Value.backward = backward


def check_section3():
    a = Value(2.0, label='a')
    b = Value(-3.0, label='b')
    c = Value(10.0, label='c')
    f = Value(-2.0, label='f')
    L = (a * b + c) * f
    L.backward()
    assert abs(a.grad - 6.0) < 1e-9, f"dL/da 应为 6（=f*b），实际 {a.grad}"
    assert abs(b.grad - (-4.0)) < 1e-9, f"dL/db 应为 -4（=f*a），实际 {b.grad}"
    assert abs(c.grad - (-2.0)) < 1e-9
    assert abs(f.grad - 4.0) < 1e-9
    print("[OK] Section 3: 自动反向传播通过")


# ═══════════════════════════════════════════════════════════════
# SECTION 4：tanh —— 单个复合算子
# 视频 1:45:00–2:05:00 段落
# ═══════════════════════════════════════════════════════════════

# TODO 4.1 给 Value 添加 tanh 方法：
#   前向：out = Value(math.tanh(self.data), (self,), 'tanh')
#   反向：self.grad += (1 - out.data**2) * out.grad
# 提示：局部导数 (1 - t^2) 用 out.data 而不是重新算 tanh。
def tanh(self):
    pass  # ← 替换这行

Value.tanh = tanh


def check_section4():
    x1 = Value(0.5, label='x1'); w1 = Value(-1.5, label='w1')
    x2 = Value(1.0, label='x2'); w2 = Value(2.0, label='w2')
    b = Value(6.881, label='b')
    n = (x1 * w1 + x2 * w2 + b)
    o = n.tanh(); o.label = 'o'
    o.backward()
    # 数值梯度校验：f(x) = tanh(0.5*-1.5 + 1*2 + 6.881)，df/dx2 ≈ (1-tanh^2)*1*2
    h = 1e-6
    num = (math.tanh(x1.data*w1.data + x2.data*w2.data + b.data + w2.data*h)
           - math.tanh(x1.data*w1.data + x2.data*w2.data + b.data)) / h
    assert abs(w2.grad - num) < 1e-4, f"w2.grad={w2.grad} vs 数值 {num}"
    print("[OK] Section 4: tanh + 数值梯度校验通过")


# ═══════════════════════════════════════════════════════════════
# SECTION 5：exp / pow / div —— 把算子拆到原子级
# 视频 2:05:00–2:15:00 段落
# ═══════════════════════════════════════════════════════════════

# TODO 5.1 __pow__（只支持整数/浮点指数 n：self**other）：
#   前向：out = Value(self.data**other, (self,), f'**{other}')
#   反向：self.grad += other * self.data**(other-1) * out.grad
# TODO 5.2 exp：反向 self.grad += out.data * out.grad
# TODO 5.3 __truediv__：a / b = a * b**-1
# TODO 5.4 用 __truediv__ + exp 重写 tanh：t = (e^{2x}-1)/(e^{2x}+1)
#   验证两种实现梯度一致。
def __pow__(self, other):
    pass  # ← 替换

def exp(self):
    pass  # ← 替换

Value.__pow__ = __pow__
Value.exp = exp


def check_section5():
    x = Value(0.8)
    t1 = x.tanh()
    t2 = ((x * 2).exp() - 1) / ((x * 2).exp() + 1)   # 依赖 __truediv__/__neg__
    assert abs(t1.data - t2.data) < 1e-9, "两种 tanh 实现前向应一致"
    t2.backward()
    assert abs(t1.grad - 0.0) < 1e-9 and abs(t2.grad - (1 - t1.data**2)) < 1e-6, \
        "tanh 导数 = 1 - tanh^2"
    print("[OK] Section 5: exp/pow/div 原子算子通过")


# ═══════════════════════════════════════════════════════════════
# SECTION 6：Neuron / Layer / MLP
# 视频 2:15:00–2:30:00 段落
# ═══════════════════════════════════════════════════════════════

import random
random.seed(42)


class Module:
    """TODO 6.1：仿 torch.nn.Module：zero_grad() 和 parameters() 接口。"""
    def parameters(self):
        return []

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0.0


class Neuron(Module):
    # TODO 6.2：__init__(nin, nonlin=True)：w 为 nin 个 Value(random.uniform(-1,1))，
    #   b 为一个 Value(0)；__call__(x) 返回 sum(wi*xi) + b，nonlin 时过 tanh。
    pass


class Layer(Module):
    # TODO 6.3：neurons = [Neuron(nin) for _ in range(nout)]
    pass


class MLP(Module):
    # TODO 6.4：sizes 形如 [3, 4, 4, 1]，逐层建 Layer
    pass


def check_section6():
    mlp = MLP(3, [4, 4, 1])
    xs = [[2.0, 3.0, -1.0], [3.0, -1.0, 0.5], [0.5, 1.0, 1.0], [1.0, 1.0, -1.0]]
    out = [mlp(x) for x in xs]
    assert len(out) == 4 and len(mlp.parameters()) == (3*4+4) + (4*4+4) + (4*1+1), \
        "参数量应为 (3*4+4)+(4*4+4)+(4*1+1)"
    print("[OK] Section 6: MLP 前向通过")


# ═══════════════════════════════════════════════════════════════
# SECTION 7：训练循环 —— MSE loss + 手写梯度下降
# 视频 2:30:00–结尾 段落
# ═══════════════════════════════════════════════════════════════

def train():
    mlp = MLP(3, [4, 4, 1])
    xs = [[2.0, 3.0, -1.0], [3.0, -1.0, 0.5], [0.5, 1.0, 1.0], [1.0, 1.0, -1.0]]
    ys = [1.0, -1.0, -1.0, 1.0]

    # TODO 7.1 循环 50 个 epoch：
    #   1) 前向得到 ypred，loss = sum((yout - ygt)**2 for ...)（平方损失）
    #   2) zero_grad() -> loss.backward()
    #   3) 对每个参数 p.data -= 0.05 * p.grad
    #   4) 每 10 步 print loss
    # 目标：loss 降到 0.01 以下，且 4 个样本预测符号与 ys 一致。
    raise NotImplementedError("SECTION 7：完成训练循环")

    # TODO 7.2（选做）：把 nonlin=True/False、lr、层数改一改，观察收敛速度变化，
    #   用 3-5 句话写进 PROGRESS.md 当天总结。


if __name__ == "__main__":
    check_section1()
    # 依次解开下面的调用（完成对应 section 后）：
    # manual_backprop_demo()
    # check_section3()
    # check_section4()
    # check_section5()
    # check_section6()
    # train()
