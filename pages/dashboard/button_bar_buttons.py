from dash_spa.components.dropdown_button_aoi import DropdownButtonAIO, dropdownLink

from dash import html
from ..icons.hero import ICON


def newTasksButton():
    return DropdownButtonAIO([
        # dropdownButtonWithIcon("Upload Files", ICON.UPLOAD, id="upload-files-open"),
        # dropdownButtonWithIcon("Advanced configuration", ICON.CUBE_TRANSPARENT, id="adv-config-open"),
        html.Div([dropdownLink("Upload Files", ICON.UPLOAD)], id="upload-files-modal-open", n_clicks=0, className="dropdown-button", style={"height": "fit-content"},),
        html.Div([dropdownLink("Advanced configuration", ICON.CUBE_TRANSPARENT)], id="advanced-config-modal-open", n_clicks=0, className="dropdown-button", style={"height": "fit-content"},),
    ], "Settings", buttonColor="gray-800", buttonIcon=ICON.SETTINGS)

def runButton():
    return  html.Button([
        ICON.PLAY,
        html.Span("Run", className='me-2')
    ],
    type='button',
    id="run-pipeline-button",
    n_clicks=0,
    className='btn btn-gray-800 d-inline-flex align-items-center me-2',
    )
