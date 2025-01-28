import pandas as pd

# Carrega o arquivo CSV na mesma pasta que o script (Não precisamos fazer um DataFrame manualmente pois o "read_csv" já é um df)
df = pd.read_csv("./introducao_tratamento_dados/clientes.csv")

# Verifica os primeiros registros usando sintaxe do python
print("TOP5 Linhas da DF \n:", df[:6])

# Verifica os primeiros registros usando sintaxe do pandas
print("Primeiros registros \n:", df.head(6).to_string)

# Verifica os últimos registros usando sintaxe do python
print("TOP5 Linhas da DF \n:", df[6:])

# Verifica os últimos registros usando sintaxe do pandas
print("Primeiros registros \n:", df.tail(6).to_string)

# Verifica a quantidade de linhas e colunas
print("Quantide de linhas e colunas do DF:", df.shape)

# Verifica a tipagem dos dados do dataframe
print("Tipo de dados da DF \n:", df.dtypes)

# Verifica e checa valores nulos do dataframe
print("Quantidade de valores nulos \n:", df.isnull().sum())

