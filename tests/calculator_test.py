"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator

#this is a fixture, that runs a function each time you pass it to a test
@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """ Function to clear history"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    # pylint: disable=unused-argument
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    """Funtion to test clear history"""
    # pylint: disable=unused-argument
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    """Function to test count history"""
    # pylint: disable=unused-argument
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    """Function to test getting last calculation result"""
    # pylint: disable=unused-argument
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_first_calculation_result(clear_history):
    """Function to test getting first calculation result"""
    # pylint: disable=unused-argument
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_divide1(clear_history):
    """ tests division of two numbers"""
    # pylint: disable=unused-argument
    assert Calculator.divide_numbers(4,2) == 2

def test_calculator_divide2(clear_history):
    """ tests division of two numbers"""
    # pylint: disable=unused-argument
    assert Calculator.divide_numbers(1,0) == "Error"
