# Importando as bibliotecas necessárias
import pandas as pd  # Biblioteca para manipulação de dados tabulares
import numpy as np   # Biblioteca para cálculos numéricos e estatísticos

# Configurando opções de exibição do Pandas para melhorar a visualização dos dados
pd.set_option('display.max_colwidth', None)  # Exibe o conteúdo completo das colunas sem truncamento
pd.set_option('display.width', None)  # Permite a exibição completa do DataFrame sem quebras de linha automáticas

# Carregando o DataFrame a partir de um arquivo CSV
df = pd.read_csv('./estatistica_de_dados/clientes-v3-preparado.csv')

# Exibindo o DataFrame completo
print(df)

# Cálculo de estatísticas básicas usando Pandas
print('Estatísticas com Pandas')

# Calcula e exibe a média da coluna 'salario'
print('Média:', df['salario'].mean())

# Calcula e exibe a mediana da coluna 'salario'
print('Mediana:', df['salario'].median())

# Calcula e exibe a variância da coluna 'salario'
print('Variância:', df['salario'].var())

# Calcula e exibe o desvio padrão da coluna 'salario'
print('Desvio Padrão:', df['salario'].std())

# Calcula e exibe a moda da coluna 'salario' (o valor que mais se repete)
print('Moda:', df['salario'].mode()[0])

# Calcula e exibe o valor mínimo da coluna 'salario'
print('Mínimo:', df['salario'].min())

# Calcula e exibe o valor máximo da coluna 'salario'
print('Máximo:', df['salario'].max())

# Calcula e exibe os quartis (25%, 50% e 75%) da coluna 'salario'
print('Quartis:', df['salario'].quantile([0.25, 0.5, 0.75]))

# Conta e exibe a quantidade de valores não nulos na coluna 'salario'
print('Contagem de valores não nulos:', df['salario'].count())

# Calcula e exibe a soma total dos valores na coluna 'salario'
print('Soma:', df['salario'].sum())

# Trabalhando com a estrutura de dados do DataFrame
# Exibe a série Pandas correspondente à coluna 'salario'
print('Coluna do DataFrame:', df['salario'])

# Exibe os valores da coluna 'salario' como um array NumPy
print('Array do campo:', df['salario'].values)

# Cálculo de estatísticas usando Numpy
print('Estatísticas com Numpy:')

# Calcula e exibe a média usando Pandas
print('Média com coluna:', np.mean(df['salario']))

# Calcula e exibe a média usando o array NumPy extraído do DataFrame
print('Média com array:', np.mean(df['salario'].values))

# Criando um array NumPy para facilitar as operações estatísticas
array_campo = df['salario'].values

# Calcula e exibe a mediana usando NumPy
print('Mediana:', np.median(array_campo))

# Calcula e exibe a variância usando NumPy
print('Variância:', np.var(array_campo))

# Calcula e exibe o desvio padrão usando NumPy
print('Desvio Padrão:', np.std(array_campo))

# Calcula e exibe o valor mínimo usando NumPy
print('Mínimo:', np.min(array_campo))

# Calcula e exibe o valor máximo usando NumPy
print('Máximo:', np.max(array_campo))

# Calcula e exibe os quartis (25%, 50% e 75%) usando NumPy
print('Quartis:', np.quantile(array_campo, q=[0.25, 0.5, 0.75]))

# Calcula e exibe os percentis 25%, 50% e 75% usando NumPy
print('Porcentagem 25%, 50% e 75%:', np.percentile(array_campo, q=[25, 50, 75]))

# Conta e exibe a quantidade de valores não zero no array
print('Contagem de valores não zeros:', np.count_nonzero(array_campo))

# Calcula e exibe a soma total dos valores no array
print('Soma:', np.sum(array_campo))