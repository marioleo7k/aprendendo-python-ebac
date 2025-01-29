# Importa a biblioteca 'requests' para realizar requisições HTTP.
import requests

# Função para enviar um arquivo para o serviço file.io sem chave de acesso.
def enviar_arquivo():
    # Caminho do arquivo a ser enviado. Substitua pelo caminho do arquivo real.
    caminho = ""  # Exemplo: "C:/caminho/arquivo.xlsx"

    try:
        # Envia o arquivo usando uma requisição POST para o serviço file.io.
        with open(caminho, "rb") as arquivo:
            requisicao = requests.post(url="https://file.io", files={"file": arquivo})
        
        # Converte a resposta da requisição para JSON.
        saida_requisicao = requisicao.json()

        # Exibe a resposta da requisição.
        print(saida_requisicao)

        # Obtém o link de acesso do arquivo enviado.
        url = saida_requisicao.get("link")
        if url:
            print("Arquivo enviado. Link para acesso:", url)
        else:
            print("Erro ao enviar o arquivo:", saida_requisicao)
    except Exception as e:
        print("Erro ao enviar arquivo:", e)

# Função para enviar um arquivo com chave de acesso (API Key).
def enviar_arquivo_chave():
    # Caminho do arquivo e chave de acesso. Substitua pelos valores reais.
    caminho = ""  # Exemplo: "C:/caminho/arquivo.xlsx"
    chave_acesso = ""  # Exemplo: "sua_api_key"

    try:
        # Envia o arquivo com a chave de acesso usando uma requisição POST.
        with open(caminho, "rb") as arquivo:
            requisicao = requests.post(
                url="https://file.io",
                files={"file": arquivo},
                headers={"Authorization": chave_acesso}
            )

        # Converte a resposta da requisição para JSON.
        saida_requisicao = requisicao.json()

        # Exibe a resposta da requisição.
        print(saida_requisicao)

        # Obtém o link de acesso do arquivo enviado.
        url = saida_requisicao.get("link")
        if url:
            print("Arquivo enviado com chave. Link para acesso:", url)
        else:
            print("Erro ao enviar o arquivo:", saida_requisicao)
    except Exception as e:
        print("Erro ao enviar arquivo com chave:", e)

# Função para baixar um arquivo a partir de uma URL fornecida.
def receber_arquivo(file_url):
    try:
        # Faz uma requisição GET para baixar o arquivo da URL fornecida.
        requisicao = requests.get(file_url)

        # Verifica se a requisição foi bem-sucedida.
        if requisicao.ok:
            # Salva o conteúdo baixado como um arquivo local.
            with open("arquivo_baixado.xlsx", "wb") as file:
                file.write(requisicao.content)
            print("Arquivo baixado com sucesso.")
        else:
            print("Erro ao baixar o arquivo:", requisicao.json())
    except Exception as e:
        print("Erro ao baixar o arquivo:", e)

# Chama as funções (substitua os valores dos parâmetros antes de usar).
# enviar_arquivo()
# enviar_arquivo_chave()
# receber_arquivo("URL_DO_ARQUIVO")