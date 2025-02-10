import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
import numpy as np   # Importa a biblioteca NumPy para operações numéricas

# Configurações do Pandas para melhorar a exibição dos dados no terminal
pd.set_option('display.width', None)  # Permite que o terminal exiba o DataFrame sem quebras de linha automáticas
pd.set_option('display.max_colwidth', None)  # Garante que colunas com textos longos sejam exibidas por completo

# Carrega os dados do arquivo CSV em um DataFrame do Pandas
df = pd.read_csv('./estatistica_de_dados/clientes-v3-preparado.csv')

# Exibe estatísticas descritivas para todas as colunas numéricas do DataFrame
print('Estatisticas do DataFrame:', df.describe())

# Exibe estatísticas descritivas apenas para as colunas 'salario' e 'anos_experiencia'
print('Estatisticas de um campo:', df[['salario', 'anos_experiencia']].describe())

# Calcula e exibe a matriz de correlação entre 'salario' e 'idade' usando o coeficiente de Pearson (padrão)
print('Correlação:', df[['salario', 'idade']].corr())

# Calcula e exibe a correlação entre as versões normalizadas (MinMaxScaler) de 'salario' e 'idade'
print('Correlação com Normalização:', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())

# Calcula e exibe a correlação entre as versões padronizadas (StandardScaler) de 'salario' e 'idade'
print('Correlação com Padronização:', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())

# Calcula e exibe a correlação entre as versões padronizadas usando RobustScaler de 'salario' e 'idade'
print('Correlação com Padronização:', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

# Calcula e exibe a matriz de correlação entre várias variáveis relacionadas à idade e ao salário
print('Correlação:', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())

# Filtra o DataFrame para incluir apenas clientes com idade inferior a 65 anos
df_filtro_idade = df[df['idade'] < 65]

# Calcula e exibe a correlação entre 'salario' e 'idade' apenas para clientes com idade < 65 anos
print('Correlação de clientes menores de 65 anos:', df_filtro_idade[['salario', 'idade']].corr())

# Adiciona uma nova variável ao DataFrame chamada 'variavel_espuria'
# Esta variável cresce sequencialmente de 0 até len(df)-1, simulando um efeito de tendência temporal
df['variavel_espuria'] = np.arange(len(df))

# Exibe os valores da variável espúria criada
print('Varivel espuria:', df['variavel_espuria'].values)

# Calcula a matriz de correlação de Pearson para várias variáveis do DataFrame
pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos']].corr()

# Calcula a matriz de correlação de Spearman para as mesmas variáveis
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos']].corr(method='spearman')

# Exibe os resultados das correlações de Pearson e Spearman
print('Correlação de Pearson:', pearson_corr)
print('Correlação de Spearman:', spearman_corr)