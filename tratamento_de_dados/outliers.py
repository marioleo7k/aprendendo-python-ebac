# Bibliotecas necessárias
import pandas as pd # Para manipulação de dataframes
from scipy import stats # Para cálculos estatísticos

pd.set_option('display.width', None) # Para visualizar todas as colunas do dataframe

df = pd.read_csv("./tratamento_de_dados/clientes_limpeza.csv") # Importando o dataframe

df_filtro_basico = df[df["idade"] > 100] # Filtrando os valores de idade maiores que 100

print("Filtro básico: \n", df_filtro_basico[["nome", "idade"]]) # Exibindo o filtro básico

print("Quantidade de pessoas com idade maior que 100: \n", df_filtro_basico.shape[0]) # Exibindo a quantidade de pessoas com idade maior que 100

# Identificar outlier com Z-Score
z_scores = stats.zscore(df["idade"].dropna()) # Calculando o Z-score para a coluna "idade", removendo valores nulos
outlier_z = df[z_scores >= 3] # Filtrando os valores de idade com Z-Score maior ou igual a 3
print("Outliers com Z-Score: \n", outlier_z[["nome", "idade"]]) # Exibindo os outliers com Z-Score

# Filtrar outliers com Z-Score em 1 linha
df_zscore = df[stats.zscore(df["idade"]) < 3] # Filtrando os valores de idade com Z-Score menor que 3

# Identificar outlier com IQR
Q1 = df["idade"].quantile(0.25) # Calculando o primeiro quartil (Q1)
Q3 = df["idade"].quantile(0.75) # Calculando o terceiro quartil (Q3)
IQR = Q3 - Q1 # Calculando o intervalo interquartil (IQR)

limite_baixo = Q1 - 1.5 * IQR # Calculando o limite inferior
limite_alto = Q3 + 1.5 * IQR # Calculando o limite superior

print("Limites IQR: ", limite_baixo, limite_alto) # Exibindo os limites IQR

outliers_iqr = df[(df["idade"] < limite_baixo) | (df["idade"] > limite_alto)] # Filtrando os valores de idade fora dos limites IQR
print("Outliers com IQR: \n", outliers_iqr[["nome", "idade"]]) # Exibindo os outliers com IQR
print("Quantidade de outliers com IQR: ", outliers_iqr.shape[0]) # Exibindo a quantidade de outliers com IQR

# Filtrar outliers com IQR em 1 linha
df_iqr = df[(df["idade"] >= limite_baixo) & (df["idade"] <= limite_alto)] # Filtrando os valores de idade dentro dos limites IQR

# Filtrar endereços inválidos
df["endereco"] = df["endereco"].apply(lambda x: "Endereço inválido" if len(x.split("\n")) < 3 else x) # Marcando endereços inválidos

# Tratar campos de texto
df["nome"] = df["nome"].apply(lambda x: "Nome Inválido" if isinstance(x, str) and len(x) > 50 else x) # Marcando nomes inválidos
print("Quantidade de registros com nomes grandes: \n", df[df["nome"] == "Nome Inválido"].shape[0]) # Exibindo a quantidade de registros com nomes inválidos

print("Dados com outliers tratados: \n", df) # Exibindo o dataframe com os outliers tratados

df.to_csv("./tratamento_de_dados/clientes_outliers.csv", index=False) # Salvando o dataframe com os outliers tratados