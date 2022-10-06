import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
import exploratory


# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Intialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(html.H1("iris dashboard"))# some code with our layout

if __name__ == '__main__':  
    app.run_server(debug=True) 