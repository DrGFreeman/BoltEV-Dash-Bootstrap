import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import  pandas as pd
import plotly_express as px

days = pd.read_csv("data/data.csv")

dash_link = html.A("Plotly Dash", href="https://plot.ly/dash/")
dbc_link = html.A("Dash-Bootstrap-Components", href="https://dash-bootstrap-components.opensource.faculty.ai/")
damdlbt_link = html.A("Damien de la Bruère-Terreault", href="https://github.com/DamdlBT/BoltEV-Dash")

lead_text = "Données de consommation énergétique d'une voiture Chevrolet Bolt EV 100% électrique utilisée au Québec."

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Code source sur GitHub", href="https://github.com/DrGFreeman/BoltEV-Dash-Bootstrap"))
    ],
    brand="BOLT EV - Efficacité et Autonomie",
    color="primary",
    dark=True
)

layout = html.Div(
    children=[
        navbar,
        dbc.Container(
            children=[
                dbc.Row(
                    dbc.Col(
                        children=[
                            html.P(lead_text, className="lead"),
                        ],
                    ),
                ),
                dbc.Row(
                    children=[
                        dbc.Col([
                            html.Label('Variable x'),
                            dcc.Dropdown(
                                id="x",
                                options=[
                                    {"label": c, "value": c} for c in sorted(days.columns)
                                ],
                                placeholder="choisir la variable",
                                value="date",
                            )],
                            width=4
                        ),
                        dbc.Col([
                            html.Label('Variable y'),
                            dcc.Dropdown(
                                id="y",
                                options=[
                                    {"label": c, "value": c} for c in sorted(days.columns)
                                ],
                                placeholder="choisir la variable",
                                value="consommation (kWh/100km)",
                            )],
                            width=4
                        ),
                        dbc.Col([
                            html.Label('Variable couleur'),
                            dcc.Dropdown(
                                id="couleur",
                                options=[
                                    {"label": c, "value": c} for c in sorted(days.columns)
                                ],
                                placeholder="choisir la variable",
                                value="temp. ext. moyenne (deg.C)",
                            )],
                            width=4
                        ),
                    ]
                ),
                dbc.Row(
                    dbc.Col([
                        dcc.Graph(id="graph")
                    ])
                ),
                html.Hr(),
                dbc.Row(
                    dbc.Col(
                        children=[
                            html.Div(
                                children=[
                                    html.P([
                                        "Basée sur la démo d'application utilisant ", dash_link,
                                        " par ", damdlbt_link , ".",
                                        " Cette version utilise le module ", dbc_link,
                                        " pour les styles CSS."],
                                        className="small"
                                    ),
                                ]
                            ),
                        ],
                    ),
                ),  
            ],
            className="mt-5"
        ),
    ],
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Bolt EV"

app.layout = layout

@app.callback(Output("graph", "figure"),
              [Input('x', 'value'),
               Input("y", "value"),
               Input("couleur", "value")])
def update_graph(x, y, couleur):
    fig = px.scatter(days, x=x, y=y, color=couleur, hover_data=days.columns)
    return fig               

if __name__ == '__main__':

    app.server.run(debug=True)