import pandas as pd
from pandas import DataFrame as dt
from basecalculos.correlacao import Correlacao

leitura = pd.read_csv("datasets\\forestfires.csv")

wind = leitura['wind'].values.tolist()
temp = leitura['temp'].values.tolist()
area = leitura['area'].values.tolist()

relacao1 = Correlacao(wind, area)
relacao2 = Correlacao(temp, area)
relacao3 = Correlacao(temp, wind)

print('Correlação(wind, area) = {}'.format(round(relacao1.correlacao_r(),4)))
print('Correlação(temp, area) = {}'.format(round(relacao2.correlacao_r(),4)))
print('Correlação(temp, wind) = {}'.format(round(relacao3.correlacao_r(),4)))
