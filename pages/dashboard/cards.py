from dash import html

from ..icons.hero import ICON

def cardFrame(content):
    return html.Div([
        html.Div([
            html.Div([
                html.Div(content, className='row d-block d-xl-flex align-items-center')
            ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 col-sm-6 col-xl-4 mb-4')



def customers():
    return cardFrame([
        html.Div([
            html.Div([
                ICON.CHART
            ], className='icon-shape icon-shape-primary rounded me-4 me-sm-0'),
            html.Div([
                html.H2("Confidence Interval", className='h5'),
                html.H3("345,678", className='fw-extrabold mb-1')
            ], className='d-sm-none')
        ], className='col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center'),
        html.Div([
            html.Div([
                html.H2("Confidence Interval", className='h6 text-gray-400 mb-0'),
                html.H3("345k", className='fw-extrabold mb-2')
            ], className='d-none d-sm-block'),
            html.Small([
                "Feb 1 - Apr 1,",
                ICON.GLOBE.ME1,
                "USA"
            ], className='d-flex align-items-center text-gray-500'),
            html.Div([
                html.Div([
                    "Since last month",
                    ICON.CHEVRON_UP_DOWN,
                    html.Span("0.2%", className='text fw-bolder')
                ])
            ], className='small d-flex mt-1')
        ], className='col-12 col-xl-7 px-xl-0')
    ])


def revenue():
    return cardFrame([
        html.Div([
            html.Div([
                ICON.CHART
            ], className='icon-shape icon-shape-secondary rounded me-4 me-sm-0'),
            html.Div([
                html.H2("VAR", className='fw-extrabold h5'),
                html.H3("$15,488", className='mb-1')
            ], className='d-sm-none')
        ], className='col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center'),
        html.Div([
            html.Div([
                html.H2("VAR", className='h6 text-gray-400 mb-0'),
                html.H3("$15,488", className='fw-extrabold mb-2')
            ], className='d-none d-sm-block'),
            html.Small([
                "Feb 1 - Apr 1,",
                ICON.GLOBE.ME1,
                "GER"
            ], className='d-flex align-items-center text-gray-500'),
            html.Div([
                html.Div([
                    "Since last month",
                    ICON.DOWN_ARROW.XS,
                    html.Span("2%", className='text-danger fw-bolder')
                ])
            ], className='small d-flex mt-1')
        ], className='col-12 col-xl-7 px-xl-0')
    ])


def bounceRate():
    return cardFrame([
        html.Div([
            html.Div([
                ICON.CHART
            ], className='icon-shape icon-shape-tertiary rounded me-4 me-sm-0'),
            html.Div([
                html.H2("ARIMA", className='fw-extrabold h5'),
                html.H3("$15,757", className='mb-1')
            ], className='d-sm-none')
        ], className='col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center'),
        html.Div([
            html.Div([
                html.H2("ARIMA", className='h6 text-gray-400 mb-0'),
                html.H3("$15,757", className='fw-extrabold mb-2')
            ], className='d-none d-sm-block'),
            html.Small("Feb 1 - Apr 1", className='text-gray-500'),
            html.Div([
                html.Div([
                    "Since last month",
                    ICON.UP_ARROW.XS,
                    html.Span("4%", className='text-success fw-bolder')
                ])
            ], className='small d-flex mt-1')
        ], className='col-12 col-xl-7 px-xl-0')
    ])
