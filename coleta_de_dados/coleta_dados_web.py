# Importa o módulo 'requests' para realizar requisições HTTP.
import requests

# Importa a biblioteca 'BeautifulSoup' do módulo 'bs4' para manipular e analisar dados HTML.
from bs4 import BeautifulSoup

# URL da página da Wiki Python Brasil que será acessada.
url = "https://wiki.python.org.br/AprendaMais"

# Realiza uma requisição HTTP GET para a URL e armazena a resposta na variável 'requisicao'.
requisicao = requests.get(url)

# Analisa o conteúdo HTML retornado pela requisição com o parser 'html.parser'.
extracao = BeautifulSoup(requisicao.text, features="html.parser")

# Imprime o texto da página HTML, removendo espaços extras no início e no final.
print(extracao.text.strip())

# Itera por todos os elementos <h2> encontrados no HTML.
for linha_texto in extracao.find_all("h2"):
    # Extrai o texto do elemento <h2>, removendo espaços extras.
    titulo = linha_texto.text.strip()
    # Imprime o título encontrado.
    print("Titulo ", titulo)

# Inicializa contadores para os títulos e parágrafos.
contar_titulos = 0
contar_paragrafos = 0

# Itera por todos os elementos <h2> e <p> encontrados no HTML.
for linha_texto in extracao.find_all(["h2", "p"]):
    # Incrementa o contador de títulos se o elemento for <h2>.
    if linha_texto.name == "h2":
        contar_titulos += 1
    # Incrementa o contador de parágrafos se o elemento for <p>.
    elif linha_texto.name == "p":
        contar_paragrafos += 1

# Imprime o total de títulos encontrados.
print("Total de titulos: ", contar_titulos)

# Imprime o total de parágrafos encontrados.
print("Total de paragrafos: ", contar_paragrafos)

# Itera novamente por todos os elementos <h2> e <p> para exibir o conteúdo.
for linha_texto in extracao.find_all(["h2", "p"]):
    # Se o elemento for <h2>, imprime o título.
    if linha_texto.name == "h2":
        titulo = linha_texto.text.strip()
        print("Titulo: \n", titulo)
    # Se o elemento for <p>, imprime o parágrafo.
    elif linha_texto.name == "p":
        paragrafo = linha_texto.text.strip()
        print("Paragrafo: \n", paragrafo)

# Itera por todos os títulos <h2> encontrados.
for linha_texto in extracao.find_all("h2"):
    # Extrai o texto do título <h2>.
    titulo = linha_texto.text.strip()
    print("\n Titulo:", titulo)
    # Busca os elementos <p> que são irmãos diretos do título <h2>.
    for link in linha_texto.find_next_siblings("p"):
        # Para cada link encontrado dentro dos parágrafos, extrai o texto e o atributo href (URL).
        for a in link.find_all("a", href=True):
            print("Texto Link: ", a.text.strip(), " | URL:", a["href"])
