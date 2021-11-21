"""Testing Division"""
import pytest
from calc.calculations.division import Division
from tests.datafromdf_testing import PandaExtractData

def test_calculation_division():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    filename = "division_1000values.xlsx"
    df_values = PandaExtractData.get_data_from_dataframe(filename)
    for index, row in df_values.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        division = Division.create(tuple_values)
        try:
    #Assert
            assert division.get_result() == df_values['result'][index].round(decimals=5)
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert division.get_result() is True


# def test_calculator_division_exception():
#     """ Testing division exception for division by zero"""
#     # Arrange
#     filename = "division_1000values.xlsx"
#     df_values = PandaExtractData.get_data_from_dataframe(filename)
#
#     tuple_values = df_values.value_1[1], df_values.value_2[1]
#     # Act
#     division = Division.create(tuple_values)
#     # Assert
#     with pytest.raises(ZeroDivisionError):
#         assert division.get_result() is True
