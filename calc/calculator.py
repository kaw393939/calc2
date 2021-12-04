"""This class creates a calculator"""
from calc.calculations.calculation import Calculation
from calc.history.calculations import Calculations


class Calculator:
    """This is the Calculator class"""

    history = []
    @staticmethod
    def get_results_of_first_calculation_added_to_history():
        """ This is the get first result class"""
        return Calculator.history[0].get_result()

    @staticmethod
    def clear_history():
        """ This is the clear result class"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """ This is the history count class"""
        return len(Calculator.history)

    @staticmethod
    def get_last_result_value():
        """Gets last result of calculation"""
        return Calculation.get_last_calculation_result()

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """Uses tuples to add numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """Uses tuples to subtract numbers"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """Uses tuples to multiply numbers"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """Uses tuples to divide numbers"""
        Calculations.add_division_calculation(tuple_values)
        return True