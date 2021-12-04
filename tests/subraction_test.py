"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction

def test_static_calculation_subtraction(subtraction_file_fixture):
    """testing static method for subtraction"""
    for index, row in subtraction_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        subtraction = Subtraction.create(tuple_values)
        assert subtraction.get_result() == subtraction_file_fixture['result'][index]