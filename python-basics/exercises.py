# -*- coding: utf-8 -*-
"""
Python 基础练习 16 题 —— 代码骨架与自动判题器
题面与提示见同目录 EXERCISES.md。

规则：
  - 只改函数/方法体（把 raise NotImplementedError 替换成你的实现）
  - 不要改函数名和任何 check_xx() 判题函数
  - 随时运行：  .venv\\Scripts\\python python-basics\\exercises.py

本文件只用到 Python 标准库，刻意不 import numpy。
"""

import math
import random


# ═══════════════════════════════════════════════════════════════
# Set 1：函数、循环、列表（第 1–4 题）
# ═══════════════════════════════════════════════════════════════

def sieve(n):
    """第1题：返回所有不超过 n 的素数（升序）。sieve(1) == []"""
    raise NotImplementedError("第1题：埃氏筛法")


def newton_sqrt(a, tol=1e-12):
    """第2题：牛顿迭代求 sqrt(a)，初值 a/2，|x^2-a|<=tol 停止；a==0 返回 0.0"""
    raise NotImplementedError("第2题：牛顿法")


def collatz_longest(limit):
    """第3题：1<=s<=limit 中考拉兹链最长者，返回 (起点, 链长)；
    链长含起点与 1；并列取较小起点。collatz_longest(10) == (9, 20)"""
    raise NotImplementedError("第3题：考拉兹链")


def euler_phi(n):
    """第4题：欧拉函数；phi(1)==1, phi(9)==6, phi(10)==4, phi(12)==4"""
    raise NotImplementedError("第4题：欧拉函数")


# ═══════════════════════════════════════════════════════════════
# Set 2：字典、字符串、嵌套结构（第 5–8 题）
# ═══════════════════════════════════════════════════════════════

def word_frequency(text):
    """第5题：小写化、按空白分词、剥掉词尾标点 . , ; : ! ? " ' ( )，
    返回 [(词, 次数)]，次数降序、同次数按词典序升序。"""
    raise NotImplementedError("第5题：词频统计")


def mat_mul(A, B):
    """第6题：纯 Python 三重循环矩阵乘（禁用 numpy/zip 取巧）。
    [[1,2],[3,4]] x [[5,6],[7,8]] == [[19,22],[43,50]]"""
    raise NotImplementedError("第6题：矩阵乘法")


def merge_intervals(intervals):
    """第7题：合并重叠或端点相接的区间，返回排序后的 tuple 列表。
    [[1,3],[2,6],[8,10],[15,18]] -> [(1,6),(8,10),(15,18)]"""
    raise NotImplementedError("第7题：合并区间")


def sparse_dot(x, y):
    """第8题：dict 稀疏向量点积，遍历较短者。
    {0:2,2:3} · {0:4,1:5,2:1} == 11"""
    raise NotImplementedError("第8题：稀疏点积")


# ═══════════════════════════════════════════════════════════════
# Set 3：递归、推导式、闭包与高阶函数（第 9–12 题）
# ═══════════════════════════════════════════════════════════════

def quicksort(lst):
    """第9题：首元素为 pivot 的函数式快排，返回新列表，不改原列表。"""
    raise NotImplementedError("第9题：快速排序")


def memoize(f):
    """第10题：返回带缓存的 wrapper；同参数只真正计算一次。
    缓存用 dict，键直接用 args。"""
    raise NotImplementedError("第10题：memoize")


def derivative(f, h=1e-6):
    """第11题：中心差商，返回函数 g(x) = (f(x+h)-f(x-h))/(2h)。"""
    raise NotImplementedError("第11题：数值导数")


def numerical_gradient(f, x, h=1e-6):
    """第12题：f: list -> float，对每个坐标中心差商，返回梯度 list。"""
    raise NotImplementedError("第12题：数值梯度")


# ═══════════════════════════════════════════════════════════════
# Set 4：面向对象与运算符重载（第 13–16 题）
# ═══════════════════════════════════════════════════════════════

class Fraction:
    """第13题：不可约有理数，分母恒正。实现 __init__ / __add__ / __eq__ / __repr__。"""

    def __init__(self, num, den):
        # TODO: 用 gcd 约分；den 为负时把符号移到分子；den==0 让它自然抛 ZeroDivisionError
        raise NotImplementedError("第13题：Fraction.__init__")

    def __add__(self, other):
        # TODO: a/b + c/d = (a*d + c*b) / (b*d)，返回新的 Fraction（构造时自动约分）
        raise NotImplementedError("第13题：Fraction.__add__")

    def __eq__(self, other):
        # TODO: 约分后分子分母分别相等
        raise NotImplementedError("第13题：Fraction.__eq__")

    def __repr__(self):
        # TODO: 返回形如 "1/2" 的字符串：f"{self.num}/{self.den}"
        raise NotImplementedError("第13题：Fraction.__repr__")


