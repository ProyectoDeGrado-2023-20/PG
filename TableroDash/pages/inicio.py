from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''El sector de salud y protección social es un ámbito complejo y vital para
cualquier sociedad. Por esta razón, comprender los patrones de contratación que se
llevan a cabo en este sector es fundamental para mejorar su funcionamiento y garantizar
una atención adecuada a las personas que lo necesitan. Por medio de la investigación,
se busca obtener un conocimiento profundo de las prácticas de contratación en el sector
de salud y protección social, identificando las fortalezas y debilidades del sistema actual.
Se busca presentar la herramienta realizada a personas expertas en el sector con el objetivo
de tener una retroalimentación sobre los indicadores que se considerar y que tan acertada es
la aplicación a partir de su experiencia.'''

texto3 = 'Aplicación creada por Santiago González y Juliana Cárdenas.'

inicio_layout = html.Div(children=[

    #Barra de Navegación
    navigation.navbar,
    html.Br(),

    #Titulo de la pagina
    html.H1(children = '''Bienvenido al Tablero de Servicios de Salud de Colombia''',
            style={'textAlign': 'center'}),
    html.Br(),

    html.Br(),

    #Parrafo
    html.Div(children=[
        html.Img(src='/assets/salud-publica.png', style={'height': '20%', 'width': '20%','margin-right':'10px'}),
        html.Div(children=[
            html.Pre(texto, style={'text-align': 'center','padding':'1px'})
        ], style={'margin-left': '10px'})
    ],
    style={'display': 'flex',
           'align-items': 'center',
           'justify-content': 'flex-start',
           'margin-left': '130px'}),
    html.Br(),
    html.Br(),
    #Botones para ir de la pagina de inicio a las instrucciones y programa
    html.Div(children=[
        html.Div(children=[
            dbc.Button("Capacidad Instalada", size="lg", id="inicio_instrucciones", href="/instrucciones",
                       style={'margin-right': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'}),
        html.Div(children=[
            dbc.Button("Contratación", size="lg", id="inicio_programa", href="/programa",
                       style={'margin-left': '10px', 'verticalAlign': 'middle'})],
            style={'display': 'inline-flex'})],
        style={'margin-bottom': '10px',
              'display': 'flex',
              'justify-content': 'center'}),
    html.Br(),
    html.Div(html.Pre(texto3, style={'text-align': 'center'}))
])