"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication(multiplication_file_fixture):
    """testing static method for multiplication"""
    for index, row in multiplication_file_fixture.iterrows():
        tuple_values = (row.value_1, row.value_2)
        multiplication = Multiplication.create(tuple_values)
        assert multiplication.get_result() == multiplication_file_fixture['result'][index]
