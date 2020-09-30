'''Caluculo do Coeficiente angular a partir de multiplos pontos bidimensionais'''
'''Para calcular a inclinação da reta m receberemos datasets externos'''


from Calculo import Calculus
class Inclinacao(Calculus):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._coef1 = len(x)*Calculus.soma_xy(self) - \
            Calculus.soma(x)*Calculus.soma(y)
        self._coef2 = len(x)*Calculus.soma_quadrado(x) - Calculus.soma(x)**2

    def coeficiente_angular(self):
        return self._coef1/self._coef2

