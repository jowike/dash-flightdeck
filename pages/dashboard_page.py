from dash import Input, Output, html
from dash_spa import register_page

from .common import topNavBar, footer, buttonBar
from .dashboard import salesChart, customers, revenue, bounceRate, pageVisitsTable, teamMembers, progressTrack, totalOrdersBarChart, rankingPanel, acquisition, newTasksButton, runButton, alertsNotifications
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path
import sys

register_page(__name__, path="/pages/dashboard", title="Dash/Flightdeck - Dashboard")
sys.path.append("/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/dependencies/")


layout = html.Main([
        topNavBar(),
        buttonBar(
            newTasksButton(),
            runButton()
        ),
        html.Div([
            salesChart(),
            customers(),
            revenue(),
            bounceRate()
        ], className='row'),
        html.Div([
            html.Div([
                html.Div([
                    pageVisitsTable(),
                    acquisition(),
                ], className='row')
            ], className='col-12 col-xl-8'),
            html.Div([
                totalOrdersBarChart(),
                alertsNotifications()
            ], className='col-12 col-xl-4')

        ], className='row'),
        # html.Div(id="pipeline-status", className="pipeline-status", style={"margin-top": "20px"}),
        footer()
    ], className='content')

