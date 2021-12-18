import os
import logging

def serve_app(app, path="", debug=False):
    """Serve Dash application

    Args:
        app (Dash): Dash instance to be served
        path (str, optional): Initial URL. Defaults to "".
        debug (bool, optional): Enable Dash debug. Defaults to False.
    """

    # Turn off werkzeug  logging as it's very noisy

    # aps_log = logging.getLogger('werkzeug')
    # aps_log.setLevel(logging.ERROR)

    # When running in a Docker container the internal port
    # is mapped onto a host port. Use the env variables passed
    # in to the container to determin the host URL.

    port = int(os.environ.get("PORT", 5000))
    hostname = os.environ.get("HOSTNAME", "localhost")
    hostport = os.environ.get("HOSTPORT", "5000")

    print(f' * Visit http://{hostname}:{hostport}{path}')

    app.run_server(debug=debug, host='0.0.0.0', port=port, threaded=False)