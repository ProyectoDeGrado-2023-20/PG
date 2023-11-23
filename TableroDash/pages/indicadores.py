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
        colorbar_title="Distancia a IPS Pública de Nivel 1"
    )
)

fig_mapa_ips_publicas_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=900
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
        colorbar_title="Distancia a IPS Pública de Nivel 1"
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
        colorbar_title="Distancia a IPS Pública de Nivel 3"
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
        colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 1"
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
        colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 1"
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
        colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 3"
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
# Layout
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

indicadores_layout = html.Div(children=[

    # Barra de Navegación
    navigation.navbar,

    html.Br(),

    # Sección Distancias
    html.H2(
        'Distancia a IPS Pública más Cercana por Nivel',
        style={
            'text-align': 'center'
        }
    ),



    # Fila 1 Mapas - Distancia N1 vs Distancia*Poblacion N1
    html.Div(
        children=[
            graph_fig_mapa_ips_publicas_n1,
            graph_fig_mapa_poblacion_ips_publicas_n1,
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'width': '100%'
            # 'overflow': 'hidden',
        }

    ),

    # Fila 1 Mapas - Distancia N1 vs Distancia*Poblacion N1
    html.Div(
        children=[
            graph_fig_mapa_ips_publicas_n2,
            graph_fig_mapa_poblacion_ips_publicas_n2,
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'width': '100%'
            # 'overflow': 'hidden',
        }

    ),

    # Fila 1 Mapas - Distancia N1 vs Distancia*Poblacion N1
    html.Div(
        children=[
            graph_fig_mapa_ips_publicas_n3,
            graph_fig_mapa_poblacion_ips_publicas_n3,
        ],
        style={
            'display': 'flex',
            'justify-content': 'center',
            'width': '100%'
            # 'overflow': 'hidden',
        }

    ),


])
