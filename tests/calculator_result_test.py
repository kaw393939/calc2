"""Testing the Calculator"""

from calc.history.calculator_result import CalculatorResult

def test_add_calculation_to_history(clear_history_fixture, setup_history_test_fixture):
    """Testing clear history after adding calculation"""
    #import pdb;pdb.set_trace()
    assert CalculatorResult.count_history() == 4
    #assert add calculation to history

def test_clear_calculation_history(clear_history_fixture, setup_history_test_fixture):
    """Testing clear history after clearing the history"""
    assert CalculatorResult.count_history() == 4
    CalculatorResult.clear_history()
    assert CalculatorResult.count_history() == 0
    assert CalculatorResult.clear_history() is True
    #assert clear history

def test_get_calculation(clear_history_fixture, setup_history_test_fixture):
    """Testing getting calculation from history"""
    assert CalculatorResult.get_calculation_from_history(0).get_result() == 3.0
    assert CalculatorResult.get_calculation_from_history(1).get_result() == -2.0
    assert CalculatorResult.get_calculation_from_history(2).get_result() == 12.0
    assert CalculatorResult.get_calculation_from_history(3).get_result() == 0.8
    #assert get calculation

def test_get_last_calculation_result(clear_history_fixture, setup_history_test_fixture):
    """Testing getting last calculation from history"""
    assert CalculatorResult.get_last_calculation_result() == 0.8
    #assert get last calculation

def test_get_first_calculation_result(clear_history_fixture, setup_history_test_fixture):
    """Testing getting first calculation from history"""
    assert CalculatorResult.get_first_calculation().get_result() == 3.0
    #assert calculator result

def test_count_of_history(clear_history_fixture, setup_history_test_fixture):
    """Testing getting the count of calculations"""
    assert CalculatorResult.count_history() == 4
    #assert test count history