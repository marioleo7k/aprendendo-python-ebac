import plotly.express as px  # Importa a biblioteca Plotly Express para visualizações interativas
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
from dash import Dash, html, dcc  # Importa componentes do Dash para criação de dashboards interativos

# Carrega os dados do arquivo CSV para um DataFrame
df = pd.read_csv('./visualizacao_de_dados_avancado/clientes-v3-preparado.csv')

def cria_graficos(df):
    # Histograma da distribuição de salários
    fig1 = px.histogram(df, x='salario', nbins=30, title='Distribuição de Salários')

    # Gráfico de pizza para distribuição de áreas de atuação
    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', hole=0, 
                  color_discrete_sequence=px.colors.sequential.Mint_r, title='Distribuição de Áreas de Atuação')

    # Gráfico de dispersão para representar salário x idade x anos de experiência
    fig3 = px.scatter(df, x='idade', y='salario', size='anos_experiencia', 
                      color='area_atuacao', hover_name='estado', size_max=60)
    fig3.update_layout(title='Salário x Idade x Anos de Experiência')

    # Gráfico de linha para salário por idade e nível de educação
    fig4 = px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_educacao')
    fig4.update_layout(
        title='Salário x Idade x Nível de Educação',
        xaxis_title='Idade',
        yaxis_title='Salário'
    )

    # Gráfico de dispersão 3D corrigido (z não é um argumento válido para px.scatter)
    fig5 = px.scatter(df, x='idade', y='salario', color='nivel_educacao', size='anos_experiencia', hover_data=['nivel_educacao'])
    fig5.update_layout(title='Salário x Idade x Nível de Educação')

    # Gráfico de barras para salário por estado civil e nível de educação
    fig6 = px.bar(df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group', 
                  color_discrete_sequence=px.colors.sequential.Viridis)
    fig6.update_layout(
        title='Salário por Estado Civil e Nível de Educação',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='white',
        paper_bgcolor='lightgray'  # Corrigindo erro de sintaxe na formatação do layout
    )

    return fig1, fig2, fig3, fig4, fig5, fig6

def cria_app(df):
    # Inicializa a aplicação Dash
    app = Dash(__name__)

    # Gera os gráficos
    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)

    # Define o layout do dashboard
    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])
    return app

# Carrega novamente os dados (não necessário, pois já foi carregado acima)
df = pd.read_csv('./visualizacao_de_dados_avancado/clientes-v3-preparado.csv')

# Executa o App
if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)