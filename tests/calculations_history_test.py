"""Testing the Calculator"""
import pytest
from calc.calculations.addition import Addition
from calc.history.calculator_result import CalculatorResult

@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    return CalculatorResult.clear_history()

@pytest.fixture(name="setup_addition_calculation_fixture")
def setup_addition_calculation_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    CalculatorResult.add_calculation_to_history(Addition.create((1,2)))
    return True

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    assert CalculatorResult.count_history() == 1
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    assert CalculatorResult.count_history() == 1
    CalculatorResult.clear_history()
    assert CalculatorResult.count_history() == 0
    assert CalculatorResult.clear_history() is True
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    assert CalculatorResult.get_calculation_from_history(0).get_result() == 3
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_get_last_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    assert CalculatorResult.get_last_calculation_result() == 3
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_get_first_calculation_result(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    assert CalculatorResult.get_first_calculation().get_result() == 3
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True

def test_count_of_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    assert CalculatorResult.count_history() == 1
    assert clear_history_fixture is True
    assert setup_addition_calculation_fixture is True
