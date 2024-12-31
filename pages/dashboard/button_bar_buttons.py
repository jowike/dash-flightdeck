from dash_spa.components.dropdown_button_aoi import DropdownButtonAIO, dropdownLink

from dash import html
from ..icons.hero import ICON


def newTasksButton():
    return DropdownButtonAIO([
        # dropdownLink("Add User", ICON.USER_ADD),
        dropdownLink("Add Parameter", ICON.CUBE_TRANSPARENT),
        dropdownLink("Upload Files", ICON.UPLOAD),
        # dropdownLink("Preview Security", ICON.SECURITY),
        # dropdownLink("Upgrade to Pro", ICON.FIRE.ME2_DANGER),
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