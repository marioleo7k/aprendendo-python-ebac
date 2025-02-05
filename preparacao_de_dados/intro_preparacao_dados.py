import pandas as pd  # Importando a biblioteca pandas para manipulação de dados

# Lendo o arquivo CSV e criando o DataFrame
df = pd.read_csv('./preparacao_de_dados/clientes-v2.csv')

# Exibindo as primeiras e últimas linhas do DataFrame
print(df.head().to_string())
print(df.tail().to_string())

# Removendo espaços em branco dos nomes das colunas
df.columns = df.columns.str.strip()

# Convertendo a coluna 'data' para o formato datetime
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Exibindo informações iniciais sobre o DataFrame
print('Verificação inicial: \n', df.info())

# Analisando dados nulos
print('Análise de dados nulos: \n', df.isnull().sum())
print('% de dados nulos: \n', df.isnull().mean() * 100)

# Removendo linhas com valores nulos
df.dropna(inplace=True)
print('Confirmação da remoção de dados nulos: \n', df.isnull().sum().sum())

# Analisando dados duplicados
print('Análise de dados duplicados: \n', df.duplicated().sum())

# Removendo dados duplicados
df.drop_duplicates(inplace=True)
print('Confirmação da remoção de dados duplicados: \n', df.duplicated().sum())

# Analisando dados únicos
print('Análise de dados únicos: \n', df.nunique())

# Exibindo estatísticas descritivas dos dados
print('Estatísticas dos dados: \n', df.describe())

# Selecionando colunas específicas
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print('Seleção de colunas: \n', df.head().to_string())

# Salvando o DataFrame tratado em um novo arquivo CSV
df.to_csv('./preparacao_de_dados/clientes-v2-tratados.csv', index=False)