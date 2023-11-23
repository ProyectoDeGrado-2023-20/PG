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

file_path = './Data/Colombia_Departamentos_Modified.json'
with open(file_path, 'r') as file:
    geojson_departamentos = json.load(file)

file_path = './Data/Colombia_Municipios_Modified.json'
with open(file_path, 'r') as file:
    geojson_municipios = json.load(file)


df_mapa_ips_publicas = pd.read_csv('./Data/Mapa_Distancia_IPS_Publicas.csv')
df_mapa_ips = pd.read_csv('./Data/Mapa_Distancia_IPS.csv')

df_ips_por_departamentos = pd.read_csv('./Data/IPS_por_Departamentos_2022.csv')
df_ips_por_departamentos_habitantes = pd.read_csv(
    './Data/IPS_por_Departamentos_Habitantes_2022.csv')

df_mapa_numero_ips = pd.read_csv('./Data/Mapa_Numero_IPS.csv')
df_mapa_numero_ips_municipios = pd.read_csv(
    './Data/Mapa_Numero_IPS_Municipios.csv')

df_ips_naturaleza_juridica = pd.read_csv(
    './Data/Distribucion_Naturaleza_Juridica_IPS.csv')
df_ips_naturaleza_juridica['Category'] = ''

df_naturaleza_juridica_numero_departamento = pd.read_csv(
    './Data/Naturaleza_Juridica_Numero_IPS.csv')
df_naturaleza_juridica_porcentaje_departamento = pd.read_csv(
    './Data/Naturaleza_Juridica_Porcentaje_IPS.csv')

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Numero IPS e IPS por Habitantes
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------
# Numero de IPS - Departamentos

fig_numero_ips = px.bar(data_frame=df_ips_por_departamentos,
                        x='IPS_2022',
                        y='Departamento',
                        orientation='h')

fig_numero_ips.update_xaxes(title_text='Número de IPS')
fig_numero_ips.update_xaxes(range=[0, 3100])
fig_numero_ips.update_yaxes(title_text='Departamento')
fig_numero_ips.update_layout(title='Número de IPS por Departamento - 2022')

color_sequence = ['#3364C7' for i in df_ips_por_departamentos['Departamento']]
fig_numero_ips.update_traces(marker=dict(color=color_sequence))

fig_numero_ips.update_traces(
    text=df_ips_por_departamentos['IPS_2022'], textposition='outside')

fig_numero_ips.update_layout(width=800, height=700)


