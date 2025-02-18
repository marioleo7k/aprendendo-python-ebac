# Importa a biblioteca Pandas para manipulação de dados
import pandas as pd 

# Importa a biblioteca Matplotlib para criação de gráficos
import matplotlib.pyplot as plt 

# Lê o arquivo CSV e carrega os dados em um DataFrame do Pandas
df = pd.read_csv('./visualizacao_de_dados/clientes-v3-preparado.csv') 

# Exibe as primeiras 20 linhas do DataFrame de forma completa no terminal
print(df.head(20).to_string()) 

# --- GRÁFICO DE BARRAS (USANDO PANDAS) ---
plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70') # Conta as ocorrências de cada nível de educação e plota um gráfico de barras
plt.title('Divisão de Escolaridade - 1') # Define o título do gráfico
plt.xlabel('Nível de Educação') # Define o rótulo do eixo X
plt.ylabel('Quantidade') # Define o rótulo do eixo Y
plt.xticks(rotation=0) # Mantém os rótulos do eixo X na posição horizontal
plt.show() # Exibe o gráfico

# --- GRÁFICO DE BARRAS (USANDO MATPLOTLIB) ---
x = df['nivel_educacao'].value_counts().index # Obtém os rótulos únicos do eixo X (níveis de educação)
y = df['nivel_educacao'].value_counts().values # Obtém a contagem de cada nível de educação

plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico
plt.bar(x, y, color='#60aaee') # Cria um gráfico de barras manualmente
plt.title('Divisão de Escolaridade - 2') # Define o título do gráfico
plt.xlabel('Nível de Educação') # Define o rótulo do eixo X
plt.ylabel('Quantidade') # Define o rótulo do eixo Y
plt.xticks(rotation=0) # Mantém os rótulos do eixo X na posição horizontal
plt.show() # Exibe o gráfico

# --- GRÁFICO DE PIZZA ---
plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90) # Cria um gráfico de pizza com percentuais formatados com uma casa decimal
plt.title('Distribuição de Nível de Educação') # Define o título do gráfico
plt.show() # Exibe o gráfico

# --- GRÁFICO DE HEXBIN (DISPERSÃO) ---
plt.figure(figsize=(10, 6)) # Define o tamanho da figura do gráfico
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Greens') # Cria um gráfico de dispersão no formato de hexágonos para mostrar densidade
plt.colorbar(label='Contagem dentro do bin') # Adiciona uma barra de cores ao gráfico para indicar densidade
plt.xlabel('Idade') # Define o rótulo do eixo X
plt.ylabel('Salário') # Define o rótulo do eixo Y
plt.title('Dispersão entre Idade e Salário') # Define o título do gráfico
plt.show() # Exibe o gráfico