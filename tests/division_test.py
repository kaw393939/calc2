"""Test of the Division operation"""
from calc.operations.division import Division


def test_multiplication():
    """method calling Division operation"""
    # Arrange
    division = Division(6, 2)
    # Act
    result = division.get_result()
    # Assert
    assert result == 3

    # Arrange
    division = Division(1, 0)
    # Act
    result = division.get_result()
    # Assert
    assert result is None
