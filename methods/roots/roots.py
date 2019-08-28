import importlib
import os
import function
import sys
from methods import lib
from decimal import Decimal

sys.setrecursionlimit(1000000000)


def reload_funcao():
    importlib.reload(function)
    os.system('rm -r __pycache__')


def functionline(function_str:str, x: float) -> float:
    """
    :param function_str:
    :param x: argumento da função.
    :return: valor propriamente dito da derivada da função gravada em -> function()
    """
    lib.receiveFunction(function_str)
    reload_funcao()

    h = Decimal(0.0000000000000000000000001)
    return Decimal(Decimal((function.f(Decimal(x) + h) - Decimal(function.f(x))) / h))


def bisection(function_str: str, a: float, b: float, E: float) -> float:
    """
    :param function_str: string da função.
    :param a: chute numero 1
    :param b: chute numero 2
    :param E: margem de erro
    :return: valor em que a função atinge a imagem = 0
    """

    lib.receiveFunction(function_str)
    reload_funcao()

    if function.f(a) * function.f(b) > 0:
        return "Intervalo inválido!"

    if abs(function.f(b)) > E:
        avg = (a + b) / 2
        if function.f(avg) * function.f(a) < 0:
            return bisection(function_str, a, avg, E)
        else:
            return bisection(function_str, b, avg, E)

    return b


def falseposition_aux(a: float, b: float, E: float):
    if function.f(a) * function.f(b) > 0:
        return "Intervalo inválido!"
    if abs(function.f(b)) > E:
        avg = ((a * function.f(b) - b * function.f(a)) / (function.f(b) - function.f(a)))
        if function.f(avg) * function.f(a) < 0:
            return falseposition_aux(a, avg, E)
        else:
            return falseposition_aux(b, avg, E)

    return b


def falseposition(function_str: str, a: float, b: float, E: float) -> float:
    """
    :param function_str: string da função
    :param a: chute numero 1
    :param b: chute numero 2
    :param E: margem de erro
    :return: valor em que a função atinge a imagem = 0
    """
    lib.receiveFunction(function_str)
    reload_funcao()

    res = falseposition_aux(a, b, E)
    return res


def newton_raphson(function_str: str, avg: float, E: float) -> float:
    """
    :param function_str: string da função
    :param avg: chute inicial
    :param E: margem de erro
    :return: valor em que a função atinge a imagem = 0
    """

    lib.receiveFunction(function_str)
    reload_funcao()

    if abs(function.f(avg)) > E:
        aux = Decimal(avg) - Decimal(function.f(avg)) / functionline(function_str, avg)
        return newton_raphson(function_str, aux, E)
    return avg


def secant(function_str: str, xnmenos: float, xn: float, E: float) -> float:
    """
    :param function_str: string da função
    :param xnmenos: valor do xi - 1
    :param xn: valor do xi
    :param E: margem de erro
    :return: valor em que a função atinge a imagem = 0
    """

    lib.receiveFunction(function_str)
    reload_funcao()

    xnmais = ((xnmenos * function.f(xn) - xn * function.f(xnmenos)) / (function.f(xn) - function.f(xnmenos)))
    if abs(function.f(xn)) > E:
        return secant(function_str, xn, xnmais, E)
    else:
        return xn
