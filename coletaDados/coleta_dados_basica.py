# Importa o módulo 'requests' para realizar requisições HTTP e obter dados da web.
import requests

# Importa a biblioteca 'BeautifulSoup' do módulo 'bs4', que facilita a análise e manipulação de dados HTML.
from bs4 import BeautifulSoup

# Importa a biblioteca 'pandas', que é usada para análise de dados e manipulação de tabelas.
import pandas as pd

# Exibe uma mensagem indicando que a requisição HTTP está sendo feita.
print("Request:   ")

# Faz uma requisição GET para o URL fornecido, que contém informações históricas do índice Bovespa no site Yahoo Finanças.
response = requests.get("https://br.financas.yahoo.com/quote/%5EBVSP/history/")

# Imprime os primeiros 6000 caracteres do conteúdo HTML retornado pela página.
print(response.text[:6000])

# Exibe uma mensagem indicando que os dados serão processados com a biblioteca BeautifulSoup.
print("BeautifulSoup:")

# Analisa o conteúdo HTML retornado pela requisição usando o parser "html.parser" e cria um objeto 'soup'.
soup = BeautifulSoup(response.text, features="html.parser")

# Imprime os primeiros 1000 caracteres do conteúdo HTML formatado de maneira mais legível.
print(soup.prettify()[:1000])

# Exibe uma mensagem indicando que os dados serão extraídos e processados com a biblioteca Pandas.
print("Pandas: ")

# Usa a função 'read_html' do Pandas para extrair tabelas diretamente do URL fornecido. 
# O resultado é uma lista de DataFrames, onde cada DataFrame corresponde a uma tabela encontrada na página.
url_dados = pd.read_html("https://br.financas.yahoo.com/quote/%5EBVSP/history/")

# Imprime as primeiras 10 linhas da primeira tabela encontrada na página.
print(url_dados[0].head(10))