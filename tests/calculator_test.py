"""This tests the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def clear_history_fixture():
    """Clears history"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

def test_calculator_add_static(clear_history_fixture):
    """Tests static addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (2.0,4.0,6.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 12.0

def test_calculator_subtract_static(clear_history_fixture):
    """Tests static subtraction"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (9.0,1.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8.0

def test_calculator_multiply(clear_history_fixture):
    """Tests static multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (5.0,2.0,2.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 20.0

def test_calculator_divide(clear_history_fixture):
    """Tests static division"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (6.0,2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 3.0

def test_calculator_divide_by_zero(clear_history_fixture):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (25.0, 0.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == "Cannot divide by zero"
