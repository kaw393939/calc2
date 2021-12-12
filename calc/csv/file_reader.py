"""read file type of external file"""
import os
import pandas as pd


class file_reader:
    """File reader class"""

    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    def read_file(self):
        """Method to read the file type"""
        handler = None
        if ".csv" in self.file_name:
            handler = self.process_csv_file()
        else:
            raise ValueError("File type error")
        return handler()

    def process_csv_file(self):
        """ Processing csv file to data frame"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "../../tests/input_excel_files", self.file_name)
        df_data = pd.read_csv(file_path, header=None)
        return df_data
