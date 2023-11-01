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

capacidad = dbc.Card(
    [
        dbc.CardImg(
            src="/assets/capacidad.jpeg",
            top=True,
            style={"opacity": 0.3},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Capacidad Instalada", className="card-title"),
                    html.P(
                        "Analisis de la capacidad instalada del sector salud de Colombia por departamento y tipo de servicio",
                        className="card-text",
                    ),
                    dbc.Button("Capacidad Instalada", size="lg", id="inicio_capacidad", href="/capacidad",
                       style={'margin-right': '10px', 'verticalAlign': 'middle'}),
                ],
            ),
        ),
    ],
    style={"width": "18rem"},
)

contratacion = dbc.Card(
    [
        dbc.CardImg(
            src="/assets/contratacion.jpeg",
            top=True,
            style={"opacity": 0.3},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4("Contratacion", className="card-title"),
                    html.P(
                        "Analisis de los contratos de salud publica realizados por el estado.",
                        className="card-text",
                    ),
                    dbc.Button("Contratación", size="lg", id="inicio_contratos", href="/contratos",
                       style={'margin-left': '10px', 'verticalAlign': 'middle'}),
                ],
            ),
        ),
    ],
    style={"width": "20rem"},
)

inicio_layout = html.Div(children=[

    #Barra de Navegación
    navigation.navbar,
    html.Br(),

    #Titulo de la pagina
    html.H1(children = '''Bienvenido al Tablero de Servicios de Salud de Colombia.''',
            style={'textAlign': 'center'}),
    html.Br(),

    html.Br(),

    #Parrafo
    html.Div(children=[
        html.Div(children=[
            html.Pre(texto, style={'text-align': 'center','padding':'1px'})
        ], style={'margin-left': '10px'})
    ],
    style={'display': 'flex',
           'align-items': 'center',
           'justify-content': 'flex-start',
           'margin-left': '130px'}),

    html.Br(),

    dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(capacidad),
                dbc.Col(contratacion)
                ]),
        ],
    fluid=True
    ),

    html.Br(),

    html.Div(html.Pre(texto3, style={'text-align': 'center'}))
])