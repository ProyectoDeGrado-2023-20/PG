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
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Data
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

file_path = './Data/Colombia_Municipios_Modified.json'
with open(file_path, 'r') as file:
    geojson = json.load(file)

df_mapa_ips_publicas = pd.read_csv('./Data/Mapa_Distancia_IPS_Publicas.csv')
df_mapa_ips = pd.read_csv('./Data/Mapa_Distancia_IPS.csv')


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias a IPS Publicas
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

width_mapa_distancia = 950
width_mapa_distancia_poblacion = 1000

locations = df_mapa_ips_publicas['Municipio_Departamento']

fig_mapa_ips_publicas_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips_publicas['Distancia_IPS_Nivel_1'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia a IPS Pública de Nivel 1",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_publicas_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900,
)

graph_fig_mapa_ips_publicas_n1 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_publicas_n1)
    ]
)

fig_mapa_ips_publicas_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips_publicas['Distancia_IPS_Nivel_2'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia a IPS Pública de Nivel 2",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_publicas_n2.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900
)

graph_fig_mapa_ips_publicas_n2 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_publicas_n2)
    ]
)

fig_mapa_ips_publicas_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips_publicas['Distancia_IPS_Nivel_3'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia a IPS Pública de Nivel 3",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_publicas_n3.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900
)

graph_fig_mapa_ips_publicas_n3 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_publicas_n3)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias Poblacion a IPS Publicas
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

locations = df_mapa_ips_publicas['Municipio_Departamento']

fig_mapa_poblacion_ips_publicas_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips_publicas['Distancia_Poblacion_IPS_Nivel_1'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 1",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_publicas_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=900
)

graph_fig_mapa_poblacion_ips_publicas_n1 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_publicas_n1)
    ]
)

fig_mapa_poblacion_ips_publicas_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips_publicas['Distancia_Poblacion_IPS_Nivel_2'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 2",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_publicas_n2.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=900
)

graph_fig_mapa_poblacion_ips_publicas_n2 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_publicas_n2)
    ]
)

fig_mapa_poblacion_ips_publicas_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips_publicas['Distancia_Poblacion_IPS_Nivel_3'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 3",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_publicas_n3.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=900
)

graph_fig_mapa_poblacion_ips_publicas_n3 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_publicas_n3)
    ]
)

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias a IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

width_mapa_distancia = 950
width_mapa_distancia_poblacion = 1000

locations = df_mapa_ips['Municipio_Departamento']

fig_mapa_ips_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips['Distancia_IPS_Nivel_1'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia a IPS de Nivel 1",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900,
)

graph_fig_mapa_ips_n1 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_n1)
    ]
)

fig_mapa_ips_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips['Distancia_IPS_Nivel_2'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia a IPS de Nivel 2",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_n2.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900
)

graph_fig_mapa_ips_n2 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_n2)
    ]
)

fig_mapa_ips_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips['Distancia_IPS_Nivel_3'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia a IPS de Nivel 3",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_n3.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900
)

graph_fig_mapa_ips_n3 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_n3)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias Poblacion a IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

locations = df_mapa_ips['Municipio_Departamento']

fig_mapa_poblacion_ips_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips['Distancia_Poblacion_IPS_Nivel_1'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia*Poblacion a IPS de Nivel 1",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=900
)

graph_fig_mapa_poblacion_ips_n1 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_n1)
    ]
)

fig_mapa_poblacion_ips_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips['Distancia_Poblacion_IPS_Nivel_2'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia*Poblacion a IPS de Nivel 2",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_n2.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=900
)

graph_fig_mapa_poblacion_ips_n2 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_n2)
    ]
)

fig_mapa_poblacion_ips_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_ips['Distancia_Poblacion_IPS_Nivel_3'],
        colorscale=[
            "#fff",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe2e2e",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        [
            "#b62020",
        ]*1,
        colorbar_title="Distancia*Poblacion a IPS de Nivel 3",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_n3.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=900
)

graph_fig_mapa_poblacion_ips_n3 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_n3)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Layout
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

