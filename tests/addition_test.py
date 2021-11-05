"""Test of the Addition operation"""
from calc.operations.addition import Addition


def test_addition():
    """method calling Addition operation"""
    # Arrange
    addition = Addition(1, 2)
    # Act
    result = addition.get_result()
    # Assert
    assert result == 3
