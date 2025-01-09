# Video:    [Bootstrap Alerts & Modals - Dash Plotly](https://youtu.be/X3OuhqS8ueM)
# Docs:     [Dash Bootstrap Components:](https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/)
#           [Dash Bootstrap Themes:](https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/)
#           [Dash HTML/CORE Components:](https://dash.plotly.com/dash-html-components)
import dash
from dash import Dash, dcc, html, Input, Output, State           # pip install dash
import dash_bootstrap_components as dbc         # pip install dash_bootstrap_components
import plotly.express as px
import pandas as pd


def modal():
    return html.Div(
    [
        # dbc.Button("Add comment", id="open"),

        dbc.Modal([
            dbc.ModalHeader(
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.ModalTitle("Configuration Sources"), 
                            width="auto"  # Ensures the title takes up only the necessary space
                        ),
                        # dbc.Col(
                        #     tableAction(), 
                        #     width="auto",  # Ensures the action takes up only the necessary space
                        #     className="text-end pe-4"  # Aligns content to the right
                        # ),
                    ],
                    justify="between",  # Spreads the columns to opposite sides
                    align="center",     # Vertically aligns content in the row
                    className="w-100"
                )
            ),
            dbc.ModalBody(
                dbc.Form(
                    [
                        dbc.Row(
                            [
                                # dbc.Label("Name property", className="mt-1"),
                                # dbc.Input(type="text", placeholder="Specify the name of the parameter"),
                                dbc.Label("Parameters", className="mt-1"),
                                dcc.Textarea(
                                    id='textarea-example',
                                    value='Textarea content initialized\nwith multiple lines of text',
                                    style={'width': '100%', 'height': 35},
                                ),
                            ],
                            className="mb-2",
                        ),
                        # dbc.Row(
                        #     [
                        #         dbc.Label("Lorem ipsum", className="mt-1"),
                        #         dbc.Input(type="email", placeholder="Enter ..."),
                        #     ],
                        #     className="mb-2",
                        # ),
                        dbc.Row(
                            [
                                # dbc.Label("Value", className="mt-1"),
                                # dbc.Input(type="text", placeholder="Enter parameter value"),
                                dbc.Label("Data Catalog", className="mt-1"),
                                dcc.Textarea(
                                    id='textarea-example',
                                    value='Another textarea content initialized\nwith multiple lines of text',
                                    style={'width': '100%', 'height': 35},
                                ),
                            ],
                            className="mb-2",
                        ),
                        dbc.Button("Save", color="primary"),
                    ],
                )
            ),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),

        ],
            id="modal",
            is_open=False,    # True, False
            size="xl",        # "sm", "lg", "xl"
            backdrop=True,    # True, False or Static for modal to not be closed by clicking on backdrop
            scrollable=True,  # False or True if modal has a lot of text
            centered=True,    # True, False
            fade=True         # True, False
        ),
    ]
)






