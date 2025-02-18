# Importa a biblioteca Pandas para manipulação de dados
import pandas as pd 

# Importa a biblioteca Seaborn para visualização avançada de dados
import seaborn as sns 

# Importa a biblioteca Matplotlib para criação de gráficos
import matplotlib.pyplot as plt 

# Lê o arquivo CSV e carrega os dados em um DataFrame do Pandas
df = pd.read_csv('./visualizacao_de_dados/clientes-v3-preparado.csv') 

# Exibe as primeiras 20 linhas do DataFrame de forma completa no terminal
print(df.head(20).to_string()) 

# --- GRÁFICO DE DISPERSÃO ---
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') 
# Cria um gráfico de dispersão para visualizar a relação entre idade e salário
# O Seaborn já gera uma visualização combinada com distribuições ao longo dos eixos
plt.show() # Exibe o gráfico

# --- GRÁFICO DE DENSIDADE ---
plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico
sns.kdeplot(df['salario'], fill=True, color='#863e9c') 
# Cria um gráfico de densidade (Kernel Density Estimation - KDE) para visualizar a distribuição do salário
plt.title('Densidade de Salário') # Define o título do gráfico
plt.xlabel('Salário') # Define o rótulo do eixo X
plt.show() # Exibe o gráfico

# --- GRÁFICO DE PAIRPLOT ---
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']]) 
# Cria múltiplos gráficos de dispersão e histogramas entre as variáveis selecionadas
plt.show() # Exibe o gráfico

# --- GRÁFICO DE REGRESSÃO LINEAR ---
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#f7a278'}) 
# Cria um gráfico de regressão linear entre idade e salário, mostrando a tendência da relação entre as variáveis
plt.title('Regressão Linear de Idade x Salário') # Define o título do gráfico
plt.xlabel('Idade') # Define o rótulo do eixo X
plt.ylabel('Salário') # Define o rótulo do eixo Y
plt.show() # Exibe o gráfico

# --- GRÁFICO DE CONTAGEM (COUNT PLOT) COM HUE ---
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel') 
# Cria um gráfico de contagem mostrando a quantidade de clientes por estado civil
# A cor (hue) diferencia os níveis de educação dentro de cada categoria de estado civil
plt.xlabel('Estado Civil') # Define o rótulo do eixo X
plt.ylabel('Quantidade de Clientes') # Define o rótulo do eixo Y
plt.legend(title='Nível de Educação') # Adiciona uma legenda indicando as categorias do nível de educação
plt.show() # Exibe o gráfico