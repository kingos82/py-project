import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
from scripts import exploratory
from dash.dependencies import Input, Output

#data reading
df0, iris =exploratory.strt() #
print(df0.columns)

# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
title_style = {
    'textAlign' : 'center',
    'color' : 'black'
}


print("initializing app")
# Intialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
print("initializing server")
server = app.server
print("initializing layout")
app.layout = html.Div([
             # This div contains a header H1, a dropdown to select the kind of plot and the plot
                html.H1("Iris Dashboard", style=title_style),  

                html.Div([
                    html.Div([
                        html.P("select the first variable"),
                        dcc.Dropdown(
                                id='p1',
                                options=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
                                value= 'sepal length (cm)'),
                            ], className="six columns"),
                    html.Div([
                        html.P("select the second variable"),
                        dcc.Dropdown(
                                id='p2',
                                options=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
                                value= 'petal width (cm)')                                
                            ], className="six columns"),
                    ], className="row"),
                    
                html.Div([ 
                    html.Div([               
                        dcc.Graph(id='cbox_p1'),
                            ], className="four columns"),
                    html.Div([
                        dcc.Graph(id='cscat_p1_p2'),
                            ], className="four columns"),
                    html.Div([
                    dcc.Graph(id='cbox_p2')
                            ], className="four columns")
                        ], className="row")
                    ])

@app.callback(
    Output('cbox_p1', 'figure'),
    Input('p1', 'value'))
def update_figure0(selected_variable):
    fig0 = exploratory.cbox(df0, selected_variable)
    return fig0

@app.callback(
    Output('cbox_p2', 'figure'),
    Input('p2', 'value'))
def update_figure1(selected_variable):
    fig1 = exploratory.cbox(df0, selected_variable)
    return fig1

@app.callback(
    Output('cscat_p1_p2', 'figure'),
    Input('p1', 'value'),
    Input('p2', 'value'))
def update_figure2(p1, p2):
    fig2 = exploratory.cscat(df0, p1, p2)
    return fig2

if __name__ == '__main__':  
    app.run_server(debug=True) 