"""Multiplication Class"""
from calc.Calculations.calculation_base import Calculation


class Multiplication(Calculation):
    """multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
