"""Test for addition"""
from calc.calculations.addition import Addition

def test_static_calculation_addition(addition_file_fixture):
    """testing static method for addition"""
    for index, row in addition_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        addition = Addition.create(tuple_values)
        assert addition.get_result() == row.result
