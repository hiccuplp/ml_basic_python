import numpy as np
from activationFuc import sigmoid


def init_network():
    # 进行权重和偏置的初始化
    network = {}
    network["W1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    network["W2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    network["W3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network


def forword(network, x):
    # 将输入信号转换成输出信号的处理过程
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


def identity_function(x):
    # 恒等函数，作为输出层的激活函数
    # 回归问题可以使用恒等函数，二元分类问题可以使用sigmoid函数
    # 多元分类问题可以使用softmax函数
    return x


if __name__ == '__main__':
    X = np.array([1, 2])
    print(X.shape)
    W = np.array([[1, 3, 5], [2, 4, 6]])
    print(W.shape)
    Y = np.dot(X, W)   # 计算多维数组的点积
    print(Y)
    # 神经网络各层的运算可以作为矩阵运算打包进行

    # 实现书中的3.9式
    X = np.array([1.0, 0.5])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    B1 = np.array([0.1, 0.2, 0.3])
    A1 = np.dot(X, W1) + B1
    print("A1:", A1)
    Z1 = sigmoid(A1)
    print("Z1:", Z1)

    W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    B2 = np.array([0.1, 0.2])
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    print("Z2:", Z2)

    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    B3 = np.array([0.1, 0.2])
    A3 = np.dot(Z2, W3) + B3
    Y = identity_function(A3)
    print("Y:", Y)

    # 演示调用
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forword(network, x)
    print("y:", y)   # [0.20993715 0.46282556]  为什么和书里面的运算结果不一样？