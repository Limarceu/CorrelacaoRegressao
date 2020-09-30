from bases_calculos.Correlacao import Correlacao
from bases_calculos.Regressao import Inclinacao
from bases_calculos.Interceptacao import Interceptacao
import pandas as pd

#path caminho de entrada de arquivo para leitura de dataset
caminho = 'datasets\\'
leitura = pd.read_csv(caminho + 'filename.csv')
'''Por opção para visualizar as colunas do dataset escolhido, print(leitura.head(2))'''

'''convertendo uma coluna em uma lista'''
coluna_1 = leitura['nome_coluna_1'].values.tolist()
coluna_2 = leitura['nome_coluna_2'].values.tolist()

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
interceptacao_b = intercep_observada.Interceptacao_b()
print('Interceptação_b = {}'.format(round(interceptacao_b, 4)))

