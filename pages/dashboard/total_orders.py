from typing import List

from dash import html, dcc
from dash_spa import prefix, url_for, NOUPDATE
from dash_chartist import DashChartist
from dash_spa.components import SPA_LOCATION, TableContext
from dash_spa import trigger_index
from dash_spa.components.dropdown_button_aoi import DropdownButtonAIO, dropdownLink
from dash_spa.components.dropdown_aio import DropdownAIO
from dash_spa.components.button_container_aoi import ButtonContainerAIO
import dash_bootstrap_components as dbc

from ..icons.hero import ICON
from config import load_contributions, load_series


options = {
    "showArea": True,
    "fullWidth": True,
    "axisX": {
        # On the x-axis start means top and end means bottom
        "position": "end"
    },
    "axisY": {
        # On the y-axis start means left and end means right
        "showGrid": True,
        "showLabel": True,
    },
}

chartType = "Bar"
_, dropdown_options = load_contributions()


def totalOrdersBarChart():
    dropdown = html.Div(
                [
                    dbc.DropdownMenu(
                        label=html.I(className="fas fa-cog"),  # Remove default label
                        toggleClassName="btn btn-white dropdown-toggle d-flex align-items-center",
                        toggle_style={"border": "1px solid #ced4da", "borderRadius": "4px"},
                        children=[
                            dbc.DropdownMenuItem(option, id=f"option-{option}")
                            for option in dropdown_options
                        ],
                        id="dropdown-menu",
                        className="dropdown-menu-end dropdown-menu-xs",  # Menu styling
                        menu_variant="light",  # Dark menu style
                    ),
                ],
                className="dropdown",
            )

    header = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Span(
                                "Global Explanation",
                                className="h6 fw-normal text-gray me-auto",
                            ),  # Title
                        ],
                        className="d-flex align-items-center justify-content-between mb-2",
                    ),
                    html.H2("322.657", className="h3 fw-extrabold"),
                    html.Div(
                        [
                            html.Span("Since last month", className="fw-normal me-2"),
                            html.Span(className="fas fa-angle-up text-success me-1"),
                            html.Span("0.3%", className="text-success fw-bold"),
                        ],
                        className="small mt-2",
                    ),
                ],
                className="d-block",
            ),
            html.Div(
                [
                    html.Div(
                        dropdown,
                        className='d-flex align-items-center justify-content-between mb-4'
                        ),
                    html.Div(
                        [
                            html.Span(className="dot rounded-circle bg-gray-800 me-2"),
                            html.Span("TODO", className="fw-normal small"),
                        ],
                        className="d-flex align-items-center text-end mb-2",
                    ),
                    html.Div(
                        [
                            html.Span(className="dot rounded-circle bg-secondary me-2"),
                            html.Span("TODO", className="fw-normal small"),
                        ],
                        className="d-flex align-items-center text-end",
                    ),
                ],
                className="d-block ms-auto",
            ),
        ],
        className="card-header d-flex flex-row align-items-center flex-0 border-bottom",
    )

    return html.Div(
        [
            html.Div(
                [
                    header,
                    html.Div(
                        [
                            DashChartist(
                                className="ct-chart-ranking ct-golden-section ct-series-a",
                                type=chartType,
                                options=options,
                                data={},  # container.data,  # Initial state, to be overwritten on-click
                                id="global-explanation-chart",
                            )
                        ],
                        className="card-body p-2", id='global-explanation-table'
                    ),
                ],
                className="card border-0 shadow",
            )
        ],
        className="col-12 px-0 mb-4",
    )
