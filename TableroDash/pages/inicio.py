from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

titulo = """
Análisis de los Servicios de Salud en Colombia
"""

texto_introduccion = """
El sector de salud y protección social es un ámbito complejo y vital para
cualquier sociedad. Por esta razón, comprender los patrones de contratación que se
llevan a cabo en este sector es fundamental para mejorar su funcionamiento y garantizar
una atención adecuada a las personas que lo necesitan. Por medio de la investigación,
se busca obtener un conocimiento profundo de las prácticas de contratación en el sector
de salud y protección social, identificando las fortalezas y debilidades del sistema actual.
Se busca presentar la herramienta realizada a personas expertas en el sector con el objetivo
de tener una retroalimentación sobre los indicadores que se considerar y que tan acertada es
la aplicación a partir de su experiencia.
"""

texto_foot = """
Aplicación creada por Santiago González y Juliana Cárdenas
"""

indicadores = dbc.Card(
    [
        dbc.CardImg(
            src="/assets/monitor-cardiaco-real.jpg",
            top=True,
            style={
                "opacity": 0.2,
                # "height": 'inherit',
                # "object-fit": 'cover',
            },
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                children=[
                    html.H4(
                        "Indicadores - IPS",
                        className="card-title"
                    ),
                    html.P(
                        "Analisis y desarrollo de indicadores para el análisis de las Instituciones Prestadoras de Salud (IPS) y su ubicación a lo largo del territorio Colombiano.",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Indicadores",
                        size="lg",
                        id="inicio_contratos",
                        href="/indicadores",
                        style={
                            'margin-left': '10px',
                            'verticalAlign': 'middle'
                        }
                    ),
                ],
            ),
        ),
    ],
    style={
        "width": "30%",
        # 'height': 'auto',
    },
)

capacidad = dbc.Card(
    [
        dbc.CardImg(
            src="/assets/capacidad.jpeg",
            top=True,
            style={
                "opacity": 0.2,
                # "object-fit": 'cover'
            },
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.H4(
                        "Capacidad Instalada",
                        className="card-title"
                    ),
                    html.P(
                        "Analisis de la capacidad instalada del sector salud de Colombia por departamento",
                        className="card-text",
                    ),
                    dbc.Button(
                        "Capacidad Instalada",
                        size="lg",
                        id="inicio_capacidad",
                        href="/capacidad",
                        style={
                            'margin-right': '10px',
                            'verticalAlign': 'middle'
                        }
                    ),
                ],
            ),
        ),
    ],
    style={
        "width": "30%",
        # 'height': 'auto',
    },
)

inicio_layout = html.Div(children=[

    # Barra de Navegación
    navigation.navbar,

    html.Br(),

    html.Br(),

    # Titulo de la pagina
    html.H1(
        children=titulo,
        style={
            'textAlign': 'center'
        },
    ),

    html.Br(),

    html.Br(),

    # Parrafo Introduccion
    html.Div(
        children=[
            html.P(
                texto_introduccion,
                style={
                    'width': '80%',
                    'text-align': 'justify',
                }
            ),
        ],
        style={
            'display': 'flex',
            'width': '100%',
            'align-items': 'center',
            'justify-content': 'center',
            # 'background-image': 'url("/assets/capacidad.jpeg")'
        }
    ),

    html.Br(),

    html.Br(),

    # dbc.Container(
    #     [
    #         dbc.Row(
    #             [
    #                 dbc.Col(capacidad),
    #                 dbc.Col(contratacion)
    #             ]
    #         ),
    #     ],
    #     fluid=True
    # ),

    html.Div(
        children=[
            indicadores,
            capacidad,
        ],
        style={
            'width': '100%',
            'display': 'flex',
            # 'align-items': 'center',
            'justify-content': 'space-evenly'
        }
    ),

    html.Br(),

    html.Br(),

    # Footer
    html.Div(
        children=[
            html.P(
                texto_foot,
                style={
                    'width': '80%',
                    'text-align': 'center',
                }
            )
        ],
        style={
            'display': 'flex',
            'width': '100%',
            'align-items': 'center',
            'justify-content': 'center',
        }
    )
])
