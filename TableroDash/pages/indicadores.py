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
# Barras Departamento - Numero y Numero por cada mil habitantes

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
# Barras Departamento - Numero y Numero por cada mil habitantes


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
# Barras Departamento - Numero y Numero por cada mil habitantes


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

locations = df_mapa_numero_ips_municipios['Municipio_Departamento']
fig_mapa_numero_ips_municipios = go.Figure(
    go.Choroplethmapbox(
        geojson=geojson_municipios,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_numero_ips_municipios['IPS_2022'],
        colorscale=[
            "#b62020",
        ]*1 +
        [
            "#cb2424",
        ]*1 +
        # [
        #     "#fe2e2e",
        # ]*1 +
        [
            "#fe5757",
        ]*5 +
        [
            "#fe8181",
        ]*5 +
        # [
        #     "#fff",
        # ]*100 +
        [
            "#b3cde0",
        ]*90 +
        [
            "#6497b1",
        ]*900 +
        [
            "#005b96",
        ]*1000 +
        # [
        #     "#03396c",
        # ]*1 +
        [
            "#011f4b",
        ]*1000,
        # ["#d05447", "#A2CDE2", "#3364C7", "#3364C7"],
        # colorbar_title="Numero IPS"
        # color
    )
)

fig_mapa_numero_ips_municipios.update_layout(
    mapbox_style="white-bg",
    # mapbox_style="carto-positron",
    mapbox_zoom=4,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=640,
    height=800
)


fig_mapa_numero_ips_municipios.update_layout(
    title='Número de IPS por Municipio'
)

