# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from app import app
from apps import navigation
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
# from dotenv import dotenv_values
import pandas as pd
import plotly.graph_objects as go
# import dash_core_components as dcc
# import dash_html_components as html
from dash import dcc
from dash import html
import plotly.express as px
from dash import html
import dash_bootstrap_components as dbc

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Data
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('./Data/Capacidad_Instalada_Transformed.csv')

departamentos = list(df['Departamento'].unique())

capacidad = [
    'Camas de hospitalización',
    'Camas de observación',
    'Consultorios de consulta externa',
    'Consultorios en el servicio de urgencias',
    'Mesas de partos',
    'Número de unidades de odontología',
    'Salas de quirófanos'
]

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Sidebar
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


sidebar = html.Div(
    children=[
        html.Label('Selecciona un departamento:'),
        dcc.Dropdown(
            id='departamento-dropdown',
            options=[{'label': d, 'value': d} for d in departamentos],
            value='Nacional'
        ),
        html.Label('Selecciona una opción para la gráfica:'),
        dcc.Dropdown(
            id='capacidad-dropdown',
            options=[{'label': opt, 'value': opt} for opt in capacidad],
            value=capacidad[0]
        )
    ])

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Graph
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


graph = html.Div(
    [
        dcc.Graph(id='grafica_capacidad')
    ]
)

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Layout
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

capacidad_layout = html.Div(
    children=[
        # Barra de Navegación
        navigation.navbar,

        html.Br(),

        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(sidebar, width=3, className='bg-light'),
                        dbc.Col(graph, width=9)
                    ],
                    style={"height": "100vh"}
                ),
            ],
            fluid=True
        )
    ])


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Callback
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

@app.callback(
    Output('grafica_capacidad', 'figure'),
    [Input('departamento-dropdown', 'value'),
     Input('capacidad-dropdown', 'value')]
)
def actualizar_grafica(departamento, opcion_grafica):
    fig = px.line(df[df['Departamento'] == departamento],
                  x='Anio', y=opcion_grafica, color='Departamento')

    return fig
