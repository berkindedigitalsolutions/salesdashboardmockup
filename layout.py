

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
import dash_bootstrap_components as dbc

#making some changes
header = html.Div(
        className = "row mb-2 p-4",
        style = {'background':'#ce9d2a','color':'#FFF','marginLeft':'0','marginRight':'0'},
        children = [
            
            html.H1(style={'marginRight':'0'}, children="DG VOLO & COMPANY"),


])


########################## GRAPHS ##################################################
customer_intelligence_fig = dcc.Graph(
    figure=go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h')))


#####################################################################################
customer_intelligence_progress = html.Div(
    className="col-8",
    children = [
        html.H5(className="medium font-weight-bold",children='Key Account Plans Created'),
        dbc.Progress("70%",className="mb-4",style={"height": "20px","font-size":"12px"}, value=70),
        html.H5(className="medium font-weight-bold",children='Date of Last Purchase'),
        dbc.Progress("40%",className="mb-4",style={"height": "20px","font-size":"12px"}, value=40),
        html.H5(className="medium font-weight-bold",children='Incumbant Vendor'),
        dbc.Progress("15%",className="mb-4",style={"height": "20px","font-size":"12px"}, value=15),
        html.H5(className="medium font-weight-bold",children='Purchase Occasion Identified'),
        dbc.Progress("10%",className="mb-4",style={"height": "20px","font-size":"12px"}, value=10),
        html.H5(className="medium font-weight-bold",children='Key Decision Maker'),
        dbc.Progress("18%",className="mb-4",style={"height": "20px","font-size":"12px"}, value=18),


    ]
)




salesMetrics = html.Div(
    className="row p-4 mb-2",
    children = [
        html.Div(className = "col-lg-4", children = [
            html.H2(className="mb-4",children="Sales Process"),
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
            html.H2(className="mb-4",children="Sales Activity"),
            html.Div(className="row",children=[
                    html.Div(className = "col-lg-12 mb-4", children = [
                    html.Div(className="card shadow",children=[
                        html.Div(className="card-header",children=html.H4("Customer Intelligence")),
                        html.Div(className="card-body",children=customer_intelligence_progress)

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
            html.H2(className="mb-4",children="Sales Results"),
                html.Div(className="row",children=[
                        html.Div(className = "col-lg-12 mb-4", children = [
                        html.Div(className="card shadow",children=[
                            html.Div(className="card-header",children=html.H4("Revenue vs Budget")),
                            html.Div(className="card-body",
                                children= daq.Gauge(
                                        color={"gradient":True,"ranges":{"green":[12,20],"yellow":[8,12],"red":[0,8]}},
                                        value=8,
                                        label='$8 MM',
                                        max=20,
                                        min=0,
                                    )  
                                )

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

