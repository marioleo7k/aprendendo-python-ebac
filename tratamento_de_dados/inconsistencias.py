# Carregando as bibliotecas
import pandas as pd # Biblioteca para manipulação de dados
import numpy as np # Biblioteca para manipulação de vetores e matrizes

pd.set_option("display.width", None) # Definindo a largura do display
pd.set_option("display.max_columns", None) # Definindo a quantidade máxima de colunas a ser exibida

df = pd.read_csv("./tratamento_de_dados/clientes_outliers.csv") # Carregando o dataset

print(df.head()) # Exibindo as primeiras linhas do dataset

# Corrigir datas de nascimento
df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d", errors="coerce") # Convertendo a coluna data para o formato datetime

data_atual = pd.to_datetime("today") # Obtendo a data atual
df["data_atualizada"] = df["data"].where(df["data"] <= data_atual, pd.NaT) # Corrigindo datas de nascimento
df["idade_ajustada"] = data_atual.year - df["data_atualizada"].dt.year # Calculando a idade
df["idade_ajustada"] -= ((data_atual.month < df["data_atualizada"].dt.month) | ((data_atual.month == df["data_atualizada"].dt.month) & (data_atual.day < df["data_atualizada"].dt.day))).astype(int) # Corrigindo a idade
df.loc[df["idade_ajustada"] > 100, "idade_ajustada"] = np.nan # Corrigindo a idade com valores nulos

# Corrigir campo com múltiplas informações
df["endereco_curto"] = df["endereco"].apply(lambda x: x.split("\n")[0].strip() if pd.notnull(x) else "Endereço Inválido") # Corrigindo o campo endereço
df["bairro"] = df["endereco"].apply(lambda x: x.split("\n")[1].strip() if pd.notnull(x) and len(x.split("\n")) > 1 else "Desconhecido") # Corrigindo o campo bairro
df["estado_sigla"] = df["endereco"].apply(lambda x: x.split(" / ")[-1].strip() if pd.notnull(x) and len(x.split("\n")) > 1 else "Desconhecido") # Corrigindo o campo estado

# Verificando a formatação do campo do endereço
df["endereco_curto"] = df["endereco_curto"].apply(lambda x: "Endereço Inválido" if len(x) > 50 or len(x) < 5 else x) # Corrigindo o campo endereço

# Corrigir dados errôneos
df["cpf"] = df["cpf"].apply(lambda x: x if len(x) == 14 else "CPF Inválido") # Corrigindo o campo CPF

# Lista de estados do Brasil
estados_br = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"] # Lista com as siglas dos estados brasileiros
df["estado_sigla"] = df["estado_sigla"].str.upper().apply(lambda x: x if x in estados_br else "Estado Inválido") # Corrigindo o campo estado

print("Dados tratados com sucesso: \n", df.head()) # Exibindo as primeiras linhas do dataset tratado

df["idade"] = df["idade_ajustada"] # Atribuindo a coluna idade_ajustada a coluna idade
df["endereco"] = df["endereco_curto"] # Atribuindo a coluna endereco_curto a coluna endereco
df["estado"] = df["estado_sigla"] # Atribuindo a coluna estado_sigla a coluna estado
df_salvar = df[['nome', 'cpf', 'idade', 'endereco', 'bairro', 'estado', 'data']] # Selecionando as colunas a serem salvas
df_salvar.to_csv("./tratamento_de_dados/clientes_tratados.csv", index=False) # Salvando o dataset tratado

print("Dados salvos com sucesso! \n", pd.read_csv("./tratamento_de_dados/clientes_tratados.csv").head()) # Exibindo o dataset tratado