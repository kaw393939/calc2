"""Testing Division"""
import pytest
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for multiplication"""
    """Implementing AAA's of testing"""
    #Arrange
    mynumbers = (1.0,2.0,5.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.1

def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    """Implementing AAA's of testing"""
    # Arrange
    mynumbers = (1.0, 0.0, 1.0)
    division = Division(mynumbers)
    # Act
    # Assert
    with pytest.raises(ZeroDivisionError):
        result = division.get_result()
        assert result is True