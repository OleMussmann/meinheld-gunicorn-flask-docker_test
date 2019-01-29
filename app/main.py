import dash
import flask
import dash_html_components as html

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app)

dash_app.layout = html.Div([html.H3('Hello World')])
dash_app.title = "mytitle"

@app.route("/")
def index():
    return dash_app
