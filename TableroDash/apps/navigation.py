import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
import dash

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Img(
                                src=dash.get_asset_url(
                                    'logo.png'), height="40px"),
                            dbc.NavbarBrand(
                                "Servicios Salud Colombia", className="ms-2")
                        ],
                        width={"size": "auto"})
                ],
                align="center",
                className="g-0"),

            dbc.Row([
                dbc.Col([
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink("Inicio", href="/")),
                        dbc.NavItem(dbc.NavLink(
                                    "Indicadores", href="/indicadores")),
                        dbc.NavItem(dbc.NavLink(
                                    "Capacidad Instalada", href="/capacidad")),
                    ],
                        navbar=True
                    )
                ],
                    width={"size": "auto"})
            ],
                align="center"),
        ],
        fluid=True
    ),
    color="primary",
    dark=True
)
