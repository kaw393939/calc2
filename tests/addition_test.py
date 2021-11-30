"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    """Implementing AAA's of testing"""
    #Arrange
    mynumbers = (1.0,2.0,3.5,4.5)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 11