from dash import html, dcc
import dash_bootstrap_components as dbc         # pip install dash_bootstrap_components


def alertsNotifications():
    return  html.Div([
        html.H2("Alerts & Notifications", className="h5 mb-4"),
        html.Ul([
            html.Li([
                html.Div([
                    html.H3("Data Flow", className="h6 mb-1"),
                    html.P("Get the most recent update watermark from the data repository.", className="small pe-4"),
                    html.P("Data as of Date: ", className="small pe-4", id="data-as-of-date"),
                ]),
            ], className="list-group-item d-flex align-items-center justify-content-between px-0 border-bottom"),
            html.Li([
                html.Div([
                    dbc.Row(
                        [
                            dbc.Col(
                                html.H3("Nowcast", className="h6 mb-1"),
                                width="auto",  # Ensures the title takes up only the necessary space
                                className="d-flex align-items-center"  # Vertically aligns the title
                            ),
                            # dbc.Col(
                            #     tableAction(), 
                            #     width="auto",  # Ensures the action takes up only the necessary space
                            #     className="d-flex justify-content-end align-items-center ms-auto"  # Pushes to the far right
                            # ),
                        ],
                        className="g-0 w-100"  # Removes gutters and ensures full-width row
                    ),
                    html.P("Monitor the real-time status of the model refinery.", className="small pe-4"),
                    html.P("Last Run Watermark: ", className="small pe-4", id="nowcast-as-of-date"),
                    html.P(id="pipeline-status", className="pipeline-status small pe-4"),
                    html.P(id="pipeline-viz", className="pipeline-status small pe-4"),
                    # html.Div(id="pipeline-status", className="pipeline-status", style={"margin-top": "20px"})
                ]),
                # html.Div([
                #     html.Div(id="pipeline-status", className="pipeline-status", style={"margin-top": "20px"})
                # ])
            ], className="list-group-item d-flex align-items-center justify-content-between px-0 border-bottom"),
         ], className="list-group list-group-flush")
    ], className="card card-body border-0 shadow mb-4 mb-xl-0")