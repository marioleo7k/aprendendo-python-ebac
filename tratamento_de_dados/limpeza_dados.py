import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# Ler o arquivo CSV
df = pd.read_csv("./tratamento_de_dados/clientes.csv")  # Lê o arquivo CSV 'clientes.csv' da subpasta especificada e armazena o conteúdo no DataFrame df

print(df.columns)  # Isso vai mostrar todas as colunas presentes no DataFrame

df.columns = df.columns.str.strip()  # Remove espaços extras dos nomes das colunas

# Remover colunas e linhas desnecessárias
df.drop(labels="pais", axis=1, inplace=True)  # Remove a coluna 'pais' (axis=1 indica que é uma coluna) e faz a alteração diretamente no df (inplace=True)
df.drop(labels=2, axis=0, inplace=True)  # Remove a linha com o índice 2 (axis=0 indica que é uma linha) e faz a alteração diretamente no df (inplace=True)

# Normalizar os campos de texto
df["nome"] = df["nome"].str.title()  # Aplica a formatação de título (primeira letra de cada palavra em maiúscula) na coluna 'nome'
df["endereco"] = df["endereco"].str.lower()  # Converte todos os caracteres da coluna 'endereco' para minúsculos
df["estado"] = df["estado"].str.strip().str.upper()  # Remove espaços em branco no início e no final da string da coluna 'estado', e converte para maiúsculas

# Converter tipos de dados
df["idade"] = df["idade"].astype(int)  # Converte os valores da coluna 'idade' para o tipo inteiro (int)

# Tratar valores nulos
df.fillna(value={"estado": "Desconhecido"}, inplace=True)  # Substitui valores nulos na coluna 'estado' por "Desconhecido"
df["endereco"] = df["endereco"].fillna("Endereço não informado")  # Substitui valores nulos na coluna 'endereco' por "Endereço não informado"
df["idade_corrigida"] = df["idade"].fillna(df["idade"].mean())  # Substitui valores nulos na coluna 'idade' pela média dos valores existentes dessa coluna

# Tratar formato de datas
df["data_corrigida"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")  # Converte a coluna 'data' para o formato de data específico, com o formato dia/mês/ano. Caso algum erro ocorra, a célula será preenchida com NaT (Not a Time)

# Verificar se há datas inválidas e tentar corrigi-las
invalid_dates = df["data_corrigida"].isna()
if invalid_dates.any():
    print("Datas inválidas encontradas, tentando corrigir...")
    df.loc[invalid_dates, "data_corrigida"] = pd.to_datetime(df.loc[invalid_dates, "data"], errors="coerce")  # Tenta converter novamente as datas inválidas sem especificar o formato

# Tratar valores duplicados
if "CPF" in df.columns:  # Verifica se a coluna 'CPF' existe no DataFrame
    df.drop_duplicates(subset="CPF", inplace=True)  # Remove as duplicatas da coluna 'CPF' (caso haja registros duplicados)

# Verificar tamanho do DataFrame
print("Quantidade de registros após limpeza:", len(df))  # Exibe o número de registros (linhas) do DataFrame após a limpeza dos dados

# Salvar DataFrame final
df["data"] = df["data_corrigida"]  # Substitui a coluna 'data' pela 'data_corrigida' no DataFrame
df["idade"] = df["idade_corrigida"]  # Substitui a coluna 'idade' pela 'idade_corrigida' no DataFrame

df_salvar = df[["nome", "cpf", "idade", "data", "endereco", "estado"]]  # Cria um novo DataFrame apenas com as colunas relevantes para salvar
df_salvar.to_csv("./tratamento_de_dados/clientes_limpeza.csv", index=False)  # Salva o novo DataFrame 'df_salvar' no arquivo CSV 'clientes_limpeza.csv' na subpasta especificada, sem o índice

print("Novo DataFrame salvo com sucesso:")  # Exibe uma mensagem indicando que o novo DataFrame foi salvo
print(pd.read_csv("./tratamento_de_dados/clientes_limpeza.csv"))  # Lê e exibe o conteúdo do arquivo CSV recém-salvo para verificar se foi salvo corretamente