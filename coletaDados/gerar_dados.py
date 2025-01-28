# Bibliotecas
import pandas as pd
import random
from faker import Faker

# Dados brasileiros
faker = Faker("pt_BR")

# Lista de dados pessoais
dados_pessoais = []

# 10 dados pessoais usando faker/random
for _ in range(10):

    nome = faker.name()
    cpf = faker.cpf()
    endereço = faker.address()
    estado = faker.state()
    pais = "Brasil"
    idade = random.randint(18, 89) # Idade mín é 18 anos, Idade máx é 89 anos
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y") 

# Dicionário sobre a estrutura de pessoa    
    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "endereço": endereço,
        "estado": estado,
        "pais": pais,
        "idade": idade,
        "data": data
    }

# Adiciona os dados de pessoa para a lista dados pessoais
    dados_pessoais.append(pessoa)

# DataFrame usando pandas para visualizar a lista dados pessoais
df_pessoas = pd.DataFrame(dados_pessoais)
print("Dados pessoais fakes \n", df_pessoas)

# Exporta em formato .csv a lista dados pessoais
df_pessoas.to_csv("dados_fake.csv", index= False)