graph_mapa_numero_ips_municipios = html.Div(
    [
        dcc.Graph(figure=fig_mapa_numero_ips_municipios)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS por Habitantes - Municipios

locations = df_mapa_numero_ips_municipios['Municipio_Departamento']
fig_mapa_numero_ips_habitantes_municipios = go.Figure(
    go.Choroplethmapbox(
        geojson=geojson_municipios,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_numero_ips_municipios['IPS/Habitantes'],
        colorscale=[
            "#b62020",
        ]*1 +
        # [
        #     "#cb2424",
        # ]*1 +
        # [
        #     "#fe2e2e",
        # ]*1 +
        [
            "#fe5757",
        ]*1 +
        [
            "#fe8181",
        ]*1 +
        # [
        #     "#fff",
        # ]*1 +
        [
            "#b3cde0",
        ]*5 +
        [
            "#6497b1",
        ]*5 +
        [
            "#005b96",
        ]*5 +
        [
            "#03396c",
        ]*10 +
        [
            "#011f4b",
        ]*10,

        # ["#d05447", "#A2CDE2", "#3364C7", "#3364C7"],
        # colorbar_title="Numero IPS por cada 100 mil habitantes"
        # color
    )
)

fig_mapa_numero_ips_habitantes_municipios.update_layout(
    mapbox_style="white-bg",
    # mapbox_style="carto-positron",
    mapbox_zoom=4,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=640,
    height=800
)


fig_mapa_numero_ips_habitantes_municipios.update_layout(
    title='Número de IPS por cada 100 mil Habitantes por Municipio'
)

graph_mapa_numero_ips_municipios_habitantes = html.Div(
    [
        dcc.Graph(figure=fig_mapa_numero_ips_habitantes_municipios)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Naturaleza Juridica IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# Numero IPS - Naturaleza Juridica

color_palette = {
    'Privada': '#3364C7',
    'Pública': '#8CBCB9',
    'Mixta': '#826251'
}

fig_ips_naturaleza_juridica = px.bar(df_ips_naturaleza_juridica,
                                     x='Category',
                                     y='IPS_2022',
                                     color='NaturalezaJuridica',
                                     barmode='stack',
                                     width=450,
                                     height=500,
                                     color_discrete_map=color_palette,
                                     title='Número de IPS por Naturaleza Juridica - 2022',
                                     )

fig_ips_naturaleza_juridica.update_yaxes(range=[0, 20000])
fig_ips_naturaleza_juridica.update_xaxes(title_text='')
fig_ips_naturaleza_juridica.update_yaxes(title_text='Número IPS')

fig_ips_naturaleza_juridica.update_layout(legend_title_text='Legends', legend=dict(
    title=dict(text='Naturaleza Jurídica')))

graph_ips_naturaleza_juridica = html.Div(
    [
        dcc.Graph(figure=fig_ips_naturaleza_juridica)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Porcentaje IPS - Naturaleza Juridica

color_palette = {
    'Privada': '#3364C7',
    'Pública': '#8CBCB9',
    'Mixta': '#826251'
}

fig_ips_naturaleza_juridica_porcentaje = px.bar(df_ips_naturaleza_juridica,
                                                x='Category',
                                                y='Porcentaje',
                                                color='NaturalezaJuridica',
                                                barmode='stack',
                                                width=450,
                                                height=500,
                                                color_discrete_map=color_palette,
                                                title='Porcentaje de IPS por Naturaleza Juridica - 2022',
                                                )

fig_ips_naturaleza_juridica_porcentaje.update_yaxes(range=[0, 100])
fig_ips_naturaleza_juridica_porcentaje.update_xaxes(title_text='')
fig_ips_naturaleza_juridica_porcentaje.update_yaxes(
    title_text='Porcentaje (%)')

fig_ips_naturaleza_juridica_porcentaje.update_layout(legend_title_text='Legends', legend=dict(
    title=dict(text='Naturaleza Jurídica')))

graph_ips_naturaleza_juridica_porcentaje = html.Div(
    [
        dcc.Graph(figure=fig_ips_naturaleza_juridica_porcentaje)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Numero IPS - Naturaleza Juridica - Departamento

color_palette = {
    'Privada': '#3364C7',
    'Pública': '#8CBCB9',
    'Mixta': '#826251'
}

fig_ips_naturaleza_juridica_numero_departamento = px.bar(data_frame=df_naturaleza_juridica_departamento,
                                                         x='Numero_IPS',
                                                         y='Departamento',
                                                         color='NaturalezaJuridica',
                                                         orientation='h',
                                                         color_discrete_map=color_palette)

fig_ips_naturaleza_juridica_numero_departamento.update_xaxes(
    title_text='Número de IPS')
fig_ips_naturaleza_juridica_numero_departamento.update_xaxes(range=[0, 3100])
fig_ips_naturaleza_juridica_numero_departamento.update_yaxes(
    title_text='Departamento')
fig_ips_naturaleza_juridica_numero_departamento.update_layout(
    title='Número de IPS por Departamento por Naturaleza Juridica- 2022')
fig_ips_naturaleza_juridica_numero_departamento.update_layout(
    legend_title_text='Legends', legend=dict(title=dict(text='Naturaleza Jurídica')))
fig_ips_naturaleza_juridica_numero_departamento.update_layout(
    width=800, height=700)

graph_ips_naturaleza_juridica_numero_departamento = html.Div(
    [
        dcc.Graph(figure=fig_ips_naturaleza_juridica_numero_departamento)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Porcentaje IPS - Naturaleza Juridica - Departamento

color_palette = {
    'Privada': '#3364C7',
    'Pública': '#8CBCB9',
    'Mixta': '#826251'
}

fig_ips_naturaleza_juridica_porcentaje_departamento = px.bar(data_frame=df_naturaleza_juridica_departamento,
                                                             x='Porcentaje_IPS',
                                                             y='Departamento',
                                                             color='NaturalezaJuridica',
                                                             orientation='h',
                                                             color_discrete_map=color_palette)

fig_ips_naturaleza_juridica_porcentaje_departamento.update_xaxes(range=[
                                                                 0, 100])
fig_ips_naturaleza_juridica_porcentaje_departamento.update_xaxes(
    title_text='Porcentaje Naturaleza Juridica (%)')
fig_ips_naturaleza_juridica_porcentaje_departamento.update_yaxes(
    title_text='Departamento')
fig_ips_naturaleza_juridica_porcentaje_departamento.update_layout(
    title='Distribucion Naturaleza Juridica IPS por Departamento - 2022')
fig_ips_naturaleza_juridica_porcentaje_departamento.update_layout(
    legend_title_text='Legends', legend=dict(title=dict(text='Naturaleza Jurídica')))
fig_ips_naturaleza_juridica_porcentaje_departamento.update_layout(
    width=800, height=700)

graph_ips_naturaleza_juridica_porcentaje_departamento = html.Div(
    [
        dcc.Graph(figure=fig_ips_naturaleza_juridica_porcentaje_departamento)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias a IPS Publicas
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

width_mapa_distancia = 640
width_mapa_distancia_poblacion = 640

locations = df_mapa_distancia_ips['Municipio_Departamento']


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

fig_mapa_ips_publicas_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_distancia_ips['Distancia_IPS_Nivel_1_Publicas'],
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
        # colorbar_title="Distancia a IPS Pública de Nivel 1",
        # zmin=0,
        # zmax=950,
    )
)

fig_mapa_ips_publicas_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia,
    height=800,
)


fig_mapa_ips_publicas_n1.update_layout(
    title='Distancia a IPS Pública de Nivel 1 (Km)'
)

graph_fig_mapa_ips_publicas_n1 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_ips_publicas_n1)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

# fig_mapa_ips_publicas_n2 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_IPS_Nivel_2_Publicas'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia a IPS Pública de Nivel 2",
#         # zmin=0,
#         # zmax=950,
#     )
# )

# fig_mapa_ips_publicas_n2.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia,
#     height=900
# )

# graph_fig_mapa_ips_publicas_n2 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_ips_publicas_n2)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

# fig_mapa_ips_publicas_n3 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_IPS_Nivel_3_Publicas'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia a IPS Pública de Nivel 3",
#         # zmin=0,
#         # zmax=950,
#     )
# )

# fig_mapa_ips_publicas_n3.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia,
#     height=900
# )

# graph_fig_mapa_ips_publicas_n3 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_ips_publicas_n3)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias Poblacion a IPS Publicas
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

locations = df_mapa_distancia_ips['Municipio_Departamento']


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

fig_mapa_poblacion_ips_publicas_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
        locations=locations,
        featureidkey='properties.key',
        z=df_mapa_distancia_ips['Distancia_Poblacion_IPS_Nivel_1_Publicas'],
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
        # colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 1",
        # zmin=0,
        # zmax=115e6,
    )
)

fig_mapa_poblacion_ips_publicas_n1.update_layout(
    mapbox_style="white-bg",
    mapbox_zoom=4,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=width_mapa_distancia_poblacion,
    height=800
)


fig_mapa_poblacion_ips_publicas_n1.update_layout(
    title='Distancia*Poblacion a IPS Pública de Nivel 1'
)

graph_fig_mapa_poblacion_ips_publicas_n1 = html.Div(
    [
        dcc.Graph(figure=fig_mapa_poblacion_ips_publicas_n1)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

# fig_mapa_poblacion_ips_publicas_n2 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_Poblacion_IPS_Nivel_2_Publicas'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 2",
#         # zmin=0,
#         # zmax=115e6,
#     )
# )

# fig_mapa_poblacion_ips_publicas_n2.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia_poblacion,
#     height=900
# )

# graph_fig_mapa_poblacion_ips_publicas_n2 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_poblacion_ips_publicas_n2)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

# fig_mapa_poblacion_ips_publicas_n3 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_Poblacion_IPS_Nivel_3_Publicas'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia*Poblacion a IPS Pública de Nivel 3",
#         # zmin=0,
#         # zmax=115e6,
#     )
# )

# fig_mapa_poblacion_ips_publicas_n3.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia_poblacion,
#     height=900
# )

# graph_fig_mapa_poblacion_ips_publicas_n3 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_poblacion_ips_publicas_n3)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias a IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

width_mapa_distancia = 950
width_mapa_distancia_poblacion = 1000

locations = df_mapa_distancia_ips['Municipio_Departamento']


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

# fig_mapa_ips_n1 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_IPS_Nivel_1_Modelo'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia a IPS de Nivel 1",
#         # zmin=0,
#         # zmax=950,
#     )
# )

# fig_mapa_ips_n1.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia,
#     height=900,
# )

# graph_fig_mapa_ips_n1 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_ips_n1)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

# fig_mapa_ips_n2 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_IPS_Nivel_2_Modelo'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia a IPS de Nivel 2",
#         # zmin=0,
#         # zmax=950,
#     )
# )

# fig_mapa_ips_n2.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia,
#     height=900
# )

# graph_fig_mapa_ips_n2 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_ips_n2)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

# fig_mapa_ips_n3 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_IPS_Nivel_3_Modelo'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia a IPS de Nivel 3",
#         # zmin=0,
#         # zmax=950,
#     )
# )

# fig_mapa_ips_n3.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia,
#     height=900
# )

# graph_fig_mapa_ips_n3 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_ips_n3)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Mapa Distancias Poblacion a IPS
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

locations = df_mapa_distancia_ips['Municipio_Departamento']


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

# fig_mapa_poblacion_ips_n1 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_Poblacion_IPS_Nivel_1_Modelo'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia*Poblacion a IPS de Nivel 1",
#         # zmin=0,
#         # zmax=115e6,
#     )
# )

# fig_mapa_poblacion_ips_n1.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia_poblacion,
#     height=900
# )

# graph_fig_mapa_poblacion_ips_n1 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_poblacion_ips_n1)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

# fig_mapa_poblacion_ips_n2 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_Poblacion_IPS_Nivel_2_Modelo'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia*Poblacion a IPS de Nivel 2",
#         # zmin=0,
#         # zmax=115e6,
#     )
# )

# fig_mapa_poblacion_ips_n2.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia_poblacion,
#     height=900
# )

# graph_fig_mapa_poblacion_ips_n2 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_poblacion_ips_n2)
#     ]
# )


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

# fig_mapa_poblacion_ips_n3 = go.Figure(

#     go.Choroplethmapbox(
#         geojson=geojson_municipios,
#         locations=locations,
#         featureidkey='properties.key',
#         z=df_mapa_distancia_ips['Distancia_Poblacion_IPS_Nivel_3_Modelo'],
#         colorscale=[
#             "#fff",
#         ]*1 +
#         [
#             "#fe8181",
#         ]*1 +
#         [
#             "#fe5757",
#         ]*1 +
#         [
#             "#fe2e2e",
#         ]*1 +
#         [
#             "#cb2424",
#         ]*1 +
#         [
#             "#b62020",
#         ]*1,
#         colorbar_title="Distancia*Poblacion a IPS de Nivel 3",
#         # zmin=0,
#         # zmax=115e6,
#     )
# )

# fig_mapa_poblacion_ips_n3.update_layout(
#     mapbox_style="white-bg",
#     mapbox_zoom=4.3,
#     mapbox_center={"lat": 43.5, "lon": -62.3},
#     width=width_mapa_distancia_poblacion,
#     height=900
# )

# graph_fig_mapa_poblacion_ips_n3 = html.Div(
#     [
#         dcc.Graph(figure=fig_mapa_poblacion_ips_n3)
#     ]
# )


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
                'Análisis del Número de IPS en Colombia',
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
                    El primer indicador para analizar la distribución de las Instituciones Prestadoras de Salud (IPS) en Colombia es el número de IPS que hay por cada Departamento. Sin embargo, este indicador no tiene en cuenta que es normal que las ciudades más grandes y los departamentos más poblados concentran la mayoría de las IPS.
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
                    Por lo tanto, se decide calcular una razón que relacione el número de IPS y la población de cada departamento. De esto surge el número de IPS por cada 100 mil habitantes.
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
            # 'flex-wrap': 'wrap',
            # 'justify-content': 'center',
            'justify-content': 'start',
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
                    A pesar de que con el indicador por departamentos es posible hacerse una idea de cuales son los departamentos en los que hacen falta mayor presencia de Instituciones Prestadoras de Salud este es un nivel de abstracción demasiado alto.
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
                    En consecuencia, es necesario tomar los mismos indicadores pero con un nivel de granuladidad más alto. En este caso, profundizamos de departamentos a los municipios en Colombia.
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
            # 'flex-wrap': 'wrap',
            # 'justify-content': 'center',
            'justify-content': 'start',
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
                    Logramos desagregar los indicadores en varios factores: población, departamentos y municipios. Sin embargo, hasta ahora no hemos tomado en cuenta las diferencias entre cada IPS, es decir, las capacidades físicas, tecnológicas, médicas de cada una.
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
                    Para atacar esta situación se ha definido una clasificación por el nivel de complejidad de la IPS, dividiendose en:
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
                    Sin embargo, esta clasificación solo existe para las IPS cuya Naturaleza Jurídica es Pública. Por lo que es necesario entender cúal es la distribucion de todas las IPS por naturaleza jurídica.
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
            # 'flex-wrap': 'wrap',
            # 'justify-content': 'center',
            'justify-content': 'start',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),


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
            # 'flex-wrap': 'wrap',
            # 'justify-content': 'center',
            'justify-content': 'start',
            'width': '100%'
            # 'overflow': 'hidden',
        }
    ),
])
