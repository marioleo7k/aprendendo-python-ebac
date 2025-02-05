# Importando bibliotecas
import pandas as pd # Biblioteca para manipulação de dados
from sklearn.preprocessing import LabelEncoder # Biblioteca para pré-processamento de dados

## Carregando os dados
df = pd.read_csv('./preparacao_de_dados/clientes-v2-tratados.csv') # Carregando o DataFrame
pd.set_option('display.width', None) # Para não truncar colunas e mostrar todo o DataFrame
pd.set_option('display.max_colwidth', None) # Para não truncar colunas e mostrar todo o DataFrame
print('\nColunas do DataFrame\n',df.columns) # Exibindo as colunas do DataFrame
print('\nComeço do DataFrame\n', df.head()) # Exibindo as primeiras linhas do DataFrame

## Modelando os Dados
df.columns = df.columns.str.strip() # Removendo espaços em branco nas colunas

## Codificando variáveis categóricas
# Codificação One-Hot para 'estado_civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1) # Codificando variável categórica
print('\nDataFrame após codificação One-Hot para a variável "estado_civil"\n:', df.head()) # Exibindo as primeiras linhas do DataFrame

# Codificação ordinal com dicionários para 'nivel_educacao'
educacao_ordem = {'ensino_fundamental': 1, 'ensino_medio': 2, 'graduacao': 3, 'pos_graduacao': 4} # Definindo a ordem das categorias
df['nivel_educacao_ord'] = df['nivel_educacao'].map(educacao_ordem) # Mapeando a ordem das categorias
print('\nDataFrame após codificação ordinal para a variável "nivel_educacao"\n:', df.head()) # Exibindo as primeiras linhas do DataFrame

# Codificaçção ordinal com cat.codes para 'area_atuacao'
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes # Codificando variável categórica
print('\nDataFrame após codificação ordinal para a variável "area_atuacao"\n:', df.head()) # Exibindo as primeiras linhas do DataFrame

# Codificação com LabelEndoder para 'estado'
label_encoder = LabelEncoder() # Instanciando o objeto LabelEncoder
df['estado_cod'] = label_encoder.fit_transform(df['estado']) # Codificando variável categórica
print('\nDataFrame após codificação com LabelEncoder para a variável "estado"\n:', df.head()) # Exibindo as primeiras linhas do DataFrame