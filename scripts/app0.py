import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd
import exploratory
from dash.dependencies import Input, Output

#data reading
df0, iris =exploratory.strt() #


# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Intialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
             # This div contains a header H1, a dropdown to select the kind of plot and the plot
            html.H1("Different kinds of plots"),
            dcc.Dropdown(
                        id='p1',
                        options=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'],
                        value= 'sepal length (cm)'),
            dcc.Graph(id='cbox_p1')
])

@app.callback(
    Output('cbox_p1', 'figure'),
    Input('p1', 'value'))
def update_figure0(selected_variable):
    fig0 = exploratory.cbox(df0, selected_variable)
    return fig0

if __name__ == '__main__':  
    app.run_server(debug=True) 