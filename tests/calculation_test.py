"""Testing calculation class"""
import pytest
from calc.history.calculator_result import CalculatorResult
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    CalculatorResult.clear_history()

@pytest.fixture
def setup_addition_calculation_fixture():
    """Fixture for addition"""
    # pylint: disable=redefined-outer-name
    addition = Addition(1, 2)
    CalculatorResult.add_calculation(addition)

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Check if clear history returns true"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert CalculatorResult.count_history() == 1

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Clears history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert CalculatorResult.count_history() == 1
    CalculatorResult.clear_history()
    assert CalculatorResult.count_history() == 0
    assert CalculatorResult.clear_history() == True

#def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
#    """Get calculation from history"""
#    # pylint: disable=unused-argument,redefined-outer-name
#    assert CalculatorResult.get_calculation(0).get_result() == 3
#
#def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
#    """Get last calculation from history"""
#    # pylint: disable=unused-argument,redefined-outer-name
#    assert CalculatorResult.get_last_calculation_result_value() == 3
#
#def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
#    """Get first calculation from history"""
#    # pylint: disable=unused-argument,redefined-outer-name
#    assert CalculatorResult.get_first_calculation().get_result() == 3
#
#def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
#    """Get calculation count from history"""
#    # pylint: disable=unused-argument,redefined-outer-name
#    assert CalculatorResult.count_history() == 1
#
#def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
#    """Get last calculation from  history"""
#    # pylint: disable=unused-argument,redefined-outer-name
#    #This test if it returns the last calculation as an object
#    assert isinstance(CalculatorResult.get_last_calculation_object(), Addition)