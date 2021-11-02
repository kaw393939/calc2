"""Testing the Calculator"""
import pytest
from calculator.calculator import Calculator

# This is how you define a function that will run each time yuo pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    Calculator.clear_history()

def test_calculator_add_first(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3

def test_calculator_add_second(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(2, 3) == 5

def test_calculator_add_third(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(3, 4) == 7

def test_calculator_history_count(clear_history):
    assert Calculator.count_history() == 0

def test_calculator_clear_history():
    assert Calculator.clear_history() == 0

def test_calc_complete(clear_history):
    #The calculator is holding static properties and methods i.e history property there is only one history property
    #Addition calculation objects to the history
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2,3) == 5
    assert Calculator.add_number(3,4) == 7
    assert Calculator.count_history() == 3
    #The numbers in the [] refers to the calculation obj ect in that position and you can call the method on the object
    assert Calculator.history[0].getResult() == 3
    assert Calculator.history[1].getResult() == 5
    assert Calculator.history[2].getResult() == 7

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1
    assert Calculator.subtract_number(2, 4) == -2
    assert Calculator.subtract_number(3, 6) == -3
    assert Calculator.count_history() == 3

def test_calculator_multiply(clear_history):
    """ Testing multiplication of two numbers"""
    assert Calculator.multiply_numbers(1, 2) == 2
    assert Calculator.multiply_numbers(2, 3) == 6
    assert Calculator.multiply_numbers(3, 4) == 12
    assert Calculator.multiply_numbers(4, 5) == 20
    assert Calculator.count_history() == 4
    assert Calculator.clear_history() == 0

def test_calculator_division(clear_history):
    """ Testing division of two numbers"""
    assert Calculator.divide_numbers(1,1) == 1
    assert Calculator.divide_numbers(2,1) == 2
    assert Calculator.divide_numbers(3,1) == 3

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(1,0)
