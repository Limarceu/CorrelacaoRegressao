from Calculo import Calculus
import math

class Correl(Calculus):
    def correlacao(self):
        def r1(self):
            return len(self.x)*Calculus.soma_xy(self)-Calculus.soma(self.x) * Calculus.soma(self.y)
            
        def r2(self):
            return math.sqrt(len(x) * Calculus.soma_quadrado(x)-Calculus.soma(x)**2)
            
        def r3(self):
            return math.sqrt(len(y) * Calculus.soma_quadrado(y)-Calculus.soma(y)**2)
    

        return r1()/(r2()*r3())
       


x = [
    10.3, 9.9,8.7,10.3,7.8,8.7,
    9.2, 8.3, 8.5, 8.4, 8.9, 8.4,
]
y = [
    52.1, 44.3, 39.7, 44.8, 54.7, 49.3,
    48.1, 55.9, 52.9, 52.4, 56.3, 44.5,
]


instancia = Correl(x, y)
print(instancia.correlacao())