indicadores_layout = html.Div(children=[

    # Barra de Navegación
    navigation.navbar,

    html.Br(),


    # -------------------------------------------------------------------------------------------------------------------
    # Sección IPS Publicas Distancias
    # -------------------------------------------------------------------------------------------------------------------

    html.Div(
        children=[
            html.H2(
                'Distancia a IPS Pública más Cercana por Nivel',
                style={
                    'text-align': 'center'
                }
            ),
            html.P(
                children=[
                    '''
                    Con el propósito de analizar el acceso a las IPS Públicas en cada municipio, se llevará a cabo un estudio focalizado en las distancias que deben recorrer los residentes para acceder a una IPS de un nivel de complejidad.
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
            html.P(
                children=[
                    '''
                    Con el propósito de analizar el acceso a las IPS Públicas en cada municipio, se llevará a cabo un estudio focalizado en las distancias que deben recorrer los residentes para acceder a una IPS de un nivel de complejidad.
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
            html.P(
                children=[
                    '''
                    Este análisis proporcionará una visión más detallada de la distribución de las IPS Públicas, teniendo en cuenta tanto su clasificación por complejidad como la ubicación geográfica de los municipios, lo cual será fundamental para comprender la accesibilidad de los servicios de salud en los municipios y las regiones y poder tomar decisiones orientadas a satisfacer las necesidades de las poblaciones más afectadas.
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

    html.Br(),

    # Fila 1 Mapas - Distancia N1 vs Distancia*Poblacion N1
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Distancia a IPS Pública de Nivel 1'
                    ),
                    graph_fig_mapa_ips_publicas_n1,
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
                    html.H5(
                        'Distancia Ponderada por Población a IPS Pública de Nivel 1'
                    ),
                    graph_fig_mapa_poblacion_ips_publicas_n1,
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
            'justify-content': 'space-between',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),

    # Fila 2 Mapas - Distancia N2 vs Distancia*Poblacion N2
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Distancia a IPS Pública de Nivel 2'
                    ),
                    graph_fig_mapa_ips_publicas_n2,
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
                    html.H5(
                        'Distancia Ponderada por Población a IPS Pública de Nivel 2'
                    ),
                    graph_fig_mapa_poblacion_ips_publicas_n2,
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
            'justify-content': 'space-between',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),

    # Fila 3 Mapas - Distancia N3 vs Distancia*Poblacion N3
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Distancia a IPS Pública de Nivel 3'
                    ),
                    graph_fig_mapa_ips_publicas_n3,
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
                    html.H5(
                        'Distancia Ponderada por Población a IPS Pública de Nivel 3'
                    ),
                    graph_fig_mapa_poblacion_ips_publicas_n3,
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
            'justify-content': 'space-between',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),

    html.Br(),


    # -------------------------------------------------------------------------------------------------------------------
    # Sección IPS - Distancias
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
                    Una de las principales limitantes al comparar las IPS entre sí es que no todas tienen la misma capacidad tecnológica, de personal médico y de instalaciones. Ante esta situación se delimitaron como vimos anteriormente una clasificación por complejidades: Baja (1), Mediana (2), Alta(3). Sin embargo, unicamente las IPS con naturaleza jurídica Pública se encuentran con esta clasificación, volviendo incomparables las IPS públicas, privadas y mixtas.
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
            html.P(
                children=[
                    '''
                    Para lidiar con esta situación se creó un modelo de Machine Learning que pueda clasificar cualquier tipo de IPS (pública, privada, mixta) según sus capacidades instaladas tales como:
                    ''',
                    html.Ul(
                        children=[
                            html.Li('Camas'),
                            html.Li('Consultorios'),
                            html.Li('Ambulancias'),
                            html.Li('Consultorios de Urgencias'),
                            html.Li('Camillas'),
                            html.Li('Salas de Cirugía'),
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
                    Ahora que podemos comparar las IPS directamente sin importar su naturaleza jurídica podemos ver las distancias que debe recorrer una persona en un municipio para ir a un municipio con una IPS de determinada complejidad: Baja (1), Mediana (2), Alta(3).
                    '''
                ],
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
        ],
        style={
            # 'width': '80%',
            'display': 'flex',
            'flex-direction': 'column',
            'justify-content': 'center',
            'align-items': 'center',
        }
    ),

    html.Br(),

    # Fila 1 Mapas - Distancia N1 vs Distancia*Poblacion N1
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Distancia a IPS de Nivel 1'
                    ),
                    graph_fig_mapa_ips_n1,
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
                    html.H5(
                        'Distancia Ponderada por Población a IPS de Nivel 1'
                    ),
                    graph_fig_mapa_poblacion_ips_n1,
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
            'justify-content': 'space-between',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),

    # Fila 2 Mapas - Distancia N2 vs Distancia*Poblacion N2
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Distancia a IPS de Nivel 2'
                    ),
                    graph_fig_mapa_ips_n2,
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
                    html.H5(
                        'Distancia Ponderada por Población a IPS de Nivel 2'
                    ),
                    graph_fig_mapa_poblacion_ips_n2,
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
            'justify-content': 'space-between',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),

    # Fila 3 Mapas - Distancia N3 vs Distancia*Poblacion N3
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H5(
                        'Distancia a IPS de Nivel 3'
                    ),
                    graph_fig_mapa_ips_n3,
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
                    html.H5(
                        'Distancia Ponderada por Población a IPS de Nivel 3'
                    ),
                    graph_fig_mapa_poblacion_ips_n3,
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
            'justify-content': 'space-between',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),



])
