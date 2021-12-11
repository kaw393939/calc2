"""Testing Division"""
from calc.calculations.division import Division

def test_static_calculation_division():
    """testing static method for division"""
    division = Division(10.0, 2.0)
    assert division.get_result() == 5.0
