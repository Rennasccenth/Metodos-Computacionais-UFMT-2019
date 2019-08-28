import math
from methods import lib


def manofspear(data_x: list, data_y: list) -> float:
    """
    :param data_x: Primeira lista contendo os valores de uma entidade de uma amostra.
    :param data_y: Segunda lista contendo os valores de outra entidade da mesma amostra.
    :return: valor do Coeficiente de Spearman para as duas entidades, baseado nas
    amostras inseridas.
    """

    copy_x = data_x.copy()
    copy_y = data_y.copy()

    copy_x.sort()
    copy_y.sort()

    x_posts, y_posts, x_adjustedposts, y_adjustedposts, spearman = [], [], [], [], []

    for x, y in zip(copy_x, copy_y):  # Percorre a lista ordenada
        x_posts.append(((lib.sumWithoutMath(lib.valueIndexes(copy_x, x)) / len(lib.valueIndexes(copy_x, x))),
                        x))  # (Posto do x, valor)
        y_posts.append(((lib.sumWithoutMath(lib.valueIndexes(copy_y, y)) / len(lib.valueIndexes(copy_y, y))),
                        y))  # (Posto do y, valor)

    for x, y in zip(data_x, data_y):
        for iterator_x, iterator_y in zip(x_posts, y_posts):
            if iterator_x[1] == x:
                x_adjustedposts.append(iterator_x[0])
            if iterator_y[1] == y:
                y_adjustedposts.append(iterator_y[0])

    for x, y in zip(x_adjustedposts, y_adjustedposts):
        spearman.append((x - y) ** 2)

    return 1 - 6 * sum(spearman) / (len(data_x) * (len(data_x) ** 2 - 1))


def pearson(data_x: list, data_y: list) -> float:
    """
    :param data_x: Primeira lista contendo os valores de uma entidade de uma amostra.
    :param data_y: Segunda lista contendo os valores de outra entidade da mesma amostra.
    :return: valor do Coeficiente de Pearson para as duas entidades, baseado nas
    amostras inseridas.
    """

    x_avg = lib.averageWithoutNumPy(data_x)
    y_avg = lib.averageWithoutNumPy(data_y)

    xi_Xavg, yi_Yavg = [], []
    for x, y in zip(data_x, data_y):
        xi_Xavg.append(x - x_avg)
        yi_Yavg.append(y - y_avg)

    sumprod, denominator_x, denominator_y = 0, 0, 0
    for i, j in zip(xi_Xavg, yi_Yavg):
        sumprod += i * j
        denominator_x += i ** 2
        denominator_y += j ** 2

    return sumprod / (math.sqrt(denominator_x) * math.sqrt(denominator_y))


def kendall(data_x: list, data_y: list) -> float:
    """
    :param data_x: Primeira lista contendo os valores de uma entidade de uma amostra.
    :param data_y: Segunda lista contendo os valores de outra entidade da mesma amostra.
    :return: valor do Coeficiente de Kendall para as duas entidades, baseado nas
    amostras inseridas.
    """
    concordant, discordant = 0, 0
    for i in range(len(data_x)):
        for j in range(i + 1, len(data_x)):
            if (data_x[j] >= data_x[i] and data_y[j] > data_y[i]) or \
                    (data_x[j] < data_x[i] and data_y[j] < data_y[i]) or \
                    (data_x[j] > data_x[i] and data_y[j] >= data_y[i]):
                concordant = concordant + 1
            else:
                discordant = discordant + 1

    return (concordant - discordant) / ((len(data_x) * (len(data_x) - 1)) / 2)


def confidenceIntervalWithoutStdDeviation(percentage: float, sample: list) -> tuple:
    return (lib.averageWithoutNumPy(sample) + (lib.tStudent(percentage, len(sample)) * lib.stdDeviation(sample) / math.sqrt(len(sample)))), \
           (lib.averageWithoutNumPy(sample) - (lib.tStudent(percentage, len(sample)) * lib.stdDeviation(sample) / math.sqrt(len(sample))))


def confidenceIntervalPopRatio(sucess: int, total: int, t_level: float) -> tuple:
    """
    :param sucess: casos de sucesso na amostra.
    :param total: numero total da amostra.
    :param t_level: intervalo de confiança exigido.
    :return: intervalo de confianca inferior e posterior para a amostra inserida.
    """
    p_pop = sucess / total
    zC = lib.zcritical("zTable.csv", t_level)

    return p_pop - zC * math.sqrt((p_pop * (1 - p_pop)) / total), p_pop + zC * math.sqrt((p_pop * (1 - p_pop) / total))


def confidenceIntervalStdDeviation(elements: int, t_level: float, deviation: float , avg: float, ) -> tuple:
    """
    :param avg: média da amostra.
    :param elements: quantidade de elementos da amostra
    :param t_level: nivel de confiança exigido.
    :param deviation: desvio padrão a ser utilizado, caso não seja passado,
    será calculado a partir dos dados da amostra para o prosseguimento do procedimento.
    :return: tupla contendo o intervalo de confiança inferior e o posterior.
    """
    zC = lib.zcritical('zTable.csv', t_level)

    return avg - zC * (deviation / math.sqrt(elements)), \
           avg + zC * (deviation / math.sqrt(elements))
