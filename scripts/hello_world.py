from config import _resources_dir_pathlib, _results_dir_pathlib
from data_processsor_class import DataProcessor

if __name__ == "__main__":

    dataprocessor = DataProcessor(_results_dir_pathlib)
    dataprocessor.fetch_csv_data_from_file_into_dataframe(
        _resources_dir_pathlib / "example_product_database.csv"
    )

    target_directory = _results_dir_pathlib
    product_names = dataprocessor.get_list_of_all_elements_in_column("Product Name")
    product_models = dataprocessor.get_list_of_all_elements_in_column("Product Model")
    product_serial_numbers = dataprocessor.get_list_of_all_elements_in_column(
        "Product Serial Number"
    )

    print(product_names[0:2])
