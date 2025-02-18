# Importação das bibliotecas
import pandas as pd  # Biblioteca para manipulação de dados
import matplotlib.pyplot as plt  # Biblioteca para visualização de dados básicos
import seaborn as sns  # Biblioteca para visualização de dados avançados

# Carrega o arquivo CSV em um DataFrame
df = pd.read_csv('./visualizacao_de_dados/clientes-v3-preparado.csv')

# Exibe as primeiras 5 linhas do DataFrame no console, formatado como string completa
print(df.head().to_string())

# 📊 Criando um Histograma simples dos salários
plt.hist(df['salario'])  # Cria um histograma com os valores da coluna 'salario'
plt.show()  # Exibe o gráfico

# 📊 Criando um Histograma mais detalhado com configurações
plt.figure(figsize=(10, 6))  # Define o tamanho do gráfico (10x6 polegadas)
plt.hist(df['salario'], bins=100, color='green', edgecolor='black', alpha=0.8)  # Cria histograma com 100 intervalos (bins), cor verde e bordas pretas
plt.title('Histograma - Distribuição de Salários')  # Adiciona um título ao gráfico
plt.xlabel('Salário')  # Nomeia o eixo X
plt.xticks(ticks=range(0, int(df['salario'].max()), 2000))  # Define marcações no eixo X de 2000 em 2000
plt.ylabel('Frequência')  # Nomeia o eixo Y
plt.grid(True)  # Adiciona uma grade ao gráfico para facilitar a leitura
plt.show()  # Exibe o gráfico

# 📊 Criando múltiplos gráficos na mesma figura
plt.figure(figsize=(10, 6))  # Define o tamanho do conjunto de gráficos

# 🔹 Gráfico de Dispersão 1 (Salário vs Salário)
plt.subplot(2, 2, 1)  # Define a posição do primeiro gráfico (linha 1, coluna 1)
plt.scatter(df['salario'], df['salario'])  # Cria um gráfico de dispersão (scatter plot)
plt.title('Dispersão - Salário e Salário')  # Define o título do gráfico
plt.xlabel('Salário')  # Nomeia o eixo X
plt.ylabel('Salário')  # Nomeia o eixo Y

# 🔹 Gráfico de Dispersão 2 (Salário vs Anos de Experiência)
plt.subplot(1, 2, 2)  # Define a posição do segundo gráfico (linha 1, coluna 2)
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30)  # Cria um gráfico de dispersão personalizado
plt.title('Dispersão - Salário e Anos de Experiência')  # Define o título do gráfico
plt.xlabel('Salário')  # Nomeia o eixo X
plt.ylabel('Anos de Experiência')  # Nomeia o eixo Y

# 🔹 Gráfico de Mapa de Calor (Correlação entre Salário e Anos de Experiência)
corr = df[['salario', 'anos_experiencia']].corr()  # Calcula a matriz de correlação entre as colunas 'salario' e 'anos_experiencia'
plt.subplot(2, 2, 3)  # Define a posição do terceiro gráfico (linha 2, coluna 1)
sns.heatmap(corr, annot=True, cmap='coolwarm')  # Cria um mapa de calor com as correlações
plt.title('Mapa de Calor - Correlação Salário e Anos de Experiência')  # Define o título do gráfico

# Ajusta o layout para evitar sobreposição dos gráficos
plt.tight_layout()

# Exibe todos os gráficos na tela
plt.show()