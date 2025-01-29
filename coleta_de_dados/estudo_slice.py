# Cria uma lista chamada 'texto' contendo números de 1 a 19. A função 'range(1, 20)' gera números de 1 até 19 (o limite superior não é incluído).
texto = list(range(1, 20))

# Cria uma nova lista 'subtexto' que contém os primeiros 11 elementos da lista 'texto' (do índice 0 ao 10, inclusive).
subtexto = texto[:11]
# Imprime o conteúdo da lista 'subtexto', que são os números de 1 a 11.
print(subtexto)

# Cria uma nova lista 'subtexto' com os elementos da lista 'texto' entre os índices 8 e 10 (inclusive). 
# Isso corresponde aos 3 números entre o 9º e o 11º números na lista original.
subtexto = texto[8:11]
# Imprime o conteúdo da lista 'subtexto', que são os números de 9 a 11.
print(subtexto)

# Cria uma nova lista 'subtexto' contendo os últimos 5 elementos da lista 'texto'. 
# O índice negativo -5 começa a contar a partir do final da lista.
subtexto = texto[-5:]
# Imprime o conteúdo da lista 'subtexto', que são os últimos 5 números da lista original.
print(subtexto)
