"""Class for exporting data to external file"""

import pandas as pd
from tests.panda_extract_data import PandaExtractData
from calc.history.calculator_result import CalculatorResult

class Export(PandaExtractData):
    # pylint: disable=abstract-class-instantiated
    """Exporting data class"""
    @staticmethod
    def export_result_excel_file():
        """Exporting the calculated result to excel file using pandas"""
        result = CalculatorResult.history
        df_result = pd.DataFrame(result, columns=['result'])
        with pd.ExcelWriter('input_excel_files/addition_15values.xlsx',
                            mode='a', if_sheet_exists='replace') as writer:
            df_result.to_excel(writer, sheet_name='Tested_output', index=False)
            writer.save()