graph_numero_ips_departamento = html.Div(
    [
        dcc.Graph(figure=fig_numero_ips)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Numero IPS por Habitantes - Departamentos

fig_ips_por_habitantes = px.bar(data_frame=df_ips_por_departamentos_habitantes,
                                x='IPS/Habitantes',
                                y='Departamento',
                                orientation='h')

fig_ips_por_habitantes.update_xaxes(
    title_text='IPS por cada 100 mil habitantes')
fig_ips_por_habitantes.update_yaxes(title_text='Departamento')
fig_ips_por_habitantes.update_layout(
    title='Número de IPS por cada 100 mil habitantes por Departamento - 2022')

color_sequence = [
    '#3364C7' for i in df_ips_por_departamentos_habitantes['Departamento']]
fig_ips_por_habitantes.update_traces(marker=dict(color=color_sequence))

fig_ips_por_habitantes.update_traces(
    text=df_ips_por_departamentos_habitantes['IPS/Habitantes'], textposition='outside')


fig_ips_por_habitantes.update_layout(width=800, height=700)

graph_numero_ips_departamento_por_habitantes = html.Div(
    [
        dcc.Graph(figure=fig_ips_por_habitantes)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS - Departamentos

locations = df_mapa_numero_ips['Departamento_DANE']
fig_mapa_numero_ips = go.Figure(
    go.Choroplethmapbox(
        geojson=geojson_departamentos,
        locations=locations,
        featureidkey='properties.Departamento',
        # featureidkey='properties.NOMBRE_DPT',
        z=df_mapa_numero_ips['IPS_2022'],
        # colorscale='RdBu',
        # colorscale=["#d05447", "#f6f7f7", "#A2CDE2", "#307AB6", "#3364C7"],
        colorscale=[
            "#b62020",
        ]*1 +
        # [
        #     "#cb2424",
        # ]*1 +
        # [
        #     "#fe2e2e",
        # ]*1 +
        # [
        #     "#fe8181",
        # ]*1 +
        # [
        #     "#fff",
        # ]*1 +
        [
            "#b3cde0",
        ]*1 +
        [
            "#6497b1",
        ]*1 +
        [
            "#005b96",
        ]*1 +
        [
            "#03396c",
        ]*1 +
        [
            "#011f4b",
        ]*1,

        # ["#d05447", "#A2CDE2", "#3364C7", "#3364C7"],
        colorbar_title="Numero IPS"
        # color
    )
)

fig_mapa_numero_ips.update_layout(
    # mapbox_style="carto-positron",
    mapbox_style="white-bg",
    mapbox_zoom=4.7,
    mapbox_center={"lat": 4.570868, "lon": -74.2973328},
    width=900,
    height=900
)

graph_mapa_numero_ips_departamento = html.Div(
    [
        dcc.Graph(figure=fig_mapa_numero_ips)
    ]
)


# -------------------------------------------------------------------------------------------------------------------
# Mapa Numero IPS por Habitantes - Departamentos

locations = df_mapa_numero_ips['Departamento_DANE']
fig_mapa_numero_ips_habitantes = go.Figure(
    go.Choroplethmapbox(
        geojson=geojson_departamentos,
        locations=locations,
        featureidkey='properties.Departamento',
        # featureidkey='properties.NOMBRE_DPT',
        z=df_mapa_numero_ips['IPS/Habitantes'],
        # colorscale='RdBu',
        # colorscale=["#d05447", "#f6f7f7", "#A2CDE2", "#307AB6", "#3364C7"],
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
            "#fe8181",
        ]*1 +
        # [
        #     "#fff",
        # ]*1 +
        [
            "#b3cde0",
        ]*1 +
        [
            "#6497b1",
        ]*1 +
        [
            "#005b96",
        ]*1 +
        [
            "#03396c",
        ]*1 +
        [
            "#011f4b",
        ]*1,

        # ["#d05447", "#A2CDE2", "#3364C7", "#3364C7"],
        colorbar_title="Numero IPS por cada 100 mil habitantes"
        # color
    )
)

fig_mapa_numero_ips_habitantes.update_layout(
    # mapbox_style="carto-positron",
    mapbox_style="white-bg",
    mapbox_zoom=4.7,
    mapbox_center={"lat": 4.570868, "lon": -74.2973328},
    width=1000,
    height=900
)

graph_mapa_numero_ips_departamento_habitantes = html.Div(
    [
        dcc.Graph(figure=fig_mapa_numero_ips_habitantes)
    ]
)


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
        colorbar_title="Numero IPS"
        # color
    )
)

fig_mapa_numero_ips_municipios.update_layout(
    mapbox_style="white-bg",
    # mapbox_style="carto-positron",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=900,
    height=900
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
        colorbar_title="Numero IPS por cada 100 mil habitantes"
        # color
    )
)

fig_mapa_numero_ips_habitantes_municipios.update_layout(
    mapbox_style="white-bg",
    # mapbox_style="carto-positron",
    mapbox_zoom=4.3,
    mapbox_center={"lat": 43.5, "lon": -62.3},
    width=1000,
    height=900
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

fig_ips_naturaleza_juridica_numero_departamento = px.bar(data_frame=df_naturaleza_juridica_numero_departamento,
                                                         x='IPS_2022',
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

fig_ips_naturaleza_juridica_porcentaje_departamento = px.bar(data_frame=df_naturaleza_juridica_porcentaje_departamento,
                                                             x='IPS_2022',
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

width_mapa_distancia = 950
width_mapa_distancia_poblacion = 1000

locations = df_mapa_ips_publicas['Municipio_Departamento']


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

fig_mapa_ips_publicas_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

fig_mapa_ips_publicas_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

fig_mapa_ips_publicas_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

fig_mapa_poblacion_ips_publicas_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

fig_mapa_poblacion_ips_publicas_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

fig_mapa_poblacion_ips_publicas_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

fig_mapa_ips_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

fig_mapa_ips_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

fig_mapa_ips_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 1

fig_mapa_poblacion_ips_n1 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 2

fig_mapa_poblacion_ips_n2 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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


# -------------------------------------------------------------------------------------------------------------------
# Nivel 3

fig_mapa_poblacion_ips_n3 = go.Figure(

    go.Choroplethmapbox(
        geojson=geojson_municipios,
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
                    El indicador inicial más obvio para analizar la distribución de las Instituciones Prestadoras de Salud (IPS) en Colombia es el número de IPS que hay por cada Departamento. Sin embargo, este indicador no tiene en cuenta que es normal que las ciudades más grandes y los departamentos más poblados concentran la mayoría de las IPS.
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
            'justify-content': 'space-between',
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
            'justify-content': 'space-between',
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
            'justify-content': 'space-between',
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
