"""Testing the Calculator"""
from calc.calculator import Calculator
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


def test_calculator_history():
    """testing calculator result is 0"""
    # Arrange
    previous_length = len(Calculator.history)
    Calculator.add_number(1, 2)
    assert len(Calculator.history) == previous_length+1


def test_calculator_add_static():
    """Testing the Add function of the calculator"""
    Calculator.add_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Addition)


def test_calculator_subtract_static():
    """Testing the subtract method of the calculator"""
    Calculator.subtract_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Subtraction)


def test_calculator_multiply_static():
    """Testing the multiply method of the calculator"""
    Calculator.multiply_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Multiplication)


def test_calculator_divide_static():
    """Testing the divide method of the calculator"""
    Calculator.divide_number(1, 1)
    last_operation = Calculator.get_last_operation()
    assert isinstance(last_operation, Division)
