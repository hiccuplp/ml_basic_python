import numpy as np


def softmax_v1(a):
    # softmax函数实现，存在缺陷：溢出问题。指数函数的值容易变得非常大
    exp_a = np.exp(a)
    exp_sum_a = np.sum(exp_a)
    y = exp_a / exp_sum_a
    return y


def softmax_v2(a):
    # softmax函数实现，防止溢出版本
    c = np.max(a)
    exp_a = np.exp(a - c)
    exp_sum_a = np.sum(exp_a)
    y = exp_a / exp_sum_a
    return y


if __name__ == '__main__':
    # 输出之和为1式softmax函数的一个重要性质。
    # 正因为有了这个性质，我们才可以把softmax函数的输出解释为”概率“。
    a = np.array([0.3, 2.9, 4.0])
    y = softmax_v1(a)
    print("y:", y)
    y2 = softmax_v2(a)
    print("y2:", y2)