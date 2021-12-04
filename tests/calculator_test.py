#"""This tests the Calculator"""
import pytest
import pandas as pd
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division

@pytest.fixture
def clear_history_fixture():
    """Clears history"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

def test_calculator_add_static(clear_history_fixture):
    """Tests static addition"""
    csv_reader = pd.read.csv("source/addition.csv")
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (4.0,8.0,2.0)
    Calculations.Add_numbers(my_tuple)
    assert Calculations.get_last_result_value() == 14.0

#def test_calculator_subtract_static(clear_history_fixture):
    #"""Tests static subtraction"""
    # pylint: disable=unused-argument,redefined-outer-name
    #my_tuple = (9.0,1.0)
    #Calculations.subtract_numbers(my_tuple)
    #assert Calculations.get_last_result_value() == 8.0

    def test_calculator_subtract_static(clear_history_fixture):
        """Testing the subtract method of the calc"""
        # pylint: disable=unused-argument,redefined-outer-name
        # using Tuple instead of args because we can pack as much data as we need into the tuple
        my_tuple = (1.0, 2.0, 3.0)
        # creating the calculation result object
        calculation_result_object = Calculator.subtract_numbers(my_tuple)
        # testing the instance
        assert isinstance(calculation_result_object, Subtraction)
        # testing the last result of the calculation
        assert Calculator.get_last_result_value() == -6.0
        # testing that the result object performs the calculation
        assert calculation_result_object.get_result() == -6.0

def test_calculator_multiply(clear_history_fixture):
    """Tests static multiplication"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (5.0,2.0,2.0)
    Calculations.multiply_numbers(my_tuple)
    assert Calculations.get_last_result_value() == 20.0

def test_calculator_divide(clear_history_fixture):
    """Tests static division"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (6.0,2.0)
    Calculations.divide_numbers(my_tuple)
    assert Calculations.get_last_result_value() == 3.0

def test_calculator_divide_by_zero(clear_history_fixture):
    """Testing the divide method of the calculator if someone attempts to divide by zero"""
    # pylint: disable=redefined-outer-name,unused-argument
    my_tuple = (25.0, 0.0)
    Calculations.divide_numbers(my_tuple)
    assert Calculations.get_last_result_value() == "Cannot divide by zero"

    csv_reader = pd.read_csv("source/addition.csv")
    for index, row in csv_reader.iterrows():
        values = (row.value1, row.value2)
        addition = Addition.create(values)
        addition_result = csv_reader["result"][index]
        assert addition.get_result() == addition_result