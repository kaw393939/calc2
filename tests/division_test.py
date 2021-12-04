"""Testing Division"""
import pytest
from calc.calculations.division import Division


def test_calculation_division(division_file_fixture):
    """testing static method for division"""
    for index, row in division_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        division = Division.create(tuple_values)
        try:
            assert division.get_result() == division_file_fixture['result'][index].round(decimals=5)
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert division.get_result() is True