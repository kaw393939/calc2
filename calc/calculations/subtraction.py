"""Subtraction Class"""
from calc.calculations.calculation import Calculation

"""Inherits value value1,value2 from calculation"""


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values -= value
        return difference_of_values
