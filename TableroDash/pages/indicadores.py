# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Libraries
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from app import app
from apps import navigation
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import json
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Data
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# Datos de Numero IPS - Departamentos
df_ips_por_departamentos = pd.read_csv('./Data/IPS_por_Departamentos_2022.csv')

# Datos de los Mapas de Numero IPS - Departamentos
df_mapa_numero_ips = pd.read_csv('./Data/Mapa_Numero_IPS.csv')

# Datos de Numero IPS - Municipios
df_ips_por_departamentos_habitantes = pd.read_csv(
    './Data/IPS_por_Departamentos_Habitantes_2022.csv')

# Datos de los Mapas de Numero IPS - Municipios
df_mapa_numero_ips_municipios = pd.read_csv(
    './Data/Mapa_Numero_IPS_Municipios.csv')

# Datos de Distribucion Naturaleza Juridica Nacional
df_ips_naturaleza_juridica = pd.read_csv(
    './Data/Naturaleza_Juridica_Nacional.csv')
df_ips_naturaleza_juridica['Category'] = ''

# Datos de Distribucion Naturaleza Juridica por Departamento
df_naturaleza_juridica_departamento = pd.read_csv(
    './Data/Naturaleza_Juridica_Departamento.csv')

# Geojson para mapas Departamentos
file_path = './Data/Colombia_Departamentos_Modified.json'
with open(file_path, 'r') as file:
    geojson_departamentos = json.load(file)

# Geojson para Mapas Municipios
file_path = './Data/Colombia_Municipios_Modified.json'
with open(file_path, 'r') as file:
    geojson_municipios = json.load(file)

# Datos de los Mapas de Distancias IPS Publicas
df_mapa_distancia_ips = pd.read_csv('./Data/Mapa_Distancia_IPS.csv')


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Funciones
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# Barras Departamento - Numero IPS y Numero IPS por cada mil habitantes

def graph_barras_ips_departamento(df: pd.DataFrame, x: str, y: str, range_x: list, width: int, x_axes: str, title: str):

    fig = px.bar(data_frame=df,
                 x=x,
                 y=y,
                 orientation='h')

    fig.update_xaxes(title_text=x_axes)
    fig.update_xaxes(range=range_x)
    fig.update_yaxes(title_text='')
    fig.update_layout(title=title)

    color_sequence = [
        '#3364C7' for i in df[y]]
    fig.update_traces(marker=dict(color=color_sequence))

    fig.update_traces(
        text=df[x], textposition='outside')

    fig.update_layout(width=width, height=700)

    graph_barras_ips_departamento = html.Div(
        [
            dcc.Graph(figure=fig)
        ]
    )

    return graph_barras_ips_departamento

# -------------------------------------------------------------------------------------------------------------------
# Mapa Departamento - Numero IPS y Numero IPS por cada mil habitantes


def graph_mapa_ips_departamento(geojson: dict, df: pd.DataFrame, locations: str, z: str, colorscale: list, title: str, zoom: float, width: int):

    locations = df[locations]

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=locations,
            featureidkey='properties.Departamento',
            z=df[z],
            colorscale=colorscale
        )
    )

    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_zoom=zoom,
        mapbox_center={"lat": 4.570868, "lon": -74.2973328},
        width=width,
        height=720
    )

    fig.update_layout(
        title=title
    )

    graph_mapa_ips_departamento = html.Div(
        [
            dcc.Graph(figure=fig)
        ]
    )

    return graph_mapa_ips_departamento


# -------------------------------------------------------------------------------------------------------------------
# Mapa Municipio - Numero IPS y Numero IPS por cada mil habitantes

def graph_mapa_ips_municipio(geojson: dict, df: pd.DataFrame, locations: str, z: str, colorscale: list, title: str, zoom: float, width: int):

    locations = df[locations]

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=locations,
            featureidkey='properties.key',
            z=df[z],
            colorscale=colorscale
        )
    )

    fig.update_layout(
        mapbox_style="white-bg",
        # mapbox_style="carto-positron",
        mapbox_zoom=zoom,
        mapbox_center={"lat": 43.5, "lon": -62.3},
        width=width,
        height=800
    )

    fig.update_layout(
        title=title
    )

    graph_mapa_ips_municipio = html.Div(
        [
            dcc.Graph(figure=fig)
        ]
    )

    return graph_mapa_ips_municipio

