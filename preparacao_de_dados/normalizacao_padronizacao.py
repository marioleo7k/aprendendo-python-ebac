# Blibliotecas
import pandas as pd # Biblioteca para manipulação de dados
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler # biblioteca para normalização e padronização

pd.set_option('display.width', None) # Define a largura máxima do terminal
pd.set_option('display.max_colwidth', None) # Define a largura máxima da coluna

df = pd.read_csv('./preparacao_de_dados/clientes-v2-tratados.csv') # Carrega o dataset

df.columns = df.columns.str.strip() # Remove espaços em branco dos nomes das colunas

print(df.head()) # Exibe as primeiras linhas do dataset
print(df.columns) # Exibe as colunas do dataset

df = df[['idade', 'salario']] # Define as colunas que serão utilizadas

# Instancia os padronizadores e normalizadores
robust_scaler = RobustScaler()
minmax_scaler = MinMaxScaler()
minmax_scaler_mm = MinMaxScaler(feature_range=(-1, 1))
standard_scaler = StandardScaler()

# Aplica as transformações
df['idadeRobustScaler'] = robust_scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = robust_scaler.fit_transform(df[['salario']])

df['idadeMinMaxScaler'] = minmax_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = minmax_scaler.fit_transform(df[['salario']])

df['idadeMinMaxScaler_mm'] = minmax_scaler_mm.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = minmax_scaler_mm.fit_transform(df[['salario']])

df['idadeStandardScaler'] = standard_scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = standard_scaler.fit_transform(df[['salario']])

print(df.head(15)) # Exibe as primeiras linhas do dataset

print('MinMaxScaler (de 0 a 1):')
print('Idade - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler'].min(), df['idadeMinMaxScaler'].max(), df['idadeMinMaxScaler'].std()))
print('Salário - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler'].min(), df['salarioMinMaxScaler'].max(), df['salarioMinMaxScaler'].std()))

print('MinMaxScaler (de -1 a 1):')
print('Idade - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['idadeMinMaxScaler_mm'].min(), df['idadeMinMaxScaler_mm'].max(), df['idadeMinMaxScaler_mm'].std()))
print('Salário - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['salarioMinMaxScaler_mm'].min(), df['salarioMinMaxScaler_mm'].max(), df['salarioMinMaxScaler_mm'].std()))

print('StandardScaler (Ajuste a média a 0 e desvio padrão a 1):')
print('Idade - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['idadeStandardScaler'].min(), df['idadeStandardScaler'].max(), df['idadeStandardScaler'].std()))
print('Salário - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['salarioStandardScaler'].min(), df['salarioStandardScaler'].max(), df['salarioStandardScaler'].std()))

print('RobustScaler (Ajuste a mediana e IQR):')
print('idade - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['idadeRobustScaler'].min(), df['idadeRobustScaler'].max(), df['idadeRobustScaler'].std()))
print('salario - Min: {:.4f} Max: {:.4f} Std: {:.4f}'.format(df['salarioRobustScaler'].min(), df['salarioRobustScaler'].max(), df['salarioRobustScaler'].std()))