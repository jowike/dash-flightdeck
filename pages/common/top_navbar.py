from dash import html, dcc
import dash_bootstrap_components as dbc

from ..icons.hero import ICON

def searchForm():
    return  html.Form([
        html.Div([
            html.Span([
                ICON.SEARCH
            ], className='input-group-text', id='topbar-addon'),
            dcc.Input(type='text', className='form-control', id='topbarInputIconLeft', placeholder='Search')
        ], className='input-group input-group-merge search-bar')
    ], className='navbar-search form-inline', id='navbar-search-main')

def infoControl():
    return html.Div(
        [
            # Info Icon
            html.Span(
                [
                    html.I(className="fas fa-info-circle me-2"),  # Replace with a proper icon (e.g., FontAwesome)
                    "Read Me ~ Your Guidebook",
                ],
                className="input-group-text",
                id="info-icon",  # ID for triggering modal
                style={"cursor": "pointer"},
            ),
            # Modal for Guidelines
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Guidelines")),
                    dbc.ModalBody(
                        [
                            html.P("Guideline 1: Lorem ipsum dolor sit amet."),
                            html.P("Guideline 2: Consectetur adipiscing elit."),
                            html.P("Guideline 3: Sed do eiusmod tempor incididunt."),
                            # TODO: Impacts of data releases (Data Flow)
                        ]
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal", className="ms-auto", n_clicks=0)
                    ),
                ],
                id="guidelines-modal",
                is_open=False,  # Initially hidden
            ),
        ],
        className="d-flex align-items-center",  # Align icon and modal trigger
    )

def topNavBar():
    """"Top navbar, search form ..."""
    return html.Nav([
        html.Div([
            html.Div([
                html.Div([
                    infoControl()
                ], className='d-flex align-items-center')
            ], className='d-flex justify-content-between w-100', id='navbarSupportedContent')
        ], className='container-fluid px-0')
    ], className='navbar navbar-top navbar-expand navbar-dashboard navbar-dark ps-0 pe-2 pb-0')
