from dash import html, dcc 
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

import os
import sys
import pandas as pd
from config import parameters, data_catalog


register_page(__name__, path="/pages/dashboard", title="Dash/Flightdeck - Dashboard")


layout = html.Main(
    [
        dcc.Interval(
            id='interval-component',
            interval=5000,  # Check for file updates every 5 seconds
            n_intervals=0
        ),
        # Store for shared data
        dcc.Store(id='shared-data'),  # Store the shared data here
        topNavBar(),
        buttonBar(newTasksButton(), runButton()),
        modal(parameters=parameters, data_catalog=data_catalog),
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
