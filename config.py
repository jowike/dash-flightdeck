import os
import pandas as pd


def __load_yaml(file_path):
    with open(file_path, "r") as file:
        return file.read()

def load_data(file_path="/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/08_reporting/data.xlsx"):
    if os.path.exists(file_path):
        df = pd.read_excel(file_path, sheet_name="data")
        df["dt"] = df["dt"].astype(str).replace(r"-\d{2}$", "", regex=True)
        # df["dt"] = pd.to_datetime(df["dt"])

        return {
            "labels": [label if index % 3 == 0 else "" for index, label in enumerate(df["dt"])],
            "series": [df[c].tolist() for c in df.columns if c != "dt"]
        }
    return df

# Global variables to store ...
# pipeline_status = "Not started"
# last_run_timestamp = "N/A"
TARGET_FOLDER = "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/_test"
PARAMETERS_PATH = "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/conf/base/parameters.yml"
CATALOG_PATH= "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/conf/base/catalog.yml"
parameters, data_catalog = __load_yaml(PARAMETERS_PATH), __load_yaml(CATALOG_PATH)

