# -*- coding: utf-8 -*-
r"""
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
#backpropagation is the mathematical core at the modern neural networks.

import math
from typing import Any


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
        other = other if isinstance(other, Value) else Value(other)
        out=Value(self.data + other.data, (self, other), '+')
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    # TODO 1.2 __mul__：同理，op='*'
    def __radd__(self, other):
        # other + self（other 是 int/float 时）：0 + Value 会走到这里
        return self + other

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out=Value(self.data * other.data, (self, other), '*')
        def _backward():
            self.grad += out.grad * other.data
            other.grad += out.grad * self.data
        out._backward = _backward
        return out

    # TODO 1.3 __neg__、__sub__（用 __add__ 和 __neg__ 组合）
    def __neg__(self):
        out=Value(-self.data, (self,), '-')
        def _backward():
            self.grad += out.grad
        out._backward = _backward
        return out


    # TODO 1.4 __sub__：同理，op='-'
    #   提示：返回 Value(self.data - other.data, (self, other), '-')
    def __sub__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data - other.data, (self, other), '-')
        def _backward():
            self.grad += out.grad
            other.grad += -out.grad
        out._backward = _backward
        return out


def check_section1():
    a = Value(2.0, label='a')
    b = Value(-3.0, label='b')
    c = Value(10.0, label='c')
    e = a * b;  e.label = 'e'
    d = e + c;  d.label = 'd'
    assert abs(d.data - 4.0) < 1e-9, "d 应为 2*(-3)+10 = 4"
    assert d._prev == {e, c}, "d 的 children 应包含 e 和 c"
    assert d._op == '+'
    f = Value(d.data-1.0, label='f')
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
    # TODO 2.1 用运算符构造计算图（不要用 .data 手算）
    d = a * b + c;  d.label = 'd'
    L = d * f;       L.label = 'L'

    # TODO 2.2 手动填梯度（直接赋值 .grad）：
    #   L = d * f,  dL/dL = 1
    #   dL/dd = f,  dL/df = d
    #   d = a*b + c, dd/da = b, dd/db = a, dd/dc = 1
    #   → dL/da = f*b,  dL/db = f*a,  dL/dc = f
    L.grad = 1.0
    d.grad = f.data        # dL/dd = f
    f.grad = d.data        # dL/df = d
    a.grad = d.grad * b.data   # dL/da = f * b
    b.grad = d.grad * a.data   # dL/db = f * a
    c.grad = d.grad           # dL/dc = f * 1
    
    assert abs(a.grad - (-2.0 * -3.0)) < 1e-9, "dL/da 应为 f*b"
    assert abs(b.grad - (-2.0 * 2.0)) < 1e-9, "dL/db 应为 f*a"
    assert abs(c.grad - (-2.0)) < 1e-9
    print("[OK] Section 2: 手动反向传播通过")
    return L, a, b, c, f


# ═══════════════════════════════════════════════════════════════
# SECTION 3：自动反向传播 —— 把手动步骤写进 Value
# 视频 1:20:00–1:45:00 段落
# ═══════════════════════════════════════════════════════════════

def backward(self):
    """TODO 3.3：完整反向传播。
    步骤：
      1) self.grad = 1.0
      2) 拓扑排序：DFS 后序收集所有节点到 topo 列表
      3) 逆序遍历 topo，逐节点调用 node._backward()
    """
    # topological order
    topo = []
    visited = set() #visited: node set
    # TODO: 写一个 build_topo(v) 递归函数
    def build_topo(v):
        if v in visited:
            return
        visited.add(v)
        for prev in v._prev:
            build_topo(prev)
        topo.append(v)
    build_topo(self)
    self.grad = 1.0
    for node in reversed(topo):
        node._backward()

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
    out = Value(math.tanh(self.data), (self,), 'tanh')
    def _backward():
        self.grad += (1 - out.data**2) * out.grad
    out._backward = _backward
    return out

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
    out = Value(self.data**other, (self,), f'**{other}')
    def _backward():
        self.grad += other * self.data**(other-1) * out.grad
    out._backward = _backward
    return out

def exp(self):
    out = Value(math.exp(self.data), (self,), 'exp')
    def _backward():
        self.grad += out.data * out.grad
    out._backward = _backward
    return out

def __truediv__(self, other):
    other = other if isinstance(other, Value) else Value(other)
    return self * other ** -1

Value.__pow__ = __pow__
Value.exp = exp
Value.__truediv__ = __truediv__


def check_section5():
    # 1) 前向一致性
    x = Value(0.8)
    t1 = x.tanh()
    t2 = ((x * 2).exp() - 1) / ((x * 2).exp() + 1)
    assert abs(t1.data - t2.data) < 1e-10, f"前向不一致: t1={t1.data}, t2={t2.data}"

    # 2) 梯度校验：两个图独立反传，比较各自 x.grad
    x1 = Value(0.8); t1 = x1.tanh(); t1.backward()
    x2 = Value(0.8); t2 = ((x2 * 2).exp() - 1) / ((x2 * 2).exp() + 1); t2.backward()
    exact = 1 - math.tanh(0.8) ** 2
    assert abs(x1.grad - exact) < 1e-6, f"tanh 直接: {x1.grad} vs {exact}"
    assert abs(x2.grad - exact) < 1e-6, f"tanh via exp/div: {x2.grad} vs {exact}"
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
    def __init__(self, nin, nonlin=True):
        self.nonlin = nonlin
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(random.uniform(-1,1))
    def __call__(self,x):
        act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
        return act.tanh() if self.nonlin else act

    def parameters(self):
        return self.w + [self.b]
class Layer(Module):
    # TODO 6.3：neurons = [Neuron(nin) for _ in range(nout)]
    def __init__(self, nin, nout):
        self.neurons =[Neuron(nin) for _ in range(nout)]

    def __call__(self,x):
        outs= [n(x) for n in self.neurons]
        return outs[0]  if len(outs)==1 else outs

    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]

class MLP(Module):
    # TODO 6.4：sizes 形如 [3, 4, 4, 1]，逐层建 Layer
    def __init__(self,nin,nout):
        sz=[nin]+nout
        self.layers =[Layer(sz[i],sz[i+1]) for i in range(len(nout))]
    def __call__(self,x):
        for layer in self.layers:
            x=layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

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

def train(lr=0.05, n_epochs=50, verbose=True):
    """TODO 7.2 实验：不同 lr 的收敛对比。每个 lr 必须独立训练一轮。"""
    mlp = MLP(3, [4, 4, 1])
    xs = [[2.0, 3.0, -1.0], [3.0, -1.0, 0.5], [0.5, 1.0, 1.0], [1.0, 1.0, -1.0, 0.7]]
    ys = [1.0, -1.0, -1.0, 1.0]
    for epoch in range(n_epochs):
        # 1) 前向 + 损失（每轮重算！参数变了，预测就变了）
        ypred = [mlp(x) for x in xs]
        loss = sum((yout - ygt)**2 for yout, ygt in zip(ypred, ys))
        # 2) 清梯度 -> 反向传播
        mlp.zero_grad()
        loss.backward()
        # 3) 梯度下降：一个 epoch 只按一个 lr 更新一次
        for p in mlp.parameters():
            p.data -= lr * p.grad
        # 4) 每 10 步打印
        if verbose and epoch % 10 == 0:
            print(f"  epoch {epoch}, loss {loss.data:.4f}")
    ypred = [mlp(x) for x in xs]
    if verbose:
        print("  最终预测:", [round(p.data, 3) for p in ypred])
        print("  目标标签:", ys)
    return loss.data


if __name__ == "__main__":
    check_section1()
    # 依次解开下面的调用（完成对应 section 后）：
    manual_backprop_demo()
    check_section3()
    check_section4()
    check_section5()
    check_section6()
    # TODO 7.2：lr 对比实验（各自独立训练）
    print("=== lr=0.05 基准 ===")
    train(lr=0.05)
    print("=== lr=0.5 过大，观察震荡 ===")
    print(f"  50 epoch 后 loss = {train(lr=0.5, verbose=False):.4f}")
    print("=== lr=0.01 过小，观察收敛慢 ===")
    print(f"  50 epoch 后 loss = {train(lr=0.01, verbose=False):.4f}")
