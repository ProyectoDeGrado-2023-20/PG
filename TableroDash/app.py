import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
app.title = 'Servicios Salud Colombia'
app._favicon = ("salud.ico")
server = app.server
