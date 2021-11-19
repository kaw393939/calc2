""" This is the calculator function"""
from calc.history.calculations import Calculations

class Calculator:
    """Calculator class"""

    @staticmethod
    def get_last_result_value():
        """Gets last result of calculation"""
        return Calculations.get_last_calculation_result_value()

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
        division = Division.create(value_a, value_b)
        Calculator.add_calculation_to_history(tuple_values)
        return True


