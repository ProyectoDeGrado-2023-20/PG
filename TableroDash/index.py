from dash import html
from dash import dcc
from dash.dependencies import Input, Output #callback

from app import app
from pages import inicio,programa

url_contente_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div")
])

app.layout = url_contente_layout

app.validation_layout = html.Div([
    url_contente_layout,
    inicio.inicio_layout
])

@app.callback(Output(component_id='output-div', component_property='children'),
              [Input(component_id='url', component_property='pathname')])
def update_output_div(pathname):
    if pathname == '/programa':
        return programa.programa_layout
    else:
        return inicio.inicio_layout

if __name__ == "__main__":
    app.run_server(debug=True)