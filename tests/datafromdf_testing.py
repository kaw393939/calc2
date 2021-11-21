"""Using pandas to extract data from external file for testing all operations"""

import os
import pandas as pd

class PandaExtractData:
    # pylint: disable=too-few-public-methods
    """Dataframe class"""
    @staticmethod
    def get_data_from_dataframe(filename):
        """to create dataframe from external excel file"""
        # Get Current Working Directory
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(base_dir, "input_excel_files", filename)
        df_data = pd.read_excel(io=file_path, index_col=None,
                           names=["value_1", "value_2", "result"], dtype='float')
        return df_data