# -------------------------------------------------------------------------------------------------------------------
# Barras Nacional - Numero IPS Naturaleza Juridica y Porcentaje IPS Naturaleza Juridica


def graph_barras_ips_naturaleza_juridica(df: pd.DataFrame, x: str, y: str, color: str, width, title: str, range_y: list, y_title: str):

    color_palette = {
        'Privada': '#3364C7',
        'Pública': '#8CBCB9',
        'Mixta': '#826251'
    }

    fig = px.bar(df,
                 x=x,
                 y=y,
                 color=color,
                 barmode='stack',
                 width=width,
                 height=500,
                 color_discrete_map=color_palette,
                 title=title,
                 )

    fig.update_yaxes(range=range_y)
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text=y_title)

    fig.update_layout(legend_title_text='Legends', legend=dict(
        title=dict(text='Naturaleza Jurídica')))

    graph_barras_ips_naturaleza_juridica = html.Div(
        [
            dcc.Graph(figure=fig)
        ]
    )

    return graph_barras_ips_naturaleza_juridica


# -------------------------------------------------------------------------------------------------------------------
# Barras Departamento - Numero IPS Naturaleza Juridica y Porcentaje IPS Naturaleza Juridica

def graph_barras_ips_naturaleza_juridica_departamento(df: pd.DataFrame, x: str, y: str, color: str, x_title: str, x_range: list, title: str, width):
    color_palette = {
        'Privada': '#3364C7',
        'Pública': '#8CBCB9',
        'Mixta': '#826251'
    }

    fig = px.bar(data_frame=df,
                 x=x,
                 y=y,
                 color=color,
                 orientation='h',
                 color_discrete_map=color_palette)

    fig.update_xaxes(
        title_text=x_title)
    fig.update_xaxes(range=x_range)
    fig.update_yaxes(
        title_text='')
    fig.update_layout(
        title=title)
    fig.update_layout(
        legend_title_text='Legends', legend=dict(title=dict(text='Naturaleza Jurídica')))
    fig.update_layout(
        width=width, height=700)

    graph_barras_ips_naturaleza_juridica_departamento = html.Div(
        [
            dcc.Graph(figure=fig)
        ]
    )

    return graph_barras_ips_naturaleza_juridica_departamento


# -------------------------------------------------------------------------------------------------------------------
# Barras Departamento - Numero IPS Naturaleza Juridica y Porcentaje IPS Naturaleza Juridica

def graph_mapa_distancia_ips_municipio(geojson: dict, df: pd.DataFrame, locations: str, poblacion: str, nivel: int, tipo_ips: str, colorscale: list, zoom: float, width: int, title: str):
    # Distancia_IPS_Nivel_1_Publicas
    # Distancia_Poblacion_IPS_Nivel_1_Publicas
    z = f'Distancia{poblacion}_IPS_Nivel_{nivel}_{tipo_ips}'
    locations = df[locations]

    fig = go.Figure(

        go.Choroplethmapbox(
            geojson=geojson,
            locations=locations,
            featureidkey='properties.key',
            z=df[z],
            colorscale=colorscale
        )
    )

    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_zoom=zoom,
        mapbox_center={"lat": 43.5, "lon": -62.3},
        width=width,
        height=800,
    )

    fig.update_layout(
        title=title
    )

    # graph_mapa_distancia_ips_municipio = dcc.Graph(
    #     figure=fig
    # )

    return fig


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Numero IPS e IPS por Habitantes
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# Numero de IPS - Departamentos

graph_numero_ips_departamento = graph_barras_ips_departamento(df_ips_por_departamentos, 'IPS_2022', 'Departamento', [
                                                              0, 3200], 640, 'Número de IPS', 'Número de IPS por Departamento - 2022')


# -------------------------------------------------------------------------------------------------------------------
# Numero IPS por Habitantes - Departamentos

graph_numero_ips_departamento_por_habitantes = graph_barras_ips_departamento(df_ips_por_departamentos_habitantes, 'IPS/Habitantes', 'Departamento', [
                                                                             0, 130], 640, 'Número de IPS por cada 100 mil Habitantes', 'Número de IPS por cada 100 mil Habitantes por Departamento - 2022')


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS - Departamentos

colorscale = ["#b62020",
              ]*1 + ["#b3cde0",
                     ]*1 + ["#6497b1",
                            ]*1 + ["#005b96",
                                   ]*1 + ["#03396c",
                                          ]*1 + ["#011f4b",
                                                 ]*1

