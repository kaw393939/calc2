"""Testing the Calculator class & History"""
import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    """Clears history"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()

@pytest.fixture
def setup_addition_calculation_fixture():
    """Adds numbers together"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests add calculation in history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    values = (4, 3)
    add = Addition(values)
    Calculations.add_calculation(add)
    assert Calculations.count_history() == 2

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Tests getting calculation from history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0).get_result() == 3

def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """Gets last calculation from history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result() == 3

def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """Gets first calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation_result() == 3

def test_count_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Gets count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1

def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Gets last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(Calculations.get_last_calculation_object(), Addition)

def test_get_first_calculation_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Gets first calculation object"""
    # pylint: disable=redefined-outer-name,unused-argument
    assert isinstance(Calculations.get_first_calculation_object(), Addition)
