import numpy as np

def andFuc_v1(x1, x2):
    """
    与门
    :param x1:
    :param x2:
    :return: 返回0或1
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp > theta:
        return 1
    else:
        return 0

def andFuc_v2(x1, x2):
    """
    与门 版本二
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

def nandFunc(x1, x2):
    """
    与非门
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

def orFunc(x1, x2):
    """
    OR门的实现
    :param x1:
    :param x2:
    :return:
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp > 0:
        return 1
    else:
        return 0

def xorFuc(x1, x2):
    """
    异或门
    :param x1:
    :param x2:
    :return:
    """
    s1 = nandFunc(x1, x2)
    s2 = orFunc(x1, x2)
    y = andFuc_v2(s1, s2)
    return y


if __name__ == '__main__':
    a, b = 0, 0
    res = xorFuc(a, b)
    print(res)
