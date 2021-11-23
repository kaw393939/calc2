"""Testing the Calculator"""
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

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success after adding the calculation to the list"""
    #Assert
    assert CalculatorResult.count_history() == 4
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success after clearing the history list"""
    #Assert
    assert CalculatorResult.count_history() == 4
    CalculatorResult.clear_history()
    assert CalculatorResult.count_history() == 0
    assert CalculatorResult.clear_history() is True
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    #Assert
    assert CalculatorResult.get_calculation_from_history(0).get_result() == 3.0
    assert CalculatorResult.get_calculation_from_history(1).get_result() == -2.0
    assert CalculatorResult.get_calculation_from_history(2).get_result() == 12.0
    assert CalculatorResult.get_calculation_from_history(3).get_result() == 0.8
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_get_last_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    #Assert
    assert CalculatorResult.get_last_calculation_result() == 0.8
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_get_first_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the first calculation from the history"""
    #Assert
    assert CalculatorResult.get_first_calculation().get_result() == 3.0
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_count_of_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the count of calculation from the history"""
    #Assert
    assert CalculatorResult.count_history() == 4
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True
