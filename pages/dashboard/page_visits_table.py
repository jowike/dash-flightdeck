from collections import OrderedDict
from dash import html, dcc
import pandas as pd

from dash_spa.components.table import TableAIO, TableContext
from ..icons import ICON

data = OrderedDict(
 [

    ('Release Date',['Nov 28', 'Dec 5', 'Dec 14', 'Dec 23', 'Dec 27']),
    ('Data Series',[
        'Real Disposable Personal Income',
        'Consumer Price Index for All Urban Consumers: All Items in U.S. City Average',
        'Advance Retail Sales: Retail Trade and Food Services',
        'Merchant Wholesalers Inventories',
        ' All Employees, Total Nonfarm'
        ]),
    # ('Data Series',['DSPIC96', 'CPIAUCSL', 'RSAFS', 'WHLSLRIMSA', 'PAYEMS']),
    ('Actual',['17,684.4', '316.441', '724,609', '905,023', '159,288']),
    ('Impact',['42,55%', '43,24%', '32,35%', '50,87%', '26,12%']),
    ('',['Up', 'Down', 'Down', 'Up', 'Down']),
    ]
)


df = pd.DataFrame.from_dict(data)


class PageVisitsTable(TableAIO):

    TABLE_CLASS_NAME = 'table align-items-center table-flush'

    def tableRow(self, index, args):
        name, views, value, rate, change = args.values()
        icon = ICON.ARROW_NARROW_UP if change == "Up" else ICON.ARROW_NARROW_DOWN
        return  html.Tr([
            html.Th(name, className='text-gray-900', scope='row'),
            html.Td(views, className='fw-bolder text-gray-500'),
            html.Td(value, className='fw-bolder text-gray-500'),
            html.Td([
                html.Div([
                    icon,
                    rate
                ], className='d-flex')
            ], className='fw-bolder text-gray-500')
        ])



@TableContext.Provider(id='page_visits_table')
def pageVisitsTable():

    table = PageVisitsTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns])

    return html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H2("Local Explanation", className='fs-5 fw-bold mb-0')
                    ], className='col'),
                    html.Div([
                        dcc.Link("See all", href='#', className='btn btn-sm btn-primary')
                    ], className='col text-end')
                ], className='row align-items-center')
            ], className='card-header'),
            html.Div(table, className='table-responsive')
        ], className='card border-0 shadow')
    ], className='col-12 mb-4')
