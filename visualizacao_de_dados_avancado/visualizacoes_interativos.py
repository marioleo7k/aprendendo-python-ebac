# Importa as bibliotecas necessárias
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Lê o dataset
df = pd.read_csv('./visualizacao_de_dados_avancado/clientes-v3-preparado.csv')

# Obtém os níveis únicos de educação
lista_nivel_educacao = df['nivel_educacao'].unique()

# Cria a lista de opções para o Dropdown
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]

# Função para criar os gráficos com base na seleção do nível de educação
def cria_graficos(selecao_nivel_educacao):
    # Filtra os dados de acordo com os níveis de educação selecionados
    filtro_df = df[df['nivel_educacao'].isin(selecao_nivel_educacao)]

    # Gráfico de barras - Salário por Estado Civil
    fig1 = px.bar(
        filtro_df, 
        x='estado_civil', 
        y='salario', 
        color='nivel_educacao', 
        barmode='group', 
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig1.update_layout(
        title='Salário por Estado Civil',
        xaxis_title='Estado Civil',
        yaxis_title='Salário',
        legend_title='Nível de Educação',
        plot_bgcolor='white',
        paper_bgcolor='lightgray',  # Corrigi a cor de fundo para um tom mais neutro
    )

    # Gráfico de dispersão - Salário vs Idade e Anos de Experiência
    fig2 = px.scatter(
        filtro_df, 
        x='idade', 
        y='salario', 
        size='anos_experiencia', 
        color='nivel_educacao', 
        hover_name='estado'
    )
    fig2.update_layout(
        title='Salário vs Idade e Anos de Experiência',
        xaxis_title='Idade',
        yaxis_title='Salário'
    )

    return fig1, fig2  # Retorna os gráficos gerados

# Função para criar o aplicativo Dash
def cria_app():
    app = Dash(__name__)

    # Layout do app
    app.layout = html.Div([
        html.H1('Visualização de Dados Interativos'),  # Título principal
        html.Div('Selecione o nível de educação:'),  # Texto informativo
        dcc.Dropdown(
            id='nivel_educacao',  # ID do dropdown
            options=options,  # Opções extraídas do dataset
            value=['Graduação'],  # Valor inicial padrão
            multi=True,  # Permite selecionar múltiplos valores
        ),
        dcc.Graph(id='grafico1'),  # Primeiro gráfico (barras)
        dcc.Graph(id='grafico2'),  # Segundo gráfico (dispersão)
    ])

    # Callback para atualizar os gráficos dinamicamente com base na seleção do usuário
    @app.callback(
        [Output('grafico1', 'figure'),
         Output('grafico2', 'figure')],
        [Input('nivel_educacao', 'value')]
    )
    def atualiza_graficos(nivel_educacao):
        return cria_graficos(nivel_educacao)

    return app  # Retorna o app configurado

# Condição para rodar o app no servidor
if __name__ == "__main__":  
    app = cria_app()  # Chama a função que cria o app
    app.run_server(debug=True, port=8050)  # Roda o servidor na porta 8050