

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

salesMetrics = html.Div(
    className="row p-4 mb-2",
    children = [
        html.Div(className = "col-lg-4", children = [
            html.H2(className="mb-2",children="Sales Process"),
            html.Div(className="row",children=[
                    html.Div(className = "col-lg-12 mb-4", children = [
                    html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Sales Process Metric 1")),
                        html.Div(className="card-body",children=html.H5("Card Body"))

                    ]),
                ]),
                html.Div(className = "col-lg-12 mb-4", children = [
                                    html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Sales Process Metric 2")),
                        html.Div(className="card-body",children=html.H5("Card Body"))

                    ]),
                ]),
                html.Div(className = "col-lg-12 mb-4", children = [
                        html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Sales Process Metric 3")),
                        html.Div(className="card-body",children=html.H5("Card Body"))

                    ]),
                ]),
            ]),
   
        ]),
        html.Div(className = "col-lg-4", children = [
            html.H2(className="mb-2",children="Sales Activity"),
            html.Div(className="row",children=[
                    html.Div(className = "col-lg-12 mb-4", children = [
                    html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Sales Activity Metric 1")),
                        html.Div(className="card-body",children=html.H5("Card Body"))

                    ]),
                ]),
                html.Div(className = "col-lg-12 mb-4", children = [
                                    html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Sales Activity Metric 2")),
                        html.Div(className="card-body",children=html.H5("Card Body"))

                    ]),
                ]),
                html.Div(className = "col-lg-12 mb-4", children = [
                        html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Sales Activity Metric 3")),
                        html.Div(className="card-body",children=html.H5("Card Body"))

                    ]),
                ]),
            ]),

        ]),
        html.Div(className = "col-lg-4", children = [
            html.H2(className="mb-2",children="Sales Result"),
                html.Div(className="row",children=[
                        html.Div(className = "col-lg-12 mb-4", children = [
                        html.Div(className="card shadow",children=[
                            html.Div(className="card-header",children=html.H4("Sales Result Metric 1")),
                            html.Div(className="card-body",children=html.H5("Card Body"))

                        ]),
                    ]),
                    html.Div(className = "col-lg-12 mb-4", children = [
                                        html.Div(className="card shadow",children=[
                            html.Div(className="card-header",children=html.H4("Sales Result Metric 2")),
                            html.Div(className="card-body",children=html.H5("Card Body"))

                        ]),
                    ]),
                    html.Div(className = "col-lg-12 mb-4", children = [
                            html.Div(className="card shadow",children=[
                            html.Div(className="card-header",children=html.H4("Sales Result Metric 3")),
                            html.Div(className="card-body",children=html.H5("Card Body"))

                        ]),
                    ]),
                ]),
            ])

])#end metrics

