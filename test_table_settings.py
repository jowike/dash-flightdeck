from dash import html
from app import create_app
from server import serve_app
from components.dropdown_aio import DropdownAIO
from components.button_container_aoi import ButtonContainerAIO
from icons.hero import TICK_ICON, GEAR_ICON


def settingsDropdown():

    button = DropdownAIO.Button([
       GEAR_ICON,html.Span("Toggle Dropdown", className='visually-hidden')
    ], className='btn btn-link text-dark dropdown-toggle dropdown-toggle-split m-0 p-1')


    def element_renderer(value, selected):
        if selected:
            element = html.Div([value, TICK_ICON], className = 'dropdown-item d-flex align-items-center fw-bold')
        else:
            element = html.Div([value], className = 'dropdown-item fw-bold')

        if value == "30":
            element.className += ' rounded-bottom'

        return element

    store = ButtonContainerAIO.createStore(["10", "20", "30"], "10")

    container = ButtonContainerAIO(store, element_renderer, className='dropdown-menu dropdown-menu-xs dropdown-menu-end pb-0')
    container.children[0:0] = [store, html.Span("Show", className='small ps-3 fw-bold text-dark')]

    dropdown = DropdownAIO(button, container)

    return html.Div(dropdown, className='col-4 col-md-2 col-xl-1 ps-md-0 text-end')


def layout():
    dropdown = settingsDropdown()
    return html.Div([dropdown])


if __name__ == "__main__":
    app = create_app(layout(), plugins=[])
    serve_app(app, debug=False)
