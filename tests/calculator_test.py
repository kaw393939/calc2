"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
#from tests.calculator_result_test import clear_history_fixture_test
from tests.panda_extract_data import PandaExtractData

def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    #Arrange
    filename = "addition_1000values.xlsx"
    df_values_add = PandaExtractData.read_file(filename)
    tuple_values = df_values_add.value_1[5], df_values_add.value_2[5]
    #Act
    Calculator.__add__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == df_values_add['result'][5] and clear_history_fixture is True

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    #Arrange
    filename = "subtraction_1000values.xlsx"
    df_values_sub = PandaExtractData.read_file(filename)
    tuple_values = df_values_sub.value_1[5], df_values_sub.value_2[5]
    #Act
    Calculator.__sub__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == df_values_sub['result'][5] and clear_history_fixture is True

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiplication method of the calc"""
    #Arrange
    filename = "multiplication_1000values.xlsx"
    df_values_mul = PandaExtractData.read_file(filename)
    tuple_values = df_values_mul.value_1[5], df_values_mul.value_2[5]
    #Act
    Calculator.__mul__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == df_values_mul['result'][5] and clear_history_fixture is True

def test_calculator_divide_static(clear_history_fixture):
    """Testing the division method of the calc"""
    #Arrange
    filename = "division_1000values.xlsx"
    df_values_div = PandaExtractData.read_file(filename)
    tuple_values = df_values_div.value_1[5], df_values_div.value_2[5]
    #Act
    Calculator.__truediv__(tuple_values)
    #Assert
    assert Calculator.get_last_calculation_from_result() == df_values_div['result'][5].round(decimals=5) \
           and clear_history_fixture is True

def test_calculator_divide_exception_static(clear_history_fixture):
    """Testing the division method of the calc for the exception"""
    #Arrange
    filename = "division_1000values.xlsx"
    df_values_div_exp = PandaExtractData.read_file(filename)
    tuple_values = df_values_div_exp.value_1[2], df_values_div_exp.value_2[0]
    #Act
    Calculator.__truediv__(tuple_values)
    #Assert
    with pytest.raises(ZeroDivisionError):
        assert Calculator.get_last_calculation_from_result() is True \
               and clear_history_fixture is True