graph_mapa_numero_ips_departamento = graph_mapa_ips_departamento(
    geojson_departamentos, df_mapa_numero_ips, 'Departamento_DANE', 'IPS_2022', colorscale, 'Número de IPS por Departamento', 4.4, 640)


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS por Habitantes - Departamentos

colorscale = ["#b62020",
              ]*1 + ["#fe8181",
                     ]*1 + ["#b3cde0",
                            ]*1 + ["#6497b1",
                                   ]*1 + ["#005b96",
                                          ]*1 + ["#03396c",
                                                 ]*1 + ["#011f4b",
                                                        ]*2

graph_mapa_numero_ips_departamento_habitantes = graph_mapa_ips_departamento(
    geojson_departamentos, df_mapa_numero_ips, 'Departamento_DANE', 'IPS/Habitantes', colorscale, 'Número de IPS por cada 100 mil Habitantes por Departamento', 4.4, 640)


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS - Municipios

colorscale = ["#b62020",
              ]*1 + ["#cb2424",
                     ]*1 + ["#fe5757",
                            ]*5 + ["#fe8181",
                                   ]*5 + ["#b3cde0",
                                          ]*90 + ["#6497b1",
                                                  ]*900 + ["#005b96",
                                                           ]*1000 + ["#011f4b",
                                                                     ]*1000


graph_mapa_numero_ips_municipios = graph_mapa_ips_municipio(
    geojson_municipios, df_mapa_numero_ips_municipios, 'Municipio_Departamento', 'IPS_2022', colorscale, 'Número de IPS por Municipio', 4, 640)


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS por Habitantes - Municipios

colorscale = ["#b62020",
              ]*1 + ["#fe5757",
                     ]*1 + ["#fe8181",
                            ]*1 + ["#b3cde0",
                                   ]*5 + ["#6497b1",
                                          ]*5 + ["#005b96",
                                                 ]*5 + ["#03396c",
                                                        ]*10 + ["#011f4b",
                                                                ]*10

graph_mapa_numero_ips_municipios_habitantes = graph_mapa_ips_municipio(
    geojson_municipios, df_mapa_numero_ips_municipios, 'Municipio_Departamento', 'IPS/Habitantes', colorscale, 'Número de IPS por Municipio', 4, 640)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Naturaleza Juridica IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# Numero IPS - Naturaleza Juridica

graph_ips_naturaleza_juridica = graph_barras_ips_naturaleza_juridica(
    df_ips_naturaleza_juridica, 'Category', 'IPS_2022', 'NaturalezaJuridica', 450, 'Número de IPS por Naturaleza Juridica - 2022', [0, 20000], 'Número de IPS')


# -------------------------------------------------------------------------------------------------------------------
# Porcentaje IPS - Naturaleza Juridica

graph_ips_naturaleza_juridica_porcentaje = graph_barras_ips_naturaleza_juridica(
    df_ips_naturaleza_juridica, 'Category', 'Porcentaje', 'NaturalezaJuridica', 450, 'Porcentaje de IPS por Naturaleza Juridica - 2022', [0, 100], 'Porcentaje de IPS (%)')


# -------------------------------------------------------------------------------------------------------------------
# Numero IPS - Naturaleza Juridica - Departamento

graph_ips_naturaleza_juridica_numero_departamento = graph_barras_ips_naturaleza_juridica_departamento(
    df_naturaleza_juridica_departamento, 'Numero_IPS', 'Departamento', 'NaturalezaJuridica', 'Número de IPS', [0, 3000], 'Número de IPS por Departamento por Naturaleza Juridica- 2022', 640)


# -------------------------------------------------------------------------------------------------------------------
# Porcentaje IPS - Naturaleza Juridica - Departamento

graph_ips_naturaleza_juridica_porcentaje_departamento = graph_barras_ips_naturaleza_juridica_departamento(
    df_naturaleza_juridica_departamento, 'Porcentaje_IPS', 'Departamento', 'NaturalezaJuridica', 'Porcentaje de IPS (%)', [0, 100], 'Distribucion Naturaleza Juridica IPS por Departamento - 2022', 640)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias a IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

