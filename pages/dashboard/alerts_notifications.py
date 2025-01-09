from dash import html, dcc
from dash_spa.components.dropdown_aio import DropdownAIO
import dash_bootstrap_components as dbc         # pip install dash_bootstrap_components

def tableAction():

    button = DropdownAIO.Button([
        html.Span(html.Span(className='fas fa-ellipsis-h icon-dark'), className='icon icon-sm'),
        html.Span("Toggle Dropdown", className='visually-hidden')
    ], className='btn btn-link text-dark dropdown-toggle-split m-0 p-0')

    # Action column dropdown bottom-left. Ripped from the Volt transactions table using Firefox debug tools

    style={
        "position": "absolute",
        "inset": "0px 0px auto auto",
        "margin": "0px",
        "transform": "translate3d(0px, 25.3333px, 0px)"
        }

    container = html.Div([
        html.A([html.Span(className='fas fa-project-diagram me-2'), "View Details" ], id="start-viz-button", n_clicks=0, className='dropdown-item rounded-top'),
        html.A([html.Span(className='fas fa-stop me-2'), "Stop" ], id="stop-viz-button", n_clicks=0, className='dropdown-item rounded-bottom')
    ], className='dropdown-menu py-0', style=style)

    return html.Div(DropdownAIO(button, container, id='manage-kedro-viz-button'), className='btn-group')


def alertsNotifications():
    return  html.Div([
        html.H2("Alerts & Notifications", className="h5 mb-4"),
        html.Ul([
            html.Li([
                html.Div([
                    html.H3("Data Flow", className="h6 mb-1"),
                    html.P("Get the most recent update watermark from the data repository.", className="small pe-4"),
                    html.P("Data as of Date: 4/5/2024 7:15 PM CET", className="small pe-4")
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
                            dbc.Col(
                                tableAction(), 
                                width="auto",  # Ensures the action takes up only the necessary space
                                className="d-flex justify-content-end align-items-center ms-auto"  # Pushes to the far right
                            ),
                        ],
                        className="g-0 w-100"  # Removes gutters and ensures full-width row
                    ),
                    html.P("Monitor the real-time status of the model refinery.", className="small pe-4"),
                    html.P("Last Run Date: 4/5/2024 7:15 PM CET", className="small pe-4"),
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