from methods import lib
from decimal import Decimal


def b(data_x, data_y):
    sum_xy, sum_x_2 = [], []
    for x, y in zip(data_x, data_y):
        sum_xy.append(x * y)
        sum_x_2.append(x**2)
    n = len(data_x)
    return ((n * sum(sum_xy)) - (sum(data_x) * sum(data_y))) / (n * sum(sum_x_2) - (sum(data_x)) ** 2)


def a(data_y, data_x):
    b_ = b(data_x, data_y)
    return str(lib.averageWithoutNumPy(data_y) - b_ * lib.averageWithoutNumPy(data_x))


def linearregression(data_x: list, data_y: list) -> str:
    """
    :param data_x: Lista de dados 1
    :param data_y: Lista de dados 2
    :return: String contendo a função linear
    """
    return str(a(data_x, data_y) + " + (" + (str(b(data_y, data_x))) + ").x + e")
