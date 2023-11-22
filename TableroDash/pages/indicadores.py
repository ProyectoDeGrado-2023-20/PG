# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Libraries
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from dash import html
from apps import navigation
import dash_bootstrap_components as dbc
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from app import app
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

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

locations = df_mapa_ips_publicas['Municipio_Departamento']
fig_mapa = go.Figure(
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
        colorbar_title="Distancia a IPS de Nivel 1 más cercana"
        # color
    )
)

fig_mapa.update_layout(
    mapbox_style="white-bg",
    # mapbox_style="carto-positron",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=1000,
    height=900
)

graph = html.Div(
    [
        dcc.Graph(figure=fig_mapa)
    ]
)
# fig_mapa.show()

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Layout
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

indicadores_layout = html.Div(children=[

    # Barra de Navegación
    navigation.navbar,

    html.Br(),

    graph,

])
