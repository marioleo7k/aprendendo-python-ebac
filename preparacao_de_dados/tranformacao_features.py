# Bibliotecas necessárias
import pandas as pd # Biblioteca para manipulação de dados
import numpy as np # Biblioteca para manipulação de vetores e matrizes
from scipy import stats as ss # Bilbioteca para estatística

## Extração de dados
df = pd.read_csv('./preparacao_de_dados/clientes-v2-tratados.csv') # Importar DataFrame
pd.set_option('display.width', None) # Configuração para exibir o DataFrame
pd.set_option('display.max_columns', None) # Configuração para exibir o DataFrame
print('\nMostrar a quantidade de colunas do DataFrame:\n', df.columns) # Exibir as colunas do DataFrame
print('\nMostrar as primeiras linhas do DataFrame:\n', df.head()) # Exibir as primeiras linhas do DataFrame

## Modelagem de Dados
df.columns = df.columns.str.strip() # Remover espaços em branco

## Engenharia de Features
# Transformação logarítmica
df['salario_log'] = np.log1p(df['salario']) # Aplicar a transformação logarítmica
print('\nMostrar as primeiras linhas do DataFrame com a transformação logarítmica:\n', df.head()) # Exibir as primeiras linhas do DataFrame

# Transformação Box-Cox
df['salario_boxcox'] , _ = ss.boxcox(df['salario'] + 1) # Aplicar a transformação Box-Cox
print('\nMostrar as primeiras linhas do DataFrame com a transformação Box-Cox:\n', df.head()) # Exibir as primeiras linhas do DataFrame

# Codificação de frequência para 'estado'
estado_freq = df['estado'].value_counts() / len(df) # Calcular a frequência de estados
df['estado_freq'] = df['estado'].map(estado_freq) # Aplicar a codificação de frequência
print('\nMostrar as primeiras linhas do DataFrame com a codificação de frequência para estado:\n', df.head()) # Exibir as primeiras linhas do DataFrame

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos'] # Criar a interação entre idade e número de filhos 
print('\nMostrar as primeiras linhas do DataFrame com a interação entre idade e número de filhos:\n', df.head()) # Exibir as primeiras linhas do DataFrame