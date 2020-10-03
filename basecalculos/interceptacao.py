from basecalculos.calculo import Calculus
from basecalculos.regressao import Inclinacao

class Interceptacao(Inclinacao):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._somx = Calculus.soma(self, self.x)
        self._somy = Calculus.soma(self, self.y)
        self.coeficiente_angular = self._coef1/self._coef2


    def interceptacao_b(self):
        b = (self._somy - self.coeficiente_angular*self._somx)/len(self.x)
        return b


