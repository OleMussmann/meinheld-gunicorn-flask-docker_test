import dash
import dash_html_components as html
import flask

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app)

dash_app.layout = html.Div([html.H3("abcde")])
