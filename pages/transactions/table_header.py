from dash import html, dcc
from dash_svg import Svg, Path

def tableHeader():
    return html.Div([
        html.Div([
            # Search orders
            html.Div([
                html.Div([
                    html.Span([
                        Svg([
                            Path(fillRule='evenodd', d='M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', clipRule='evenodd')
                        ], className='icon icon-xs', xmlns='http://www.w3.org/2000/svg', viewBox='0 0 20 20', fill='currentColor', **{"aria-hidden": "true"})
                    ], className='input-group-text'),
                    dcc.Input(type='text', className='form-control', placeholder='Search orders')
                ], className='input-group me-2 me-lg-3 fmxw-400')
            ], className='col col-md-6 col-lg-3 col-xl-4'),
            # Table Settings
            html.Div([
                html.Div([
                    html.Button([
                        Svg([
                            Path(fillRule='evenodd', d='M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z', clipRule='evenodd')
                        ], className='icon icon-sm', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg'),
                        html.Span("Toggle Dropdown", className='visually-hidden')
                    ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-1', **{"data-bs-toggle": "dropdown", "aria-haspopup": "true", "aria-expanded": "false"}),
                    html.Div([
                        html.Span("Show", className='small ps-3 fw-bold text-dark'),
                        html.A([
                            "10",
                            Svg([
                                Path(fillRule='evenodd', d='M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z', clipRule='evenodd')
                            ], className='icon icon-xxs ms-auto', fill='currentColor', viewBox='0 0 20 20', xmlns='http://www.w3.org/2000/svg')
                        ], className='dropdown-item d-flex align-items-center fw-bold', href='#'),
                        html.A("20", className='dropdown-item fw-bold', href='#'),
                        html.A("30", className='dropdown-item fw-bold rounded-bottom', href='#')
                    ], className='dropdown-menu dropdown-menu-xs dropdown-menu-end pb-0')
                ], className='dropdown')
            ], className='col-4 col-md-2 col-xl-1 ps-md-0 text-end')
        ], className='row align-items-center justify-content-between')
    ], className='table-settings mb-4')
