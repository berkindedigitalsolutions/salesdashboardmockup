
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#from users import users_info
import flask
import json
import dash_daq as daq
from dash.dependencies import Input, Output
from datetime import datetime
import dash_table
import pandas as pd
import numpy as np
from layout import header,salesMetrics, salesMetricResults
import os
########### Define your variables

tabtitle='DGV Sales Dashboard'

##### PATH TESTING




########### Initiate the app
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    dcc.Location(id='url',refresh=False),
    header,
    salesMetrics,
    salesMetricResults,

    ]
)





########################################################### CALLBACKS ############################################################################

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
