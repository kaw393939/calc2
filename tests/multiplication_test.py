"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication
from tests.panda_extract_data import PandaExtractData

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    filename = "multiplication_1000values.xlsx"
    df_values = PandaExtractData.read_file(filename)
    for index, row in df_values.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        multiplication = Multiplication.create(tuple_values)
    #Assert
        assert multiplication.get_result() == df_values['result'][index]
