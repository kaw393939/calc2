"""Testing Division"""

from calc.Calculations.division import Divide
def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    values = (100.0,10.0)
    division = Divide(values)
    #Act
    #Assert
    assert division.get_output()== 0.1
