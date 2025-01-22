import os
import yaml
from dateutil import relativedelta
import pandas as pd
from openpyxl import load_workbook

def __load_yaml(file_path):
    with open(file_path, "r") as file:
        return file.read()

def load_predictions(
        type: str,
        file_path:str="/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/08_reporting/dash_input_report.xlsx",
        ):

    if os.path.exists(file_path):
        wb = load_workbook(file_path, read_only=True)
        if type == "base":
            assert "Nowcast Browser – Base" in wb.sheetnames
            df = pd.read_excel(file_path, sheet_name="Nowcast Browser – Base")
        elif type == "adj":
            assert "Nowcast Browser – Adjusted" in wb.sheetnames
            df = pd.read_excel(file_path, sheet_name="Nowcast Browser – Adjusted")
        else: raise ValueError("Invalid type. Please choose 'base' or 'adj'.")

        df["Reference Date"] = df["Reference Date"].astype(str).replace(r"-\d{2}$", "", regex=True)

        return {
            "labels": [label if index % 3 == 0 else "" for index, label in enumerate(df["Reference Date"])],
            "series": [df[c].tolist() for c in df.columns if c != "Reference Date"]
        }
    return None

def load_cards(
        file_path:str="/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/08_reporting/dash_input_report.xlsx",
        ):
    if os.path.exists(file_path):
        wb = load_workbook(file_path, read_only=True)
        assert "Cards" in wb.sheetnames

        df = pd.read_excel(file_path, sheet_name="Cards")

        d = {}
        for r in df.iterrows():
            d[r[1]["Card"]] = {
                "Value": r[1]["Value"],
                "Since Last Month": r[1]["Since Last Month"],
            }
        return d
    return None


def load_contributions(
        file_path:str="/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/08_reporting/dash_input_report.xlsx",
        ):

    if os.path.exists(file_path):
        wb = load_workbook(file_path, read_only=True)
        assert "Local Explanation" in wb.sheetnames
        df = pd.read_excel(file_path, sheet_name="Local Explanation")

        df['Release Date'] = pd.to_datetime(df['Release Date']).dt.strftime('%b %d')

        # Prepare the ordered dictionary

        df[''] = ['Up' if x > 0 else 'Down' if x < 0 else '' for x in df['Impact']]  # Adding 'Up' or 'Down' based on 'Impact'
        
        return df.drop(columns=['Series ID']).to_dict('records'), df["Series ID"].tolist()
    return None

def load_series(series_id=None):
    def load_yaml(filepath):
        with open(filepath, 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
        
    data_catalog = load_yaml(CATALOG_PATH)
    parameters = load_yaml(PARAMETERS_PATH)

    ref_datetime = pd.to_datetime(parameters['options']['ref_date'])
    ref_date_col = parameters['options']['ref_date_col']
    y_code = parameters['options']['y_code']
        
    df = pd.read_excel(data_catalog['harmonized_data']['filepath'])
    df[ref_date_col] = pd.to_datetime(df[ref_date_col])
    df = df.sort_values(ref_date_col)

    _, series_ids = load_contributions()
    colnames = [ref_date_col, y_code] + series_ids

    for c in colnames[1:]:
        df[c] = df[c].pct_change()

    series = df.loc[df[ref_date_col].between(ref_datetime-relativedelta.relativedelta(months=6), ref_datetime), colnames]
    series["dt"] = pd.to_datetime(series[ref_date_col]).dt.strftime('%b')

    # if series_id is None: series_id = series_ids[1]

    return {
        "labels": [month for month in series["dt"]],
        "series": [series[c].tolist() for c in [y_code, series_id]]
    }

# Global variables to store ...
# pipeline_status = "Not started"
# last_run_timestamp = "N/A"
TARGET_FOLDER = "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/_test"
PARAMETERS_PATH = "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/conf/base/parameters.yml"
CATALOG_PATH= "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/conf/base/catalog.yml"
parameters, data_catalog = __load_yaml(PARAMETERS_PATH), __load_yaml(CATALOG_PATH)

