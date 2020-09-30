import pandas as pd
from pandas import DataFrame as dt
from estatistica import Correlacao

leitura = pd.read_csv("C:\\Users\\marcelodiana\\Downloads\\forestfires.csv")

wind = leitura['wind'].values.tolist()
temp = leitura['temp'].values.tolist()
area = leitura['area'].values.tolist()

if len(wind) == len(area):
    a = Correlacao()
    print('Correlação(wind, area) = {}'.format(a.r(wind, area)))
    print('Correlação(wind, area) = {}'.format(round(a.r(wind, area),3)))
else:
    pass

if len(temp) == len(area):
    a = Correlacao()
    print('Correlação(temp, area) = {}'.format(a.r(temp, area)))
    print('Correlação(temp, area) = {}'.format(round(a.r(temp, area),3)))
else:
    pass

if len(temp) == len(wind):
    a = Correlacao()
    print('Correlação(temp, wind) = {}'.format(a.r(temp, wind)))
    print('Correlação(temp, wind) = {}'.format(round(a.r(temp, wind),3)))
else:
    pass