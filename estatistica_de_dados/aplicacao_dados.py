import pandas as pd
import joblib
import os

# Configurações do pandas
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

# Caminho dos arquivos
csv_path = './estatistica_de_dados/clientes-v3-preparado.csv'
model_path_linear = './estatistica_de_dados/modelo_regressao_linear.pkl'
model_path_logistica = './estatistica_de_dados/modelo_regressao_logistica.pkl'

# Verificar se os arquivos existem
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

if not os.path.exists(model_path_linear):
    raise FileNotFoundError(f"Modelo de regressão linear não encontrado: {model_path_linear}")

if not os.path.exists(model_path_logistica):
    raise FileNotFoundError(f"Modelo de regressão logística não encontrado: {model_path_logistica}")

# Carregar os dados
df = pd.read_csv(csv_path)

# Verificar valores nulos
if df.isnull().sum().sum() > 0:
    print("Aviso: Existem valores nulos no conjunto de dados!")
    df = df.fillna(0)  # ou alguma outra estratégia de tratamento

# Carregar modelos
modelo_regressao_linear = joblib.load(model_path_linear)
modelo_regressao_logistica = joblib.load(model_path_logistica)

# Novos dados para previsão
dados_novos_funcionarios = pd.DataFrame({
    'idade': [35, 45, 30],
    'anos_experiencia': [6, 12, 5],
    'nivel_educacao_cod': [2, 3, 4],
    'area_atuacao_cod': [1, 4, 3],
})

# Verificar se as colunas dos dados novos correspondem às do modelo treinado
if set(dados_novos_funcionarios.columns) != set(df.columns):
    raise ValueError("As colunas dos dados novos não correspondem às do modelo treinado!")

# Fazer previsões
try:
    salario_previsto = modelo_regressao_linear.predict(dados_novos_funcionarios)
    categoria_salario = modelo_regressao_logistica.predict(dados_novos_funcionarios)

    for i, salario in enumerate(salario_previsto):
        print(f'Salário previsto para o funcionário {i+1}: R$ {salario:.2f}')

    for i, categoria in enumerate(categoria_salario):
        print(f'Categoria salarial prevista para o funcionário {i+1}: {categoria}')
except Exception as e:
    print(f"Erro ao realizar previsões: {e}")