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
                       ], className='icon-shape icon-sm icon-shape-tertiary rounded me-3',
                        style={'background-color': '#FFDBCC', 'color': '#D95050'},
                        ),
                        html.Div([
                            html.Label("Average Error Rate", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='average-error-rate')
                        ], className='d-block')
                    ], className='d-flex align-items-center me-5'),

                     html.Div([
                        html.Div([
                            ICON.CHART_LINE
                        ], className='icon-shape icon-sm icon-shape-secondary rounded me-3',
                        style={'background-color': '#EDF1F9', 'color': '#A0B2D9'}  # D8DAE6, 9BAFB8
                        ),
                        html.Div([
                            html.Label("Adjusted R-Squared", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='adjusted-r-squared')
                        ], className='d-block')
                    ], className='d-flex align-items-center pt-3'),
                    
                    html.H2("Underlying Estimates", className='fs-6 fw-bold mt-3'),
                    html.Div([
                        html.Div([
                            ICON.DATABASE
                        ], className='icon-shape icon-sm icon-shape-secondary rounded me-3',
                        style={'background-color': '#F2F4F6', 'color': '#C8CBDC'}  # D8DAE6
                        ),
                        html.Div([
                            html.Label("Number of Indicators", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='indicators-count')
                        ], className='d-block')
                    ], className='d-flex align-items-center'),
                    html.Div([
                        html.Div([
                            ICON.HEXAGON
                        ], className='icon-shape icon-sm icon-shape-purple rounded me-3',
                        style={'background-color': '#EEEEEC', 'color': '#C5C8B8'}
                        ),
                        html.Div([
                            html.Label("Number of Models", className='mb-0'),
                            html.H4("Not Available", className='mb-0', id='models-count')
                        ], className='d-block')
                    ], className='d-flex align-items-center pt-3')


                ], className='d-block')
            ], className='card-body')
        ], className='card border-0 shadow')
    ], className='col-12 mb-4')

