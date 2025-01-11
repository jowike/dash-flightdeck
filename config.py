# Global variables to store ...
# pipeline_status = "Not started"
# last_run_timestamp = "N/A"
TARGET_FOLDER = "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/data/_test"
PARAMETERS_PATH = "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/conf/base/parameters.yml"
CATALOG_PATH= "/Users/ejowik001/Desktop/Github/Nowcasting/kedro/refinery/conf/base/catalog.yml"


def __load_yaml(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
parameters, data_catalog = __load_yaml(PARAMETERS_PATH), __load_yaml(CATALOG_PATH)