

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

#making some changes
header = html.Div(
        className = "row mb-2 p-4",
        style = {'background':'#ce9d2a','color':'#FFF','marginLeft':'0','marginRight':'0'},
        children = [
            
            html.H1(style={'marginRight':'0'}, children="DG VOLO & COMPANY"),


])