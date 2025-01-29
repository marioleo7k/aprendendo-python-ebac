# Importa a biblioteca pandas para manipulação de dados.
import pandas as pd

# Lista de nomes para exemplificação.
lista_nomes = ["Ana", "Maria", "Nicolle"]
print("Lista de nomes: \n", lista_nomes)

# Exibe o primeiro elemento da lista.
print("Primeiro Elemento da Lista: \n", lista_nomes[0])

# Dicionário representando atributos de uma pessoa.
dicionario_pessoa = {
    "nome": "Ana",
    "idade": 21,
    "cidade": "São Paulo"
}
print("Dicionário de uma pessoa: \n", dicionario_pessoa)

# Acessa o atributo 'nome' do dicionário usando o método 'get'.
print("Atributo de uma pessoa: \n", dicionario_pessoa.get("nome"))

# Lista de dicionários representando várias pessoas.
dados = [
    {"nome": "Ana", "idade": 20, "cidade": "São Paulo"},
    {"nome": "Lucas", "idade": 56, "cidade": "Cotia"},
    {"nome": "Rafaela", "idade": 12, "cidade": "Belo Horizonte"},
]

# Cria um DataFrame (tabela) com os dados.
df = pd.DataFrame(dados)
print("DataFrame:\n", df)

# Exibe somente a coluna 'nome'.
print("\nColuna 'nome':\n", df["nome"])

# Exibe as colunas 'nome' e 'cidade'.
print("\nColunas 'nome' e 'cidade':\n", df[["nome", "cidade"]])

# Exibe a primeira linha do DataFrame usando `iloc`.
print("\nPrimeira linha: \n", df.iloc[0])

# Adiciona uma nova coluna 'salario' ao DataFrame.
df["salario"] = ["4100", "2200", "15000"]

# Adiciona uma nova linha ao DataFrame com o método `loc`.
df.loc[len(df)] = {
    "nome": "João",
    "idade": 30,
    "cidade": "João Pessoa",
    "salario": "1500"
}
print("\nDataFrame Atual:\n", df)

# Remove a coluna 'salario' do DataFrame.
df.drop(labels="salario", axis=1, inplace=True)

# Aplica um filtro para selecionar pessoas com idade maior ou igual a 30.
# Converte a coluna 'idade' para inteiro antes de filtrar.
df["idade"] = df["idade"].astype(int)
filtro_idade = df[df["idade"] >= 30]
print("\nFiltro (idade >= 30):\n", filtro_idade)

# Salva o DataFrame em um arquivo CSV.
df.to_csv(path_or_buf="dados.csv", index=False)

# Lê o arquivo CSV salvo anteriormente.
df_lido = pd.read_csv("dados.csv")
print("\nLeitura do CSV:\n", df_lido)