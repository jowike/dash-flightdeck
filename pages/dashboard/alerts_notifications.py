from dash import html, dcc


def alertsNotifications():
    return  html.Div([
        html.H2("Alerts & Notifications", className="h5 mb-4"),
        html.Ul([
            # TODO: 
            html.Li([
                html.Div([
                    html.H3("Data Flow", className="h6 mb-1"),
                    html.P("Get the most recent update watermark from the data repository.", className="small pe-4"),
                    html.P("Data as of Date: 4/5/2024 7:15 PM CET", className="small pe-4")
                ]),
            ], className="list-group-item d-flex align-items-center justify-content-between px-0 border-bottom"),
            html.Li([
                html.Div([
                    html.H3("Nowcast", className="h6 mb-1"),
                    html.P("Monitor the real-time status of the model refinery.", className="small pe-4"),
                    html.P("Last Run Date: 4/5/2024 7:15 PM CET", className="small pe-4"),
                    html.P(id="pipeline-status", className="pipeline-status small pe-4"),
                    # html.Div(id="pipeline-status", className="pipeline-status", style={"margin-top": "20px"})
                ]),
                # html.Div([
                #     html.Div(id="pipeline-status", className="pipeline-status", style={"margin-top": "20px"})
                # ])
            ], className="list-group-item d-flex align-items-center justify-content-between px-0 border-bottom"),
         ], className="list-group list-group-flush")
    ], className="card card-body border-0 shadow mb-4 mb-xl-0")