import math
import random
from methods import lib
from methods.coefficients import coefficients


def bootstrap(data: list, rep: int) -> float:
    """
    :param data: Lista contendo os dados da amostra.
    :param rep: Numero de repetições a ser realizada.
    :return:
    """

    avg = lib.averageWithoutNumPy(data)
    print('Média: ', avg)
    averages, buffer = [], []

    for _ in range(rep):
        buffer = data.copy()
        buffer.pop(random.randrange(0, len(data)))
        averages.append(lib.sumWithoutMath(buffer) / len(buffer))
        buffer.clear()

    return lib.sumWithoutMath(averages) / len(averages)


def jack_knife_avg(data: list) -> float:
    """
    :param data: conjunto dos dados.
    :return: estimativa jack knife dos dados.
    """
    jack_knife_sample, buffer = [], []

    for i in range(len(data)):
        buffer = data.copy()
        buffer.pop(i)
        jack_knife_sample.append(lib.sumWithoutMath(buffer) / len(buffer))
        buffer.clear()
    return lib.sumWithoutMath(jack_knife_sample) / len(jack_knife_sample)


def jack_knife_variance(data: list) -> float:
    jack_knife_sample, buffer = [], []
    jkap = jack_knife_avg(data)

    for i in range(len(data)):
        buffer = data.copy()
        buffer.pop(i)
        for j in buffer:
            aux = j - jkap
            jack_knife_sample.append(aux**2)
        buffer.clear()

    return lib.sumWithoutMath(jack_knife_sample) / (len(data) - 1)


def jao_da_faca(data: list, flag: int = 0, n=None):
    """
    :param n: Opcional, representa o nivel de confiança exigido.
    :param data: Lista dos dados da amostra.
    :param flag: Estimativa a ser utilizada.
    :return:
    """
    avg = lib.averageWithoutNumPy(data)
    if flag == 0:
        return jack_knife_avg(data)
    elif flag == 1:
        return jack_knife_variance(data)
    elif flag == 2:
        return math.sqrt(jack_knife_variance(data))
    elif flag == 3:
        return coefficients.confidenceIntervalStdDeviation \
            (len(data), n, math.sqrt(jack_knife_variance(data)), jack_knife_avg(data))
