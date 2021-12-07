"""Test Addition"""
from calc.calculations.addition import Addition

def test_static_calculation_addition():
    """testing static method for addition"""
    addition = Addition(2.0,3.0)
    assert addition.get_result() == 5.0
