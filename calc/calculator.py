""" This is the increment function"""
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


# the calculator class just contains the methods to calculate

class Calculator:
    """ This is the Calculator class"""

    # the calculator class just calls methods on Calculations class
    @staticmethod
    def get_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    # tuple allows me to pass in as many values as a I want
    def add_numbers(values: tuple):
        """ adds list of numbers"""
        addition = Addition.create(values)
        Calculations.add_calculation(addition)
        return True

    @staticmethod
    def subtract_numbers(values: tuple):
        """ subtract a list of numbers from result"""
        subtraction = Subtraction.create(values)
        Calculations.add_calculation(subtraction)
        return True

    @staticmethod
    def multiply_numbers(values: tuple):
        """ multiplication number from result"""
        multiplication = Multiplication.create(values)
        Calculations.add_calculation(multiplication)
        return True

    @staticmethod
    def divide_numbers(values: tuple):
        """ multiplication number from result"""
        division = Division.create(values)
        Calculations.add_calculation(division)
        return True
