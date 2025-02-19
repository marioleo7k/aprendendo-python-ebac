import pandas as pd # Biblioteca de manipulação de dados
import plotly.express as px # Biblioteca de visualização de dados

# Carregar o DataFrame
df = pd.read_csv('./visualizacao_de_dados_avancado/clientes-v3-preparado.csv')

# Gráfico de dispersão
fig = px.scatter(df, x= 'idade', y= 'salario', color= 'nivel_educacao', hover_data= ['estado_civil'])
fig.update_layout(
    title= 'Idade vs Salário por Nível de Educação',
    xaxis_title= 'Idade',
    yaxis_title= 'Salário'
)
fig.show()