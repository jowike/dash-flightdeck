from dash import Input, Output, State, html
from pathlib import Path
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project


def register_callbacks(app, project_root):
    @app.callback(
        Output("pipeline-status", "children"),
        Input("run-pipeline-button", "n_clicks")
    )
    def trigger_pipeline(n_clicks):
        if n_clicks > 0:
            try:
                # Initialize Kedro session
                bootstrap_project(Path(project_root))
                with KedroSession.create(Path(project_root)) as session:
                    session.run()
                return html.Div("Pipeline executed successfully!", style={"color": "green"})
            except Exception as e:
                return html.Div(f"Pipeline execution failed: {str(e)}", style={"color": "red"})
        return html.Div()  # Empty div initially


    @app.callback(
        Output("modal", "is_open"),
        [Input("advanced-config-modal-open", "n_clicks"), Input("close", "n_clicks")],
        [State("modal", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

