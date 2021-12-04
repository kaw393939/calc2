"""Fixtures for tests"""

import pytest
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculator_result import CalculatorResult
from calc.utilities.csv import PandasFileReader

@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture_test():
    """define function to clear history"""
    return CalculatorResult.clear_history()

@pytest.fixture(name="setup_history_test_fixture")
def setup_addition_calculation_fixture_test():
    """define function to ad calculation"""
    # import pdb;pdb.set_trace()
    filename = "addition.csv"
    df_values = PandasFileReader(filename).read_file()

    numbers_tuple1 = df_values.value_1[0], df_values.value_2[0]
    numbers_tuple2 = df_values.value_1[1], df_values.value_2[2]
    numbers_tuple3 = df_values.value_1[2], df_values.value_2[2]
    numbers_tuple4 = df_values.value_1[3], df_values.value_2[3]

    CalculatorResult.add_calculation_to_history(Addition.create(numbers_tuple1))
    CalculatorResult.add_calculation_to_history(Subtraction.create(numbers_tuple2))
    CalculatorResult.add_calculation_to_history(Multiplication.create(numbers_tuple3))
    CalculatorResult.add_calculation_to_history(Division.create(numbers_tuple4))
    return True

@pytest.fixture(name="addition_file_fixture", scope="module")
def read_addition_file():
    """Method to read addition csv"""
    file_name = "addition.csv"
    return  PandasFileReader(file_name).read_file()

@pytest.fixture(name="subtraction_file_fixture", scope="module")
def read_subtraction_file():
    """Method to read subtraction csv"""
    file_name = "subtraction.csv"
    return  PandasFileReader(file_name).read_file()

@pytest.fixture(name="multiplication_file_fixture", scope="module")
def read_multiplication_file():
    """Method to read multiplication.csv"""
    file_name = "multiplication.csv"
    return  PandasFileReader(file_name).read_file()

@pytest.fixture(name="division_file_fixture", scope="module")
def read_division_file():
    """Method to read division csv"""
    file_name = "division.csv"
    return  PandasFileReader(file_name).read_file()

@pytest.fixture(name="subtraction_test_file_fixture", scope="module")
def read_subtraction_test_file():
    """Method to read subtraction csv"""
    file_name = "subtraction.csv"
    return  PandasFileReader(file_name).read_file()