from dash import Input, Output, State, html
from pathlib import Path
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
import os
import subprocess
import socket
import signal

kedro_viz_process = None
viz_port = None

def register_callbacks(app, project_root):
    @app.callback(
        Output("pipeline-status", "children"),
        Input("run-pipeline-button", "n_clicks")
    )
    def trigger_pipeline_run(n_clicks):
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
        Output("pipeline-viz", "children"),
        [Input("start-viz-button", "n_clicks"),
         Input("stop-viz-button", "n_clicks"),
        ]
    )
    def manage_pipeline_viz(start_clicks, stop_clicks):
        global kedro_viz_process, viz_port

        def __find_free_port(port=5001, max_port=65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            while port <= max_port:
                try:
                    sock.bind(('', port))
                    sock.close()
                    return port
                except OSError:
                    port += 1
            raise IOError('no free ports')

        # Start Kedro Viz
        if start_clicks > 0:
            if kedro_viz_process is None or kedro_viz_process.poll() is not None:
                try:
                    viz_port = __find_free_port()

                    # Start Kedro Viz in a new process group
                    kedro_viz_process = subprocess.Popen(
                        f"cd {project_root} && kedro viz --autoreload --host=127.0.0.1 --port={viz_port}",
                        shell=True,
                        preexec_fn=os.setsid  # Create a new process group
                    )
                    return html.Div([
                        html.Div([
                            "✨ Kedro Viz is running at ",
                            html.A(
                                f"http://127.0.0.1:{viz_port}/",
                                href=f"http://127.0.0.1:{viz_port}/",
                                target="_blank",
                                style={
                                    "color": "#7FBBFF",
                                    "text-decoration": "underline",
                                }
                            )
                        ]),
                    ])
                except Exception as e:
                    return html.Div(f"Failed to start Kedro Viz: {str(e)}", style={"color": "red"})

        # Stop Kedro Viz
        if stop_clicks > 0:
            if kedro_viz_process:
                try:
                    # Kill the entire process group
                    os.killpg(os.getpgid(kedro_viz_process.pid), signal.SIGTERM)
                    kedro_viz_process.wait(timeout=5)  # Ensure the process terminates
                    kedro_viz_process = None  # Reset the process variable
                    viz_port = None  # Reset the port variable
                    return html.Div("✨ Kedro Viz has been stopped.")
                except subprocess.TimeoutExpired:
                    return html.Div("Failed to stop Kedro Viz: Timeout occurred.", style={"color": "red"})
                except Exception as e:
                    return html.Div(f"Failed to stop Kedro Viz: {str(e)}", style={"color": "red"})

        # Default output if no action is triggered
        return html.Div("Click the buttons to start or stop Kedro Viz.")


    @app.callback(
        Output("modal", "is_open"),
        [Input("advanced-config-modal-open", "n_clicks"), Input("close", "n_clicks")],
        [State("modal", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

