import pandas as pd
from pandas import DataFrame as dt
from estatistica import Correlacao

leitura = pd.read_csv("C:\\Users\\marcelodiana\\Downloads\\TimeUse.csv")
print(leitura.columns(''))

males = leitura['Sleep'].head(14).values.tolist()
females = leitura['Sleep'].tail(14).values.tolist()
print(males)
print(females)
machos = [int((m.split(':'))[0])*60 + int((m.split(':')[1])) for m in males]
femeas = [int((m.split(':'))[0])*60 + int((m.split(':')[1])) for m in females]
print(f'{machos},\n{femeas}')  #convertido em segundos

def rota_calculo(x, y):
    if len(x) == len(y):
        instancia = Correlacao()
        return round(instancia.r(x, y),4)
    else:
        pass

print('Correlação(males, females) = {}'.format(rota_calculo(machos, femeas)))
