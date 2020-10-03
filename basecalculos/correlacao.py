from basecalculos.calculo import Calculus
import math


class Correlacao(Calculus):
    def __init__(self, x, y, r1=None, r2=None, r3=None):
        super().__init__(x, y)
        self.r1 = len(x)*Calculus.soma_xy(self) - Calculus.soma(self, self.x) * Calculus.soma(self, self.y)
        self.r2 = math.sqrt(
            len(x) * Calculus.soma_quadrado(self, self.x)-Calculus.soma(self, self.x)**2)
        self.r3 = math.sqrt(
            len(y) * Calculus.soma_quadrado(self, self.y)-Calculus.soma(self, self.y)**2)

    def correlacao_r(self):
        if len(self.x) == len(self.y):
            r = self.r1/(self.r2*self.r3)
            return r


