import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import plotly.graph_objects as go

#Dados

dados_conceitos= dict(
    java =       {'variáveis': 3, 'condicioanais' :6, 'loops': 2, 'poo':1, 'funções':1},
    python =     {'variáveis': 9, 'condicioanais': 8, 'loops': 5, 'poo':7, 'funções':4},
    sql =        {'variáveis': 10, 'condicioanais': 2, 'loops': 3, 'poo':4, 'funções':4},
    golang =     {'variáveis': 7, 'condicioanais': 6, 'loops': 5, 'poo':4, 'funções':3},
    javascript = {'variáveis': 8, 'condicioanais': 7, 'loops': 4, 'poo':3, 'funções':2})

color_map=dict(
    java='red',
    python='blue',
    sql='grey',
    golang = 'orange',
    javascript = 'yellow'
)

#POO - programação orientada a objetos - Em Python seria em classes 
app = dash.Dash(__name__)

#_______________________________Layout_____________________________

#Monto o esqueleto onde vou posiicionar as coisas

app.layout = html.Div([
    html.H2 ('Ricardo Batista', style={'text-align':'center'}),
    html.Div(dcc.Dropdown(id='dropdown_linguagens',
                          options=[
                              {'label':'Java','value': 'java'},
                              {'label':'Python','value': 'python'},
                              {'label':'SQL','value': 'sql'},
                              {'label':'Golang','value': 'golang'},
                              {'label':'JavaScript','value': 'javascript'}],
                              value=['java'],
                              multi=True,
                              style={'width': '70%','margin': '0 auto'}
                                   )
    ),
    dcc.Graph(
        id='scatter_plot'
        
    )

    ])

#Quanto maior o número do H, menor é o texto
#dcc esta associado ao 

#_____________________________Callbacks____________________________
#Onde o layout vai rodar

@app.callback(
        Output('scatter_plot','figure'),
        [Input('dropdown_linguagens','value')]
    
)
def atualizar_scatter(linguagens_selecionadas):

    scatter_trace=[]

    for linguagem in linguagens_selecionadas:
        dados_linguagem=dados_conceitos[linguagem]
        for conceito, conhecimento in dados_linguagem.items():
            scatter_trace.append(
            go.Scatter(
                x=[conceito],
                y=[conhecimento],
                mode='markers',
                name=linguagem.upper(),
                marker=dict(size=20, color=color_map[linguagem]),
                showlegend=False
                )
               
            )

    scatter_layout = go.Layout(
    title= 'Minhas Linguagens',
    xaxis=dict(title='Conceitos', showgrid=False),
    yaxis=dict(title='Nivel de conhecimento', showgrid=False)
)

    return {'data': scatter_trace, 'layout': scatter_layout}


if __name__ == '__main__':
    app.run_server(debug=True)



