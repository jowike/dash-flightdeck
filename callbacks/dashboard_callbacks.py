from dash import Input, Output, State, html
from pathlib import Path
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
import os
import subprocess
import socket
import signal
import base64
import pandas as pd
from dash import ctx, no_update  # Dash context to track which input triggered the callback


kedro_viz_process = None
viz_port = None

from config import parameters, data_catalog


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
        Output("advanced-config-modal", "is_open"),
        [Input("advanced-config-modal-open", "n_clicks"), Input("advanced-config-modal-close", "n_clicks")],
        [State("advanced-config-modal", "is_open")],
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    @app.callback(
        Output("upload-files-modal", "is_open"),
        [Input("upload-files-modal-open", "n_clicks"), Input("upload-files-modal-close", "n_clicks")],
        [State("upload-files-modal", "is_open")],
    )
    def toggle_upload(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

    
    # Callback
    @app.callback(Output('output-data-upload', 'children'),
                Input('upload-data', 'contents'),
                State('upload-data', 'filename'))
    def update_output(list_of_contents, list_of_names):

        def __handle_upload(contents, filename):
            try:
                # file_path = os.path.basename(filename)
                # target_path = os.path.join(TARGET_FOLDER, filename)
                # os.rename(file_path, target_path)
                content_type, content_string = contents.split(',')
                decoded = base64.b64decode(content_string)

                # Save the file to the target folder
                target_path = os.path.join(app.upload_target, filename)
                with open(target_path, 'wb') as f:
                    f.write(decoded)

                # Calculate file size
                file_size_kb = len(decoded) / 1024
                file_size_str = f"{file_size_kb:.2f} KB" if file_size_kb < 1024 else f"{file_size_kb / 1024:.2f} MB"
                
                # Success message with file details
                message = f"Upload successful!\nFile: {filename} ({file_size_str})"
                icon_color = '#37BE67'  # Green for success
                icon_class = 'fa fa-check'  # Font Awesome check icon
            except Exception:
                # Failure message
                message = "Upload failed! Please try again."
                icon_color = '#F4405E'  # Red for failure
                icon_class = 'fas fa-times'  # Font Awesome cross icon

            return html.Div([
                html.Div([
                    html.I(className=icon_class, style={
                        'margin-right': '10px',
                        'font-size': '20px',
                        'color': icon_color  # Only the icon is colored
                    }),
                    html.Span(message, style={
                        'font-size': '14px',
                        'font-weight': 'bold',
                        'color': '#000000'  # Message text is black
                    }),
                ], style={
                    'padding': '10px',
                    'margin-top': '10px',
                    'text-align': 'center',
                    'display': 'inline-flex',
                    'align-items': 'center',
                })
            ])
        if list_of_contents is not None:
            children = [
                __handle_upload(c, n) for c, n in
                zip(list_of_contents, list_of_names)]
            return children
    # Callback to save changes
    @app.callback(
        Output("output-edit-advanced-config", "children"),
        Input("save-button", "n_clicks"),
        State("textarea-parameters", "value"),
        State("textarea-catalog", "value"),
        prevent_initial_call=True,
    )
    def save_file(n_clicks, parameters_content, data_catalog_content):
        def __save_yaml(file_path, content):
            with open(file_path, "w") as file:
                # yaml.safe_dump(yaml.safe_load(content), file)
                file.write(content)

        try:
            __save_yaml(app.parameters_path, parameters_content)
            __save_yaml(app.catalog_path, data_catalog_content)

            message = "Update successful!"
            icon_color = '#37BE67'  # Green for success
            icon_class = 'fa fa-check'  # Font Awesome check icon

        except Exception:
            message = "Edit failed! Please try again."
            icon_color = '#F4405E'  # Red for failure
            icon_class = 'fas fa-times'  # Font Awesome cross icon

        return html.Div([
            html.Div([
                html.I(className=icon_class, style={
                    'margin-right': '10px',
                    'font-size': '20px',
                    'color': icon_color  # Only the icon is colored
                }),
                html.Span(message, style={
                    'font-size': '14px',
                    'font-weight': 'bold',
                    'color': '#000000'  # Message text is black
                }),
            ], style={
                'padding': '10px',
                'margin-top': '10px',
                'margin-bottom': '20px',
                'text-align': 'center',
                'display': 'inline-flex',
                'align-items': 'center',
            })
        ])

    # Callback to enable and disable editing
    @app.callback(
        [
            Output("textarea-parameters", "disabled"),
            Output("textarea-catalog", "disabled"),
            Output("textarea-parameters", "value"),
            Output("textarea-catalog", "value"),
        ],
        [
            Input("enable-edit", "n_clicks"),
            Input("save-button", "n_clicks"),
            Input("discard-changes", "n_clicks"),
        ],
    )
    def toggle_textareas(enable_clicks, save_clicks, discard_clicks):
        # print(f"Triggered by: {ctx.triggered_id}")
        # print(f"Enable: {enable_clicks}, Save: {save_clicks}, Discard: {discard_clicks}")

        # Check which button triggered the callback
        if ctx.triggered_id == "enable-edit":
            return False, False, no_update, no_update  # Enable both textareas
        elif ctx.triggered_id == "save-button":
            return True, True, no_update, no_update  # Disable both textareas
        elif ctx.triggered_id == "discard-changes":
            return True, True, parameters, data_catalog
        # Default case (keep textareas disabled)
        return True, True, no_update, no_update