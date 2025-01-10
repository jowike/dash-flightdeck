from dash import html
from dash_spa import register_page, prefix

from .common import topNavBar, footer, buttonBar
from .dashboard import (
    salesChart,
    customers,
    revenue,
    bounceRate,
    pageVisitsTable,
    totalOrdersBarChart,
    acquisition,
    newTasksButton,
    runButton,
    alertsNotifications,
    modal,
    upload_modal
)


import sys

register_page(__name__, path="/pages/dashboard", title="Dash/Flightdeck - Dashboard")
sys.path.append(
    "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/dependencies/"
)

layout = html.Main(
    [
        topNavBar(),
        buttonBar(newTasksButton(), runButton()),
        modal(),
        upload_modal(),
        html.Div([salesChart(), customers(), revenue(), bounceRate()], className="row"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                pageVisitsTable(),
                                acquisition(),
                            ],
                            className="row",
                        )
                    ],
                    className="col-12 col-xl-8",
                ),
                html.Div(
                    [totalOrdersBarChart(), alertsNotifications()],
                    className="col-12 col-xl-4",
                ),
            ],
            className="row",
        ),
        footer(),
    ],
    className="content",
)
