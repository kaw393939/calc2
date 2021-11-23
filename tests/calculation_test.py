"""Testing the calculation class"""

from calc.calculations.calculation import Calculation
from tests.panda_extract_data import PandaExtractData

def test_convert_args_to_list_float():
    """Testing the overridden method of super class"""
    #Arrange
    filename = "subtraction_15values.xlsx"
    df_values = PandaExtractData.read_file(filename)

    numbers_tuple = df_values.value_1[0], df_values.value_2[0], df_values.value_1[1], df_values.value_2[1]
    #Act
    numbers_tuple_list = Calculation.convert_args_to_list_float(numbers_tuple)
    #Assert
    assert numbers_tuple_list == [2.0,1.0,4.0,2.0]

def test_get_result():
    """Testing the overridden method of super class + abstract class and method"""
    assert Calculation.get_result(self=None) is True
