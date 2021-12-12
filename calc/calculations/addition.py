"""Addition Class"""
from calc.calculations.calculation import Calculation

"""Inherits value value1,value2 from calculation"""


class Addition(Calculation):
    """ calculation addition class"""

    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values += value
        return sum_of_values