class Polynomial:
    """第14题：系数低次到高次排列。实现 __call__（Horner 求值）/ __add__ / degree。"""

    def __init__(self, coeffs):
        self.coeffs = list(coeffs)

    def __call__(self, x):
        # TODO: Horner 法，如 [1,2,3] -> 1 + x*(2 + x*3)
        raise NotImplementedError("第14题：Polynomial.__call__")

    def __add__(self, other):
        # TODO: 短的补 0，逐系数相加，返回新 Polynomial
        raise NotImplementedError("第14题：Polynomial.__add__")

    @property
    def degree(self):
        # TODO: 最高非零系数的下标；全零（含空列表）返回 -1
        raise NotImplementedError("第14题：Polynomial.degree")


class Linear:
    """第15题：线性层雏形。W 为 nout x nin 嵌套列表，b 为长度 nout 的列表。"""

    def __init__(self, W, b):
        self.W = W
        self.b = b

    def __call__(self, x):
        # TODO: 每行与 x 逐元素相乘求和，再加对应偏置
        raise NotImplementedError("第15题：Linear.__call__")

    def parameters(self):
        # TODO: 摊平返回 [W 的全部元素..., b 的全部元素...]
        raise NotImplementedError("第15题：Linear.parameters")


class Number:
    """第16题（选做）：标量自动微分，micrograd 第1–3节闭卷默写版。"""

    def __init__(self, data, _children=()):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._backward = lambda: None

    def __add__(self, other):
        # TODO: 构造 out；out._backward 把 out.grad 累加给两个输入（注意是 +=）
        raise NotImplementedError("第16题：Number.__add__")

    def __mul__(self, other):
        # TODO: self.grad += other.data * out.grad；另一个对称
        raise NotImplementedError("第16题：Number.__mul__")

    def backward(self):
        # TODO: self.grad = 1；拓扑排序后逆序调用各节点 _backward()
        raise NotImplementedError("第16题：Number.backward")


# ═══════════════════════════════════════════════════════════════
# 判题器（不要修改）
# ═══════════════════════════════════════════════════════════════

def check_01():
    assert sieve(1) == []
    assert sieve(2) == [2]
    assert sieve(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert len(sieve(1000)) == 168  # π(1000) = 168


def check_02():
    assert newton_sqrt(0.0) == 0.0
    assert abs(newton_sqrt(2) - math.sqrt(2)) < 1e-10
    assert abs(newton_sqrt(25) - 5.0) < 1e-10
    assert abs(newton_sqrt(1e-8) - 1e-4) < 1e-10


def check_03():
    s, length = collatz_longest(10)
    assert (s, length) == (9, 20), f"期望 (9,20)，实际 ({s},{length})"
    s1, l1 = collatz_longest(1)
    assert (s1, l1) == (1, 1)


def check_04():
    assert euler_phi(1) == 1
    assert euler_phi(9) == 6
    assert euler_phi(10) == 4
    assert euler_phi(12) == 4
    assert euler_phi(7) == 6  # 素数 p：phi(p)=p-1


def check_05():
    text = "The cat sat on the mat; the cat ran."
    got = word_frequency(text)
    assert got[0] == ("the", 3), got
    assert got[1] == ("cat", 2), got
    # 次数为 1 的词按词典序
    assert [w for w, c in got if c == 1] == ["mat", "on", "ran", "sat"], got


def check_06():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert mat_mul(A, B) == [[19, 22], [43, 50]]
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert mat_mul(I, M) == M
    C = [[1, 2, 3]]          # 1x3
    D = [[1], [2], [3]]      # 3x1
    assert mat_mul(C, D) == [[14]]


def check_07():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == \
        [(1, 6), (8, 10), (15, 18)]
    assert merge_intervals([[3, 5], [1, 3]]) == [(1, 5)]          # 相接合并 + 乱序
    assert merge_intervals([[1, 2], [4, 5]]) == [(1, 2), (4, 5)]  # 不相交
    assert merge_intervals([]) == []


def check_08():
    assert sparse_dot({0: 2, 2: 3}, {0: 4, 1: 5, 2: 1}) == 11
    assert sparse_dot({}, {1: 9}) == 0
    assert sparse_dot({0: 1, 3: 2}, {1: 4, 2: 5}) == 0


def check_09():
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert quicksort(data) == sorted(data)
    assert data == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], "不得修改原列表"
    rng = random.Random(0)
    for _ in range(20):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(0, 30))]
        assert quicksort(xs) == sorted(xs)


