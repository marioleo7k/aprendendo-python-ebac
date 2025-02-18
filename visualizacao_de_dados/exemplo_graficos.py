# Importa a biblioteca Pandas para manipulação de dados
import pandas as pd 

# Importa a biblioteca Matplotlib para criação de gráficos
import matplotlib.pyplot as plt 

# Importa a biblioteca Seaborn para visualizações estatísticas avançadas
import seaborn as sns 

# Lê o arquivo CSV e carrega os dados em um DataFrame do Pandas
df = pd.read_csv('./visualizacao_de_dados/clientes-v3-preparado.csv') 

# Exibe as primeiras 20 linhas do DataFrame de forma completa no terminal
print(df.head(20).to_string()) 

# --- CÁLCULO DA MATRIZ DE CORRELAÇÃO ---
df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos', 'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()
# Cria uma matriz de correlação entre as variáveis numéricas selecionadas
# A correlação mede a relação entre duas variáveis (-1 a 1), onde:
# - 1 indica uma correlação positiva perfeita
# - -1 indica uma correlação negativa perfeita
# - 0 indica ausência de correlação

# --- GRÁFICO DE HEATMAP DE CORRELAÇÃO ---
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
sns.heatmap(df_corr, annot=True, cmap='coolwarm', fmt='.2f')  
# Cria um mapa de calor (heatmap) para visualizar a matriz de correlação
# `annot=True` exibe os valores numéricos dentro das células
# `cmap='coolwarm'` define a escala de cores (tons de azul para correlações negativas, vermelho para positivas)
# `fmt='.2f'` exibe os números com duas casas decimais

plt.title('Heatmap de Correlação')  # Define o título do gráfico
plt.show()  # Exibe o gráfico

# --- GRÁFICO DE COUNT PLOT (ESTADO CIVIL) ---
sns.countplot(x='estado_civil', data=df)  
# Cria um gráfico de contagem mostrando quantos clientes pertencem a cada categoria de estado civil

plt.title('Distribuição do Estado Civil')  # Define o título do gráfico
plt.xlabel('Estado Civil')  # Define o rótulo do eixo X
plt.ylabel('Contagem')  # Define o rótulo do eixo Y
plt.show()  # Exibe o gráfico

# --- GRÁFICO DE COUNT PLOT COM HUE (ESTADO CIVIL VS NÍVEL DE EDUCAÇÃO) ---
sns.countplot(x='estado_civil', data=df, hue='nivel_educacao')  
# Cria um gráfico de contagem semelhante ao anterior, mas agora segmentado pelo nível de educação
# O argumento `hue='nivel_educacao'` agrupa os dados de estado civil por nível de educação

plt.title('Distribuição do Estado Civil')  # Define o título do gráfico
plt.xlabel('Estado Civil')  # Define o rótulo do eixo X
plt.ylabel('Contagem')  # Define o rótulo do eixo Y
plt.legend(title='Nível de Educação')  # Adiciona uma legenda indicando as categorias do nível de educação
plt.show()  # Exibe o gráfico