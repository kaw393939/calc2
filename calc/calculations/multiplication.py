"""Multiplication Class"""
from calc.calculations.calculation import Calculation

"""Inherits value value1,value2 from calculation"""


class Multiplication(Calculation):
    """multiplication calculation object"""

    def get_result(self):
        """get the multiplication results"""
        multiplication_values = 1.0
        for value in self.values:
            multiplication_values *= value
        return multiplication_values