def check_10():
    calls = []

    @memoize
    def fib(n):
        calls.append(n)
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    assert fib(20) == 6765
    assert len(calls) == 21 and len(set(calls)) == 21, \
        f"每个 n 应只真正计算一次，实际调用记录 {len(calls)} 条"
    assert fib(20) == 6765 and len(calls) == 21, "第二次调用应命中缓存，不再执行 f"


def check_11():
    g = derivative(lambda x: x * x)
    assert abs(g(3) - 6) < 1e-5
    assert abs(derivative(math.sin)(0.0) - 1.0) < 1e-5
    assert abs(derivative(lambda x: x ** 3)(2) - 12) < 1e-4


def check_12():
    f1 = lambda v: sum(v)
    assert numerical_gradient(f1, [1.0, 2.0, 3.0]) == [1.0, 1.0, 1.0] or \
        all(abs(a - b) < 1e-6 for a, b in
            zip(numerical_gradient(f1, [1.0, 2.0, 3.0]), [1.0, 1.0, 1.0]))
    f2 = lambda v: v[0] ** 2 + 2 * v[1] ** 2
    g = numerical_gradient(f2, [3.0, 4.0])
    assert abs(g[0] - 6) < 1e-5 and abs(g[1] - 16) < 1e-5, g


def check_13():
    assert Fraction(2, 4) == Fraction(1, 2)
    assert Fraction(1, 2) + Fraction(1, 3) == Fraction(5, 6)
    assert Fraction(1, -2).num == -1 and Fraction(1, -2).den == 2
    assert repr(Fraction(1, 2)) == "1/2"
    assert Fraction(3, 7) + Fraction(4, 7) == Fraction(1, 1)


def check_14():
    p = Polynomial([1, 2, 3])
    assert p(2) == 17
    assert p(0) == 1
    q = p + Polynomial([-1, 0, -3, 1])
    assert q.coeffs == [0, 2, 0, 1]
    assert Polynomial([1, 2, 3]).degree == 2
    assert Polynomial([0, 0, 0]).degree == -1


def check_15():
    layer = Linear([[1, 2], [3, 4]], [1, 1])
    assert layer([1, 1]) == [4, 8]
    assert layer([0, 0]) == [1, 1]
    assert layer.parameters() == [1, 2, 3, 4, 1, 1]


def check_16():
    a, b, c, f = Number(2.0), Number(-3.0), Number(10.0), Number(-2.0)
    L = (a * b + c) * f
    assert abs(L.data - (-8.0)) < 1e-9
    L.backward()
    assert abs(a.grad - 6.0) < 1e-9, f"da 应为 6，实际 {a.grad}"
    assert abs(b.grad - (-4.0)) < 1e-9
    assert abs(c.grad - (-2.0)) < 1e-9
    assert abs(f.grad - 4.0) < 1e-9


_CHECKS = {
    1: check_01, 2: check_02, 3: check_03, 4: check_04,
    5: check_05, 6: check_06, 7: check_07, 8: check_08,
    9: check_09, 10: check_10, 11: check_11, 12: check_12,
    13: check_13, 14: check_14, 15: check_15, 16: check_16,
}

_TITLES = {
    1: "埃氏筛法", 2: "牛顿法求平方根", 3: "最长考拉兹链", 4: "欧拉函数",
    5: "词频统计", 6: "矩阵乘法", 7: "合并区间", 8: "稀疏向量点积",
    9: "快速排序", 10: "memoize 装饰器", 11: "数值导数", 12: "数值梯度",
    13: "Fraction 有理数类", 14: "Polynomial 多项式类",
    15: "Linear 线性层", 16: "Number 自动微分(选做)",
}


def main():
    passed = 0
    for num in range(1, 17):
        try:
            _CHECKS[num]()
            print(f"[OK] 第{num:>2}题 通过    {_TITLES[num]}")
            passed += 1
        except NotImplementedError:
            print(f"[  ] 第{num:>2}题 未完成  {_TITLES[num]}")
        except AssertionError as e:
            print(f"[X]  第{num:>2}题 答案错误 {_TITLES[num]}  -> {e}")
        except Exception as e:
            print(f"[!]  第{num:>2}题 运行报错 {_TITLES[num]}  -> "
                  f"{type(e).__name__}: {e}")
    print(f"\n进度：{passed}/16")
    if passed == 16:
        print("全部通过！回 micrograd 继续 SECTION 2。")


if __name__ == "__main__":
    main()
