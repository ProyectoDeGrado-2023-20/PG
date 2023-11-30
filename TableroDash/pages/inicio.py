from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

titulo = """
Análisis de los Servicios de Salud en Colombia
"""

texto_introduccion = """
La salud es crucial para el bienestar social y el desarrollo de las naciones. En Colombia,
el sistema de salud ha experimentado avances, pero persisten desigualdades. Actualmente, el
país debate la reforma propuesta por el presidente Gustavo Petro. Este investigación analiza el
sistema de salud colombiano, centrándose en las Instituciones Prestadoras de Servicios de Salud
(IPS), como centros de salud, hospitales y clínicas. Se utilizarán bases de datos como el REPS y
el SIHO para proporcionar una visión integral de la configuración y funcionamiento del sistema. Se
abordarán problemas al comparar IPS debido a su naturaleza jurídica, proponiendo un modelo de Machine
Learning para extender la clasificación. También se analizará la evolución de la infraestructura
sanitaria entre 2002 y 2022 a nivel nacional y por departamento. La investigación busca contribuir al
entendimiento del sistema de salud colombiano y guiar decisiones futuras para mejorar la eficiencia
y calidad de los servicios.
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
        'height': '500 px',
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
