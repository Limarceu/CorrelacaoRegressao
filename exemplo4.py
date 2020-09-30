import pandas as pd
from pandas import DataFrame as dt
from Correlacao import Correlacao

leitura = pd.read_excel("datasets\\cars.xlsx")
#print(leitura)

Horsepower = leitura['Horsepower'].values.tolist()
Weight = leitura['Weight'].values.tolist()
Acceleration = leitura['Acceleration'].values.tolist()
MPG = leitura['MPG'].values.tolist()
Displacement = leitura['Displacement'].values.tolist()

relacao1 = Correlacao(Horsepower, Displacement)
relacao2 = Correlacao(Horsepower, Weight)
relacao3 = Correlacao(Horsepower, MPG)
relacao4 = Correlacao(Horsepower, Acceleration)
relacao5 = Correlacao(Displacement, MPG)

print('Correlação(Horsepower, Displacement) = {}'.format(round(relacao1.correlacao_r(),4)))
print('Correlação(Horsepower, Weight) = {}'.format(round(relacao2.correlacao_r(),4)))
print('Correlação(Horsepower, MPG) = {}'.format(round(relacao3.correlacao_r(),4)))
print('Correlação(Horsepower, Acceleration) = {}'.format(round(relacao4.correlacao_r(),4)))
print('Correlação(Displacement, MPG) = {}'.format(round(relacao5.correlacao_r(),4)))

