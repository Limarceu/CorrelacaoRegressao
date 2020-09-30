import pandas as pd
from pandas import DataFrame as dt
from estatistica import Correlacao

leitura = pd.read_excel("C:\\Users\\marcelodiana\\Downloads\\cars.xlsx")
#print(leitura)

Horsepower = leitura['Horsepower'].values.tolist()
Weight = leitura['Weight'].values.tolist()
Acceleration = leitura['Acceleration'].values.tolist()
MPG = leitura['MPG'].values.tolist()
Displacement = leitura['Displacement'].values.tolist()

def rota_calculo(x, y):
    if len(x) == len(y):
        instancia = Correlacao()
        return round(instancia.r(x, y),4)
    else:
        pass

print('Correlação(Horsepower, Displacement) = {}'.format(rota_calculo(Horsepower, Displacement)))
print('Correlação(Horsepower, Weight) = {}'.format(rota_calculo(Horsepower, Weight)))
print('Correlação(Horsepower, MPG) = {}'.format(rota_calculo(Horsepower, MPG)))
print('Correlação(Horsepower, Acceleration) = {}'.format(rota_calculo(Horsepower, Acceleration)))
print('Correlação(Displacement, MPG) = {}'.format(rota_calculo(Displacement, MPG)))
