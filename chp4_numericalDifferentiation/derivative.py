def numerical_diff_v1(f, x):
    """
    会产生舍入误差（指因省略小数的精细部分的数值，而造成最终的计算结果上的误差）
    np.float32(1e-50)   输出为 0.0  无法正确表示出来，使用过小的值会造成计算机出现计算上面的问题
    :param f:
    :param x:
    :return:
    """
    h = 10e-50
    return (f(x+h) - f(x)) / h


def numerical_diff_v2(f, x):
    h = 1e-4  # 0.0001
    return (f(x+h) - f(x-h)) / (2 * h)


def functions_1(x):
    return 0.01 * x**2 + 0.1 * x


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pylab as plt

    x = np.arange(0.0, 20.0, 0.1)
    y = functions_1(x)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, y)
    plt.show()

    print(numerical_diff_v2(functions_1, 5))
    print(numerical_diff_v2(functions_1, 10))