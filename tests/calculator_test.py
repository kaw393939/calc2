"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_add_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.add(1,2)
    assert result == 3

def test_calculator_subtract_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.subtract(1,2)
    assert result == -1


def test_calculator_multiply_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.multiply(1,2)
    assert result == 2

def test_calculator_divide_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.divide(1,2)
    assert result == 0.5

def test_calculator_divide_fail_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.divide(1,0)
    assert result == "Error: A number cannot be divided by 0"

def test_calculator_increment_result():
    """testing calculator result is 0"""
    calc = Calculator()
    result = calc.increment(2)
    assert result == 3
