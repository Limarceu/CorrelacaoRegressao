import pandas as pd
from pandas import DataFrame as dt
from estatistica import Correlacao

leitura = pd.read_excel("C:\\Users\\marcelodiana\\Downloads\\cereal.xlsx")
#print(leitura)

fat = leitura['fat'].values.tolist()
calories = leitura['calories'].values.tolist()
sodium = leitura['sodium'].values.tolist()
potass = leitura['potass'].values.tolist()
protein = leitura['protein'].values.tolist()

def rota_calculo(x, y):
    if len(x) == len(y):
        instancia = Correlacao()
        return round(instancia.r(x, y),4)
    else:
        pass

print('Correlação(fat, calories) = {}'.format(rota_calculo(fat, calories)))
print('Correlação(fat, sodium) = {}'.format(rota_calculo(fat, sodium)))
print('Correlação(sodium, potass) = {}'.format(rota_calculo(sodium, potass)))
print('Correlação(calories, protein) = {}'.format(rota_calculo(calories, protein)))

