"""Testing Multiplication"""
from calc.Calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    mynumbers = (1.0, 2.0)
    multiply = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiply.get_result() == 2
