"""Fixtures to be ued globally under the tests directory"""
import os
import pandas as pd
import pytest
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculator_result import CalculatorResult
from tests.panda_extract_data import PandaExtractData

@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    return CalculatorResult.clear_history()

@pytest.fixture(name="setup_addition_calculation_fixture")
def setup_addition_calculation_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    #Arrange
    filename = "addition_15values.xlsx"
    df_values = PandaExtractData.read_file(filename)

    numbers_tuple1 = df_values.value_1[0], df_values.value_2[0]
    numbers_tuple2 = df_values.value_1[1], df_values.value_2[2]
    numbers_tuple3 = df_values.value_1[2], df_values.value_2[2]
    numbers_tuple4 = df_values.value_1[3], df_values.value_2[3]
    #Act
    CalculatorResult.add_calculation_to_history(Addition.create(numbers_tuple1))
    CalculatorResult.add_calculation_to_history(Subtraction.create(numbers_tuple2))
    CalculatorResult.add_calculation_to_history(Multiplication.create(numbers_tuple3))
    CalculatorResult.add_calculation_to_history(Division.create(numbers_tuple4))
    return True

@pytest.fixture(name="addition_file_fixture")
def read_addition_file():
    """Method to read the file type"""
    file_name = "addition_1000values.xlsx"
    return  PandaExtractData(file_name).read_file()


