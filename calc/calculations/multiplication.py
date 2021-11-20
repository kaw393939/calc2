"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """Class to multiply"""

    def get_result(self):
        """Get  multiplication results"""
        product = 1.0
        for value in self.values:
            product = product * value
        return product
