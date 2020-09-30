import pandas as pd
from pandas import DataFrame as dt
from basecalculos.correlacao import Correlacao

leitura = pd.read_csv("datasets\\TimeUse.csv")

males = leitura['Sleep'].head(14).values.tolist()
females = leitura['Sleep'].tail(14).values.tolist()
machos = [int((m.split(':'))[0])*60 + int((m.split(':')[1])) for m in males]
femeas = [int((m.split(':'))[0])*60 + int((m.split(':')[1])) for m in females]
print(f'{machos},\n{femeas}')  #convertido em segundos

relacao_sono = Correlacao(machos, femeas)

print('Correlação_sono(males, females) = {}'.format(relacao_sono.correlacao_r()))

