"""Using pandas to extract data from external file for testing all operations"""

import os
import pandas as pd


class PandaExtractData:
    """Dataframe class"""

    @staticmethod
    def read_file(file_name):
        """Method to read the file type"""
        function_handler = None
        if ".csv" in file_name:
            function_handler =  PandaExtractData._process_csv_file
        elif ".xlsx" in file_name:
            function_handler =  PandaExtractData._process_xlsx_file
        else:
            raise ValueError("Unknown File Type")
        return function_handler(file_name)

    @staticmethod
    def _process_xlsx_file(file_name):
        """Method to process data from excel file to df"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "input_excel_files", file_name)
        df_data = pd.read_excel(io=file_path, index_col=None,
                                names=["value_1", "value_2", "result"], dtype='float')
        return df_data


    @staticmethod
    def _process_csv_file(file_name):
        """Method to process data from csv file to df"""
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "input_excel_files", file_name)
        df_data = pd.read_csv(file_path, header=None)
        return df_data
