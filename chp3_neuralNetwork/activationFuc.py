import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    # 阶跃函数
    if x > 0:
        return 1
    else:
        return 0


def step_function_v2(x):
    # 阶跃函数
    y = x > 0  # 不等号运算
    return y.astype(np.int)


def plot_func(x, y):
    # 绘图函数
    plt.plot(x, y)
    plt.ylim(np.min(y) - 1, np.max(y) + 1)  # 指定y轴的范围
    plt.show()


def sigmoid(x):
    # sigmoid function
    return 1 / (1 + np.exp(x))


if __name__ == '__main__':
    value = 9
    print(step_function(value))

    value_2 = np.arange(-5.0, 5.0, 0.1)
    result = step_function_v2(value_2)
    plot_func(value_2, result)

    # sigmoid函数的平滑性对神经网络的学习具有重要意义。
    # 感知机中神经元之间流动的是0或1的二元信号，而神经网络中流动的是连续的实数值信号。
    # 线性函数的问题：不管如何加深层数，总是存在与之等效的“无隐藏层的神经网络”。
    # 使用线性函数，无法发挥多层网络带来的优势。
    result2 = sigmoid(value_2)
    plot_func(value_2, result2)
