'''Caluculo do Coeficiente angular a partir de multiplos pontos bidimensionais'''

'''Para calcular a inclinação da reta m receberemos datasets externos'''

import pandas as pd


class Inclinacao:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma_xy(self):
        somador_xy = 0
        for n, xi in enumerate(x):
            somador_xy = x[n]*y[n] + somador_xy
        return somador_xy

    @staticmethod
    def soma(args):
        somador = 0
        for n in args:
            somador += n
        return somador

    @staticmethod
    def soma_quadrado(args):
        soma_quad = 0
        for n in args:
            soma_quad += n**2
        return soma_quad


x = [
    10.3,9.9,8.7,10.3,7.8,8.7,
    9.2,8.3,8.5,8.4,8.9,8.4,
]
y = [
    52.1,44.3,39.7,44.8,54.7,49.3,
    48.1,55.9,52.9,52.4,56.3,44.5,
]

ab = Inclinacao(x, y)
print(ab.soma_xy())
