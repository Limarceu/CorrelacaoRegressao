'''O Cálculo utiliza como entrada duas listas como argumentos.
    Tais argumentos podem ser extraídos de tabelas xlxs, csv
    ou qualquer extensão de arquivos que suportem datasets lidos
    pelo pandas.
'''

class Calculus():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def soma_xy(self):
        somador_xy = 0
        for n, xi in enumerate(self.x):
            somador_xy = self.x[n]*self.y[n] + somador_xy
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
