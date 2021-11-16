"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0
    #Arrange
    mynumbers = (2.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 4.0
    #Arrange
    mynumbers = (0.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 2.0
