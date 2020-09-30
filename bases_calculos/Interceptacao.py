from Calculo import Calculus
from Regressao import Inclinacao

class Interceptacao(Inclinacao):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._somx = Calculus.soma(x)
        self._somy = Calculus.soma(y)
        self.coeficiente_angular = self._coef1/self._coef2


    def Interceptacao_b(self):
        b = (self._somy - self.coeficiente_angular*self._somx)/len(x)
        return b

