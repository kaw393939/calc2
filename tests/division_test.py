"""Testing Division"""
# pylint: skip-file
from calc.Calculations.division import Divide

def test_calculation_divide():
    """testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (4.0, 2.0)
    divide = Divide(mynumbers)
    assert divide.get_result() == 2
