"""Subtraction Class"""
from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """Class to subtract"""

    def get_result(self):
        """Get subtraction results"""
        difference = self.values[0]
        for value in self.values[1:]:
            difference = difference - value
        return difference
