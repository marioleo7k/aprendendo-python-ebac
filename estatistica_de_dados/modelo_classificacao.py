# Importa as bibliotecas necessárias
import pandas as pd  # Para manipulação de dados
from sklearn.model_selection import train_test_split  # Para dividir os dados em treino e teste
from sklearn.linear_model import LogisticRegression  # Modelo de Regressão Logística
from sklearn.tree import DecisionTreeClassifier  # Modelo de Árvore de Decisão
from sklearn.metrics import accuracy_score, precision_score, recall_score  # Métricas de avaliação
import joblib  # Para salvar e carregar modelos treinados

# Carrega o conjunto de dados a partir de um arquivo CSV
df = pd.read_csv('./estatistica_de_dados/clientes-v3-preparado.csv')

# Cria uma nova coluna 'salario_categoria' que será a variável alvo (target)
# Se o salário for maior que a mediana dos salários, classifica como 1, senão como 0
df['salario_categoria'] = (df['salario'] > df['salario'].median()).astype(int)

# Define as variáveis preditoras (features) e a variável alvo
X = df[['idade', 'anos_experiencia', 'nivel_educacao_cod']]  # Features
Y = df['salario_categoria']  # Target

# Divide os dados em treino (80%) e teste (20%) de forma aleatória, garantindo reprodutibilidade com random_state=42
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Cria e treina um modelo de Regressão Logística
modelo_lr = LogisticRegression()
modelo_lr.fit(X_train, Y_train)

# Cria e treina um modelo de Árvore de Decisão
modelo_dt = DecisionTreeClassifier()
modelo_dt.fit(X_train, Y_train)

# Faz previsões com os modelos treinados usando os dados de teste
Y_prev_lr = modelo_lr.predict(X_test)
Y_prev_dt = modelo_dt.predict(X_test)

# Calcula as métricas de avaliação para o modelo de Regressão Logística
accuracy_lr = accuracy_score(Y_test, Y_prev_lr)  # Acurácia: porcentagem de previsões corretas
precision_lr = precision_score(Y_test, Y_prev_lr)  # Precisão: proporção de positivos preditos corretamente
recall_lr = recall_score(Y_test, Y_prev_lr)  # Recall: proporção de positivos reais detectados corretamente

# Exibe os resultados das métricas para a Regressão Logística
print(f'\nAcurácia de Regressão Logística: {accuracy_lr:.2f}')
print(f'\nPrecisão da Regressão Logística: {precision_lr:.2f}')
print(f'\nRecall (Sensibilidade) da Regressão Logística: {recall_lr:.2f}')

# Salva os modelos treinados em arquivos para uso posterior
joblib.dump(modelo_lr, filename= './estatistica_de_dados/modelo_regressao_logistica.pkl')
joblib.dump(modelo_dt, filename= './estatistica_de_dados/modelo_arvore_decisao.pkl')