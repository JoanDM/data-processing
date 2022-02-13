import json
from pathlib import Path

import pandas as pd

from config import prRed


class CsvDataProcessor(object):
    def __init__(self, target_directory):
        self.set_target_directory(target_directory)
        self.df = None
        self.df_headers = None

    def fetch_csv_data_from_file_into_dataframe(self, path_to_csv):
        self.df = pd.read_csv(path_to_csv)
        self.df_headers = self.get_df_headers()

    def print_all_elements_specific_column(self, column_id):
        for index, row in self.df.iterrows():
            print(row[column_id])

    def get_list_of_all_elements_in_column(self, column_id):
        return self.df[column_id].tolist()

    def get_df_headers(self):
        return self.df.columns.values

    def get_element_by_index_and_column(self, row_indexer, column_indexer):
        return self.df.loc[row_indexer, column_indexer]

    def set_target_directory(self, target_directory):
        self.target_directory = Path(str(target_directory))
        target_directory.mkdir(parents=True, exist_ok=True)


class JsonDataProcessor(object):
    def __init__(self, target_directory):
        self.set_target_directory(target_directory)
        self.json_dict = None

    def set_target_directory(self, target_directory):
        self.target_directory = Path(str(target_directory))
        target_directory.mkdir(parents=True, exist_ok=True)

    def set_current_json_dict(self, json_dict):
        self.json_dict = json_dict

    def insert_key_val_to_current_json_dict(self, key, val):
        self.json_dict[key] = val

    def delete_key_from_current_json_dict(self, key):
        try:
            del self.json_dict[key]
        except KeyError:
            prRed(
                f"Error, target key is not present in dict. "
                f"Available keys: {self.json_dict.keys()}"
            )

    def print_current_json_dict_content(self):
        print(json.dumps(self.json_dict, indent=4))

    def save_current_dict_to_json_file(
        self,
        target_filename,
        target_directory,
        print_output_file_path=True,
    ):
        target_filename_dir = target_directory / f"{target_filename}.json"
        with open(target_filename_dir, "w") as fp:
            json.dump(self.json_dict, fp, indent=4)
        if print_output_file_path:
            print(f"File saved to {target_filename_dir}")
