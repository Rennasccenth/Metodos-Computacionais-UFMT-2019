from flask import Flask, request
from methods import lib
from methods.roots import roots
from methods.coefficients import coefficients
from methods.resampling import resampling
from methods.regressions import regressions

app = Flask(__name__)


#  ROOTS

@app.route('/roots/bisection', methods=['POST'])
def bisection():
    func = request.json['funcao']
    a = request.json['a']
    b = request.json['b']
    E = request.json['E']
    res = roots.bisection(func, float(a), float(b), float(E))
    return str(res)


@app.route('/roots/falseposition', methods=['POST'])
def falseposition():
    func = request.json['funcao']
    a = request.json['a']
    b = request.json['b']
    E = request.json['E']
    res = roots.falseposition(func, float(a), float(b), float(E))
    return str(res)


@app.route('/roots/newtonraphson', methods=['POST'])
def newtonraphson():
    func = request.json['funcao']
    avg = request.json['chute']
    E = request.json['E']
    res = roots.newton_raphson(func, float(avg), float(E))
    return str(res)


@app.route('/roots/secant', methods=['POST'])
def secant():
    func = request.json['funcao']
    xnmenos = request.json['xnmenos']
    xn = request.json['xn']
    E = request.json['E']
    res = roots.secant(func, float(xnmenos), float(xn), float(E))
    return str(res)


# COEFFICIENTS

@app.route('/coefficients/spearman', methods=['POST'])
def spearman():
    lista_1 = lib.stringToFloatList(request.json['dado1'])
    lista_2 = lib.stringToFloatList(request.json['dado2'])
    res = coefficients.manofspear(lista_1, lista_2)
    return str(res)


@app.route('/coefficients/kendall', methods=['POST'])
def kendall():
    lista_1 = lib.stringToFloatList(request.json['dado1'])
    lista_2 = lib.stringToFloatList(request.json['dado2'])
    res = coefficients.kendall(lista_1, lista_2)
    return str(res)


@app.route('/coefficients/pearson', methods=['POST'])
def pearson():
    lista_1 = lib.stringToFloatList(request.json['dado1'])
    lista_2 = lib.stringToFloatList(request.json['dado2'])
    res = coefficients.pearson(lista_1, lista_2)
    return str(res)


# CONFIDENCE INTERVAL

@app.route('/confidenceinterval/stddev', methods=['POST'])
def confidenceIntervalStdDeviation():
    numero_elementos = request.json['total']
    intervalo_exigido = request.json['confianca']
    desvio_padrao = request.json['desvio']
    media = request.json['media']
    res = coefficients.confidenceIntervalStdDeviation(int(numero_elementos), float(intervalo_exigido), float(desvio_padrao), float(media))
    return str(res)


@app.route('/confidenceinterval/withoutstddev', methods=['POST'])
def confidenceIntervalWithoutStdDeviation():
    lista = lib.stringToFloatList(request.json['dados'])
    porcentagem = request.json['porcentagem']
    res = coefficients.confidenceIntervalWithoutStdDeviation(float(porcentagem), lista)
    return str(res)


@app.route('/confidenceinterval/popratio', methods=['POST'])
def confidenceIntervalPopRatio():
    sucessos = request.json['sucessos']
    total = request.json['total']
    intervalo_exigido = request.json['confianca']
    res = coefficients.confidenceIntervalPopRatio(int(sucessos), int(total), float(intervalo_exigido))
    return str(res)


# RESAMPLING

@app.route('/resampling/bootstrap', methods=['POST'])
def bootstrap():
    dados = lib.stringToFloatList(request.json['dados'])
    repeticoes = request.json['repeticoes']
    res = resampling.bootstrap(dados, int(repeticoes))
    return str(res)


@app.route('/resampling/jackknife/average', methods=['POST'])
def jackknife_media():
    dados = lib.stringToFloatList(request.json['dados'])
    res = resampling.jao_da_faca(dados)
    return str(res)


@app.route('/resampling/jackknife/variance', methods=['POST'])
def jackknife_variancia():
    dados = lib.stringToFloatList(request.json['dados'])
    res = resampling.jao_da_faca(dados, 1)
    return str(res)


@app.route('/resampling/jackknife/stddev', methods=['POST'])
def jackknife_desviopadrao():
    dados = lib.stringToFloatList(request.json['dados'])
    res = resampling.jao_da_faca(dados, 2)
    return str(res)


@app.route('/resampling/jackknife/confidenceinterval', methods=['POST'])
def jackknife_intervalodeconfianca():
    dados = lib.stringToFloatList(request.json['dados'])
    nv_confianca = request.json['confianca']
    res = resampling.jao_da_faca(dados, 3, int(nv_confianca))
    return str(res)


# REGRESSIONS

@app.route('/regressions/linear', methods=['POST'])
def linear():
    lista_1 = lib.stringToFloatList(request.json['dados1'])
    lista_2 = lib.stringToFloatList(request.json['dados2'])
    res = regressions.linearregression(lista_1, lista_2)
    return str(res)


if __name__ == '__main__':
    app.run()
