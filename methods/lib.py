import importlib
import os
import sys
import math

sys.setrecursionlimit(10000000)

file_function = '''
from math import *


def f(x):
    return {}
'''


def receiveFunction(string):
    with open('function.py', 'w') as file:
        file.writelines(file_function.format(string))


def function(x: float) -> float:
    """
    :param x: argumento da função
    :return: valor da função no ponto do argumento.
    """
    return (x * x * x) - 5 * x + 2


def averageWithoutNumPy(array: list) -> float:
    """
    :param array: array de float ou int.
    :return: magicamente retorna a média aritimética dos valores nesse array.
    """

    count, avg = 0, 0
    while count < len(array):
        avg += array[count]
        count += 1

    return avg / len(array)


def sumWithoutMath(array: list) -> float:
    """
    :param array: array de valores float ou int.
    :return: faz a incrível mágica de somar todos os valores
    dessa lista e nos devolve o resultado (e tudo isso sem usar a
    função sum!!, o que é claramente impressionante!)
    """
    count, sum_ = 0, 0
    while count < len(array):
        sum_ += array[count]
        count += 1

    return sum_


def valueIndexes(array: list, value: float) -> list:
    """
    :param array: lista contendo os valores a serem procurados.
    :param value: valor a ser procurado na lista.
    :return: lista contendo os índices aonde aquele valor apareceu.
    """
    res = []
    for index, item in enumerate(array):
        if item == value:
            res.append(index + 1)

    return res


def zcritical(tablepath: str, percentage: float) -> float:
    """
    :param tablepath: caminho para o .csv da tabela.
    :param percentage: intervalo de confiança exigido, no formato [percentage]%.
    :return: correspondencia mais próxima na Tabela de Distribuição
    normal.
    """
    percentage = abs(percentage) / 200

    with open(tablepath) as file:
        column = file.readline().replace("\n", '').replace(',', '.').split(";")
        column.pop(0)
        value, table = [], []

        for item in file:
            stream = item.replace('\n', '').replace(',', '.')
            stream_listed = stream.split(';')
            value.append(stream_listed.pop(0))
            table.append(stream_listed)

        minor_distance = 10
        for horiz in table:
            for vert in horiz:
                current = abs(float(vert) - percentage)
                if current < minor_distance:
                    minor_distance = current
                    line = table.index(horiz)
                    pilar = horiz.index(vert)

    return float(value[line]) + float(column[pilar])


def stdDeviation(sample: list) -> float:
    """
    :param sample: lista contendo os valores da amostra
    :return: desvio padrão da amostra
    """
    averg = averageWithoutNumPy(sample)

    aux = []
    for i in sample:
        aux.append((i - averg) ** 2)

    return math.sqrt(sum(aux) / (len(sample)))


def tStudent(percentage: float, elements: int, tablepath: str = 'tStudent.csv') -> float:
    degree_of_freedom = elements - 1
    percentage = 1 - percentage / 100

    with open(tablepath) as file:

        column = file.readline().replace("\n", '').replace(',', '.').split(";")
        column.pop(0)
        degrees, table = [], []

        for item in file:
            stream = item.replace('\n', '').replace(',', '.')
            stream_listed = stream.split(';')
            degrees.append(stream_listed.pop(0))
            table.append(stream_listed)

        minor_distance_i, minor_distance_j = 100, None

        for i in column:
            if minor_distance_i > abs(float(i) - percentage):
                minor_distance_i = abs(float(i) - percentage)
                pilar = column.index(i)

        for j in degrees:
            if j is 'i':
                pass
            elif minor_distance_j is None or (minor_distance_j > abs(float(j) - degree_of_freedom)):
                minor_distance_j = abs(float(j) - degree_of_freedom)
                line = degrees.index(j)

    return float(table[line][pilar])


def stringToFloatList(string: str) -> list:
    res = []
    for i in string.replace('[', '').replace(']', '').split(','):
        res.append(float(i))
    return res
