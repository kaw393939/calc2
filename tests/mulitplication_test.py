"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_static_calculation_multiplication():
    """testing static method for multiplication"""
    multiplication = Multiplication(3.0,5.0)
    assert multiplication.get_result() == 15.0
