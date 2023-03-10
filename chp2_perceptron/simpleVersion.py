def andFuc(x1, x2):
    """
    与门
    :param x1:
    :param x2:
    :return: 返回0或1
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp >= theta:
        return 1
    else:
        return 0


if __name__ == '__main__':
    x1, x2 = 1, 0
    res = andFuc(x1, x2)
    print(res)
