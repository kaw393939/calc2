"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    """Implementing AAA's of testing"""
    #Arrange
    mynumbers = (1.0,2.0,4.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 8.0