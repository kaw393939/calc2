"""Testing Addition"""

from calc.calculations.addition import Addition
from tests.datafromdf_testing import PandaExtractData
# from tests.export_result_to_excel import Export

def test_static_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = "addition_1000values.xlsx"
    df_values = PandaExtractData.get_data_from_dataframe(filename)
    for index, row in df_values.iterrows():
        tuple_values = (row.value_1, row.value_2)
    #Act
        addition = Addition.create(tuple_values)
    #Assert
        assert addition.get_result() == df_values['result'][index]

    # #calling method of export class to export the calculated data from history to excel file
    # export_results = Export.export_result_excel_file()
