import pandas as pd
from pandas import DataFrame as dt
from Correlacao import Correlacao

leitura = pd.read_excel("datasets\\cereal.xlsx")
#print(leitura)

fat = leitura['fat'].values.tolist()
calories = leitura['calories'].values.tolist()
sodium = leitura['sodium'].values.tolist()
potass = leitura['potass'].values.tolist()
protein = leitura['protein'].values.tolist()

#instancia1 = Correlacao(x,y).correlacao_r()
#print(instancia1)
c1 = Correlacao(fat, calories)
c2 = Correlacao(fat, sodium)
c3 = Correlacao(sodium, potass)
c4 = Correlacao(calories, protein)

print('Correlação(fat, calories) = {}'.format(c1.correlacao_r()))
print('Correlação(fat, sodium) = {}'.format(c2.correlacao_r()))
print('Correlação(sodium, potass) = {}'.format(c3.correlacao_r()))
print('Correlação(calories, protein) = {}'.format(c4.correlacao_r()))