colorscale = ["#fff",
              ]*1 + ["#fe8181",
                     ]*1 + ["#fe5757",
                            ]*1 + ["#fe2e2e",
                                   ]*1 + ["#cb2424",
                                          ]*1 + ["#b62020",
                                                 ]*1

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Layout
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

indicadores_layout = html.Div(children=[

    # -------------------------------------------------------------------------------------------------------------------
    # Barra de Navegación
    # -------------------------------------------------------------------------------------------------------------------
    navigation.navbar,

    html.Br(),


    # -------------------------------------------------------------------------------------------------------------------
    # Sección Numero de IPS e IPS por Habitantes
    # -------------------------------------------------------------------------------------------------------------------

    # Departamentos
    html.Div(
        children=[
            html.H2(
                'Análisis de las Instituciones Prestadoras de Salud (IPS) en Colombia',
                style={
                    'text-align': 'center'
                }
            ),

            html.Br(),

            html.H3(
                'Departamental',
                style={
                    'text-align': 'center'
                }
            ),
            html.P(
                children=[
                    '''
                    A nivel Departamental es posible observar el número de IPS y el número de IPS por cada 100 mil habitantes.
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
        ],
        style={
            # 'width': '100%',
            'display': 'flex',
            'flex-direction': 'column',
            # 'flex-wrap': 'wrap',
            'justify-content': 'center',
            'align-items': 'center',
        }
    ),

    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Número de IPS'
                    ),
                    graph_numero_ips_departamento,
                    graph_mapa_numero_ips_departamento,
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
            html.Div(
                children=[
                    html.H5(
                        'Número de IPS por Cada 100 mil Habitantes'
                    ),
                    graph_numero_ips_departamento_por_habitantes,
                    graph_mapa_numero_ips_departamento_habitantes,
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
        ],
        style={
            'display': 'flex',
            'flex-wrap': 'wrap',
            'justify-content': 'center',
            # 'justify-content': 'start',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),

    # Municipios
    html.Div(
        children=[
            html.Br(),

            html.H3(
                'Municipal',
                style={
                    'text-align': 'center'
                }
            ),
            html.P(
                children=[
                    '''
                    Es posible ir a un nivel más detallado realizando este mismo análisis, pero a nivel de cada municipio.
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
        ],
        style={
            # 'width': '100%',
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
        }
    ),

    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Número de IPS'
                    ),
                    graph_mapa_numero_ips_municipios,
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
            html.Div(
                children=[
                    html.H5(
                        'Número de IPS por Cada 100 mil Habitantes'
                    ),
                    graph_mapa_numero_ips_municipios_habitantes,
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
        ],
        style={
            'display': 'flex',
            'flex-wrap': 'wrap',
            'justify-content': 'center',
            # 'justify-content': 'start',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),


    # -------------------------------------------------------------------------------------------------------------------
    # Sección Naturaleza Juridica IPS
    # -------------------------------------------------------------------------------------------------------------------

    # Departamentos
    html.Div(
        children=[
            html.H2(
                'Distribución por Naturaleza Juridica y Niveles IPS',
                style={
                    'text-align': 'center'
                }
            ),

            html.Br(),

            html.P(
                children=[
                    '''
                    Las IPS se encuentran divididas según su complejidad o nivel de atención así:
                    ''',
                    html.Ul(
                        children=[
                            html.Li(
                                'Baja (1): Atención general con tecnología de baja complejidad'),
                            html.Li(
                                'Mediana (2): Atención general y especializada con tecnología de mediana complejidad'),
                            html.Li(
                                'Alta (3): Atención general, especializada y subespecializada con tecnología de alta complejidad'),
                        ],
                        style={
                            # 'width': '80%',
                        }
                    ),
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
            html.P(
                children=[
                    '''
                    Sin embargo, esta clasificación solo existe para las IPS cuya Naturaleza Jurídica es Pública. Por lo que es necesario entender cúal es la distribucion de todas las IPS por naturaleza jurídica a nivel general y departamental.
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
        ],
        style={
            # 'width': '100%',
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
        }
    ),

    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Número de IPS'
                    ),
                    graph_ips_naturaleza_juridica,
                    graph_ips_naturaleza_juridica_numero_departamento
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
            html.Div(
                children=[
                    html.H5(
                        'Porcentaje de IPS'
                    ),
                    graph_ips_naturaleza_juridica_porcentaje,
                    graph_ips_naturaleza_juridica_porcentaje_departamento
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
        ],
        style={
            'display': 'flex',
            'flex-wrap': 'wrap',
            'justify-content': 'center',
            # 'justify-content': 'start',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),


    # -------------------------------------------------------------------------------------------------------------------
    # Sección Distancias IPS
    # -------------------------------------------------------------------------------------------------------------------

    html.Div(
        children=[
            html.H2(
                'Distancia a IPS más Cercana por Nivel',
                style={
                    'text-align': 'center'
                }
            ),
            html.P(
                children=[
                    '''
                    Finalmente analizamos la distancia que se debe recorrer desde un municipio hasta la IPS de determinado nivel de atención más cercana. Sin embargo, el nivel de complejidad solo se define para las IPS Públicas, por lo que con un modelo de Machine Learning podemos clasificar todas las IPS con los tres niveles de atención
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
        }
    ),

    html.Br(),

    # Dropdowns
    html.Div(
        children=[
            # Publicas o Modelo
            html.Div(
                children=[
                    html.Label(
                        'Seleccione el tipo de distancia a evaluar:',
                        style={
                            'width': '100%',
                            'display': 'inline-block',
                        }
                    ),
                    dcc.Dropdown(
                        id='dropdown-tipo-ips',
                        options=[
                            {'label': 'Distancia a una IPS Pública',
                                'value': 'Publicas'},
                            {'label': 'Distancia a cualquier tipo de IPS',
                             'value': 'Modelo'},
                        ],
                        value='Publicas',
                        clearable=False,
                        style={
                            'width': '100%',
                        },
                    ),
                ],
                style={
                    'width': '80%',
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
            # Nivel de Atencion
            html.Div(
                children=[
                    html.Label(
                        'Seleccione el nivel de complejidad:',
                        style={
                            'width': '100%',
                            # 'display': 'inline-block',
                        }
                    ),
                    dcc.Dropdown(
                        id='dropdown-nivel-ips',
                        options=[
                            {'label': 'Baja Complejidad', 'value': 1},
                            {'label': 'Mediana Complejidad', 'value': 2},
                            {'label': 'Alta Complejidad', 'value': 3},
                        ],
                        value=1,
                        clearable=False,
                        style={
                            'width': '100%',
                        },
                    ),
                ],
                style={
                    'width': '80%',
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                },
            ),
        ],
        style={
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
        },
    ),

    # Fila 1 Mapas - Distancia N1 vs Distancia*Poblacion N1
    html.Div(
        children=[
            html.Div(
                children=[
                    dcc.Graph(
                        id='mapa-distancia-ips'
                    )
                    # graph_fig_mapa_ips_publicas_n1,
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                }
            ),
            html.Div(
                children=[
                    dcc.Graph(
                        id='mapa-distancia-poblacion-ips'
                    )
                    # graph_fig_mapa_poblacion_ips_publicas_n1,
                ],
                style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'justify-content': 'center',
                    'align-items': 'center',
                }
            )
        ],
        style={
            'display': 'flex',
            'flex-wrap': 'wrap',
            'justify-content': 'center',
            # 'justify-content': 'start',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),
])

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Callback
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


@app.callback(
    [
        Output('mapa-distancia-ips', 'figure'),
        Output('mapa-distancia-poblacion-ips', 'figure'),
    ],
    [
        Input('dropdown-tipo-ips', 'value'),
        Input('dropdown-nivel-ips', 'value'),
    ]
)
def actualizar_grafica(tipo_ips, nivel_ips):

    if tipo_ips == 'Publica':
        show = ' Pública '
    else:
        show = ''

    graph_mapa_distancia_ips = graph_mapa_distancia_ips_municipio(
        geojson_municipios,
        df_mapa_distancia_ips,
        'Municipio_Departamento',
        '',
        nivel_ips,
        tipo_ips,
        colorscale,
        4,
        640,
        f'Distancia a IPS{show} de Nivel {nivel_ips} (Km)'
    )

    graph_mapa_poblacion_ips = graph_mapa_distancia_ips_municipio(
        geojson_municipios,
        df_mapa_distancia_ips,
        'Municipio_Departamento',
        '_Poblacion',
        nivel_ips,
        tipo_ips,
        colorscale,
        4,
        640,
        f'Distancia Ponderada por Población a IPS{show} de Nivel 1 (Km)'
    )

    return graph_mapa_distancia_ips, graph_mapa_poblacion_ips
