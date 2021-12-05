"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator

def test_calculator_add_static(clear_history_fixture, addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    tuple_values = addition_file_fixture.value_1[5], addition_file_fixture.value_2[5]
    Calculator.__add__(tuple_values)
    assert Calculator.get_last_calculation_from_result() == addition_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_subtract_static(clear_history_fixture, subtraction_file_fixture):
    """Testing the subtract method of the calc"""
    tuple_values = subtraction_file_fixture.value_1[5], subtraction_file_fixture.value_2[5]
    Calculator.__sub__(tuple_values)
    assert Calculator.get_last_calculation_from_result() == subtraction_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_multiply_static(clear_history_fixture, multiplication_file_fixture):
    """Testing the multiplication method of the calc"""
    tuple_values = multiplication_file_fixture.value_1[5], multiplication_file_fixture.value_2[5]
    Calculator.__mul__(tuple_values)
    assert Calculator.get_last_calculation_from_result() == multiplication_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_divide_static(clear_history_fixture, division_file_fixture):
    """Testing the division method of the calc"""
    tuple_values = division_file_fixture.value_1[5], division_file_fixture.value_2[5]
    Calculator.__truediv__(tuple_values)
    assert Calculator.get_last_calculation_from_result() == division_file_fixture['result'][5].round(decimals=5) \
           and clear_history_fixture is True

def test_calculator_divide_exception_static(clear_history_fixture, division_file_fixture):
    """Testing the division method of the calc for the exception"""
    tuple_values = division_file_fixture.value_1[2], division_file_fixture.value_2[0]
    Calculator.__truediv__(tuple_values)
    with pytest.raises(ZeroDivisionError):
        assert Calculator.get_last_calculation_from_result() is True \
               and clear_history_fixture is True
