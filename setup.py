import sys
import subprocess


def run_command(command):
    try:
        print(f"Executing: {command}")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}\nError: {e}")
        sys.exit(1)

def install_packages():
    commands = [
        "pip install kedro",
        "pip install kedro-viz",
        "pip install kedro-datasets",
        "pip install bottleneck",
        "pip install pmdarima",
        "python3 C:\\Users\\elzbi\\OneDrive\\Dokumenty\\GitHub\\mifs\\setup.py install --user",  # TODO: git clone + git checkout
        "pip install numpy==1.26.4",
        "pip install -U kaleido",
        "pip install xlsxwriter",
        "pip install openpyxl",
        "pip install diskcache",
        "pip install pyyaml",
        "pip install dash_uploader",
        "pip install dash_spa",
        "pip install dash_chartist",
        "pip install dash_loading_spinners",
    ]
    for cmd in commands:
        run_command(cmd)

# Environment setup
if __name__ == "__main__":
    install_packages()

