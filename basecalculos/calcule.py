from correlacao import Correlacao
from regressao import Inclinacao
from interceptacao import Interceptacao
import pandas as pd

#path caminho de entrada de arquivo para leitura de dataset
caminho = 'datasets\\'
leitura = pd.read_excel(caminho + 'sampleData.xlsx')
'''Por opção para visualizar as colunas do dataset escolhido, print(leitura.head(2))'''

'''convertendo uma coluna em uma lista'''
coluna_1 = leitura['Text_Messages_Sent_Yesterday'].values.tolist()
coluna_2 = leitura['Text_Messages_Received_Yesterday'].values.tolist()

'''Correlação'''
correlacao_observada = Correlacao(coluna_1, coluna_2)
correlacao = correlacao_observada.correlacao_r()
print('Correlação = {}'.format(round(correlacao,4)))

'''Inclinacao'''
inclinacao_observada = Inclinacao(coluna_1, coluna_2)
inclinacao = inclinacao_observada.coeficiente_angular()
print('Inclinação_m = {}'.format(round(inclinacao, 4)))

'''Interceptação'''
intercep_observada = Interceptacao(coluna_1, coluna_2)
interceptacao_b = intercep_observada.interceptacao_b()
print('Interceptação_b = {}'.format(round(interceptacao_b, 4)))

'''Mostra a equação da reta'''
print('==================')
print('y = {}*x + ({})'.format(round(inclinacao,3), round(interceptacao_b,3)))
print('==================')

xm, ym = 11.5, 320.5
sx , sy = 1.1, 18.2
r = 0.92
m = r*sy/sx
b = ym - m*xm
x = 16
print('y = {}x + ({})'.format(round(m, 2), round(b, 2)))
y = m*x +b
print(round(y,2))
