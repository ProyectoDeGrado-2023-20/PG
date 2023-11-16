from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''Contratos'''

texto3 = 'Aplicación creada por Santiago González y Juliana Cárdenas.'

indicadores_layout = html.Div(children=[

    # Barra de Navegación
    navigation.navbar,
    html.Br()

])
