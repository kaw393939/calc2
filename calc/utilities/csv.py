"""this is the CSV code"""
# Load the Pandas libraries with alias 'pd'
import os
import pandas as pd
# Read data from file '*.csv'

class PandasFileReader:
    """File reader class"""
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    def read_file(self):
        """Method to read the file type"""
        function_handler = None
        if ".csv" in self.file_name:
            function_handler = self._process_csv_file
        else:
            raise ValueError("Incorrect File Type")
        return function_handler()

    def _process_csv_file(self):
        """Method to process data from csv file to df"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/source", self.file_name)
        df_data = pd.read_csv(file_path, header=None)
        return df_data
