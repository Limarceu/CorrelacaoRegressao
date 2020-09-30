from Calculo import Calculus
import math


class Correlacao(Calculus):
    def __init__(self, x, y, r1=None, r2=None, r3=None):
        super().__init__(x, y)
        self._r1 = len(x)*Calculus.soma_xy(self) - \
            Calculus.soma(x) * Calculus.soma(y)
        self._r2 = math.sqrt(
            len(x) * Calculus.soma_quadrado(x)-Calculus.soma(x)**2)
        self._r3 = math.sqrt(
            len(y) * Calculus.soma_quadrado(y)-Calculus.soma(y)**2)

    def correlacao_r(self):
        if len(self.x) == len(self.y):
            r = self._r1/(self._r2*self._r3)
            return r
