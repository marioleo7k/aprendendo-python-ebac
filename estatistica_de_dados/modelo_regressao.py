import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
from sklearn.model_selection import train_test_split  # Função para dividir os dados em treino e teste
from sklearn.linear_model import LinearRegression  # Classe para criar um modelo de regressão linear
from sklearn.metrics import mean_squared_error, r2_score  # Importa métricas de avaliação do modelo
import joblib  # Biblioteca para salvar e carregar modelos treinados

# Carregar os dados do arquivo CSV
df = pd.read_csv('./estatistica_de_dados/clientes-v3-preparado.csv')

# Corrigir nomes das colunas para evitar erros de digitação ou inconsistências
df.columns = df.columns.str.lower()  # Converte todos os nomes de colunas para minúsculas

# Selecionar as variáveis independentes (X) e a variável dependente (Y)
#X = df[['anos_experiencia']]  # Variável preditora (anos de experiência)
# Caso queira incluir mais variáveis preditoras, utilize a linha abaixo:
X = df[['anos_experiencia', 'nivel_educacao_cod', 'area_atuacao_cod', 'idade']]

Y = df[['salario']]  # Variável alvo (salário)

# Dividir os dados em conjunto de treinamento (80%) e teste (20%)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Criar o modelo de Regressão Linear
modelo_lr = LinearRegression()

# Treinar o modelo com os dados de treinamento
modelo_lr.fit(X_train, Y_train)

# Fazer previsões no conjunto de teste
Y_prev = modelo_lr.predict(X_test)

# Calcular o Coeficiente de Determinação (R²) - mede o quão bem o modelo explica a variável alvo
r2 = r2_score(Y_test, Y_prev)
print(f'\nCoeficiente de Determinação - R²: {r2:.2f}')

# Calcular a Raiz do Erro Quadrático Médio (RMSE) - mede o erro médio das previsões
rmse = mean_squared_error(Y_test, Y_prev) ** 0.5  # Calcula a raiz quadrada do erro quadrático médio
print(f'\nRaiz do Erro Quadrático Médio - RMSE: {rmse:.2f}')

# Exibir o desvio padrão do salário para referência
print(f'\nDesvio Padrão do Campo Salário: {df["salario"].std():.2f}')

# Salvar o modelo treinado em um arquivo para uso futuro
joblib.dump(modelo_lr, './estatistica_de_dados/modelo_regressao_linear.pkl')