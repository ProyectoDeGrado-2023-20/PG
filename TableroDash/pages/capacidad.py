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
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
# import plotly.graph_objects as go


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Data
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('TableroDash/Data/Capacidad_Instalada_Poblacion.csv')

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
            value=capacidad[0],
            multi=True,
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

        # Contenedor
        dbc.Container(
            children=[
                dbc.Row(
                    children=[


                        # ---------------------------------------------------------
                        # Dropdowns
                        # ---------------------------------------------------------

                        dbc.Col(
                            children=[
                                html.Div(
                                    children=[


                                        # ---------------------------------------------------------
                                        # Dropdown Departamentos
                                        # ---------------------------------------------------------

                                        html.Label(
                                            'Selecciona un departamento:'
                                        ),
                                        dcc.Dropdown(
                                            id='dropdown-departamento',
                                            options=[{'label': d, 'value': d}
                                                     for d in departamentos],
                                            value='Nacional',
                                            multi=True,
                                            # clearable=False,
                                        ),


                                        # ---------------------------------------------------------
                                        # Dropdown Capacidades
                                        # ---------------------------------------------------------

                                        html.Label(
                                            'Selecciona una opción para la gráfica:'
                                        ),
                                        dcc.Dropdown(
                                            id='dropdown-capacidad',
                                            options=[{'label': opt, 'value': opt}
                                                     for opt in capacidad],
                                            value=capacidad[0],
                                            # multi=True,
                                            clearable=False,
                                        ),
                                    ],
                                ),
                            ],
                            width=3,
                            className='bg-light',
                        ),


                        # ---------------------------------------------------------
                        # Graficos
                        # ---------------------------------------------------------

                        dbc.Col(
                            children=[
                                html.Div(
                                    children=[
                                        dcc.Graph(id='graph-capacidad-bruta')
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        dcc.Graph(
                                            id='graph-capacidad-poblacion')
                                    ]
                                ),
                            ],
                            width=9,
                        ),
                    ],
                    style={
                        "height": "100vh",
                    },
                ),
            ],
            fluid=True,
        ),
    ])


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Callback
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

@app.callback(
    [
        Output('graph-capacidad-bruta', 'figure'),
        Output('graph-capacidad-poblacion', 'figure'),
    ],
    [
        Input('dropdown-departamento', 'value'),
        Input('dropdown-capacidad', 'value'),
    ],
)
def actualizar_grafica(departamento, capacidad):

    if isinstance(departamento, str):
        departamento = [departamento]

    # -------------------------------------------------------------------------------------------------------------------
    # Grafica Capacidad Instalada
    # -------------------------------------------------------------------------------------------------------------------

    max_graph_capacidad_bruta = df[df['Departamento'].isin(
        departamento)][capacidad].max()
    sd_graph_capacidad_bruta = df[df['Departamento'].isin(
        departamento)][capacidad].std()

    graph_capacidad_bruta = px.line(
        data_frame=df[df['Departamento'].isin(departamento)],
        x='Anio',
        y=capacidad,
        color='Departamento',
        range_y=[0, max_graph_capacidad_bruta + sd_graph_capacidad_bruta],
        title=f'{capacidad} por Departamento de 2002 a 2022'
    )

    graph_capacidad_bruta.update_layout(
        xaxis_title='Año',
        yaxis_title=capacidad,
    )

    # -------------------------------------------------------------------------------------------------------------------
    # Grafica Capacidad Instalada por cada 100 mil Habitantes
    # -------------------------------------------------------------------------------------------------------------------

    max_graph_capacidad_poblacion = df[df['Departamento'].isin(
        departamento)][f'{capacidad}/Habitantes'].max()
    sd_graph_capacidad_poblacion = df[df['Departamento'].isin(
        departamento)][f'{capacidad}/Habitantes'].std()

    graph_capacidad_poblacion = px.line(
        data_frame=df[df['Departamento'].isin(departamento)],
        x='Anio',
        y=f'{capacidad}/Habitantes',
        color='Departamento',
        range_y=[0, max_graph_capacidad_poblacion +
                 sd_graph_capacidad_poblacion],
        title=f'{capacidad} por cada 100 mil Habitantes por Departamento de 2002 a 2022'
    )

    graph_capacidad_poblacion.update_layout(
        xaxis_title='Año',
        yaxis_title=dict(
            text=f'{capacidad} cada 100 mil Habitantes',
            font=dict(
                size=12
            ),
        )
    )

    return graph_capacidad_bruta, graph_capacidad_poblacion
