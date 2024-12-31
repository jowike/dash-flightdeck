from dash import html, dcc
from dash_chartist import DashChartist

data = {
    "labels": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    "series": [ 
        [0, 10, 30, 40, 80, 60, 100],
        [1, 11, 29, 41, 79, 65, ]
          ]
}

options = {
    'low': 0,
    'showArea': False,
    'fullWidth': True,
    'axisX': {
        # On the x-axis start means top and end means bottom
        'position': 'end',
        'showGrid': True
        },
    'axisY': {
        # On the y-axis start means left and end means right
        'showGrid': False,
        'showLabel': False,
        }
    }

chartType = 'Line'

def _chartHeader():
    return  html.Div([
        html.Div([
            html.Div("Nowcast Browser", className='fs-5 fw-normal mb-2'),
            html.H2("$15,567", className='fs-3 fw-extrabold'),
            html.Div([
                html.Span("Since last month", className='fw-normal me-2'),
                html.Span(className='fas fa-angle-up text-success'),
                html.Span("2.57%", className='text-success fw-bold')
            ], className='small mt-2')
        ], className='d-block mb-3 mb-sm-0'),
        html.Div([
            dcc.Link("Base", href='#', className='btn btn-secondary text-dark btn-sm me-2'),
            dcc.Link("Adjusted", href='#', className='btn btn-sm me-3')
        ], className='d-flex ms-auto')
    ], className='card-header d-sm-flex flex-row align-items-center flex-0')


def salesChart():
    return  html.Div([
        html.Div([
            _chartHeader(),
            html.Div([
                DashChartist(
                    className='ct-chart-sales-value ct-double-octave',
                    type=chartType,
                    options=options,
                    tooltips=True,
                    data=data,
                    )
            ], className='card-body p-2')
        ], className='card border-0')
    ], className='col-12 mb-4')
