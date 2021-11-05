"""Test of the Multiplication operation"""
from calc.operations.multiplication import Multiplication


def test_multiplication():
    """method calling Multiplication operation"""
    # Arrange
    multiplication = Multiplication(3, 2)
    # Act
    result = multiplication.get_result()
    # Assert
    assert result == 6
