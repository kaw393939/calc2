"""Testing Division"""
import pytest
from calc.calculations.division import Division
from calc.utils.file_reader import PandasFileReader

def test_calculation_division():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    filename = "division_1000values.xlsx"
    df_values = PandasFileReader(filename).read_file()
    for index, row in df_values.iterrows():
        tuple_values = (row.value_1, row.value_2)
    # Act
        division = Division.create(tuple_values)
        try:
    #Assert
            assert division.get_result() == df_values['result'][index].round(decimals=5)
        except ZeroDivisionError:
            with pytest.raises(ZeroDivisionError):
                assert division.get_result() is True
