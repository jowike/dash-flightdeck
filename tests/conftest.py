import logging
import pytest
from selenium.webdriver.chrome.options import Options

# Turn off werkzeug logging as it's very noisy

aps_log = logging.getLogger('werkzeug')
aps_log.setLevel(logging.ERROR)


# This is needed to force Chrome to run without sandbox enabled. Docker
# does not support namespaces so running Chrome in a sandbox is not possible.
#
# See https://github.com/plotly/dash/issues/1420

def pytest_setup_options():
    options = Options()
    options.add_argument('--no-sandbox')
    # options.add_argument("--start-maximized")
    return options