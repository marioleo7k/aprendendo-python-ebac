import pandas as pd

# Função para calcular o cudo de um número (ele elevado a 3)
# 1 forma usando sintaxe do Python

def elevado_cubo(x):
    return x ** 3

# 2 forma usando sintaxe do pandas, função lambda

eleva_cubo_lambda = lambda x: x ** 3

# Mostrar calculo da primeira forma
print("1 forma", elevado_cubo(2))

# Mostrar calculo da segunda forma
print("2 forma", eleva_cubo_lambda(3))

# Dataframe para testar a função
df = pd.DataFrame({"numeros" : [2, 5, 6, 10, 21, 13]})

# coluna criada da função do cubo quando usamos a def elevado_cubo (esse método não é o melhor pois estamos consumindo 2 linhas do código usando um def quando podemos dar apply direto usando lambda)
df["cubo_funcao"] = df["numeros"].apply(elevado_cubo)

# coluna criada da função do cubo quando usamos o lambda direto no apply do DataFrame (Esse é o melhor método pois economizamos linhas definindo funções e aplicamos cálculos restritos a algum paramêtro)
df["cubo_lambda"] = df["numeros"].apply(lambda x: x ** 3)

print(df)

