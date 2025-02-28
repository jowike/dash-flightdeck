from dash import html

from ..icons.hero import ICON

def acquisition():
    return html.Div([
        html.Div([
            html.Div([
                html.H2("Model Assessment", className='fs-5 fw-bold mb-1'),
                html.P("Gives you an overview of the key evaluation metrics for predictive analytics to effectively assess the quality of nowcasts."),
                html.Div([
                    html.Div([
                        html.Div([
                            ICON.TRIANGLE_EXCLAMATION
                       ], className='icon-shape icon-sm icon-shape-danger rounded me-3',
                        ),
                        html.Div([
                            html.Label("Average Error Rate", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='average-error-rate')
                        ], className='d-block')
                    ], className='d-flex align-items-center me-5'),
                    html.Div([
                        html.Div([
                            ICON.FIRE.ME2
                        ], className='icon-shape icon-sm icon-shape-secondary rounded me-3',
                        style={'background-color': '#FBEAD6', 'color': '#FFC900'},  # F8BD7A
                        # style={'background-color': '#ECEEEB', 'color': '#464A4D'}
                        ),
                        html.Div([
                            html.Label("Adjusted R-Squared", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='adjusted-r-squared')
                        ], className='d-block')
                    ], className='d-flex align-items-center pt-3'),
                    html.H2("Underlying Estimates", className='fs-6 fw-bold mt-3'),
                    html.Div([
                        html.Div([
                            ICON.GLOBE.ME0
                        ], className='icon-shape icon-sm icon-shape-tertiary rounded me-3', style={'background-color': '#EAE2E3', 'color': '#50270C'}),
                        html.Div([
                            html.Label("Number of Indicators", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='indicators-count')
                        ], className='d-block')
                    ], className='d-flex align-items-center'),
                    html.Div([
                        html.Div([
                            ICON.HEXAGON
                        ], className='icon-shape icon-sm icon-shape-purple rounded me-3'),
                        html.Div([
                            html.Label("Number of Models", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='models-count')
                        ], className='d-block')
                    ], className='d-flex align-items-center pt-3')




                ], className='d-block')
            ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 mb-4')

