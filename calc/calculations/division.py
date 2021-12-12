"""Division Class"""
from calc.calculations.calculation import Calculation

"""Inherits value value1,value2 from calculation"""


class Division(Calculation):
    """Division calculation object"""

    def get_result(self):
        """get the multiplication results"""
        division_values = 1.0
        try:
            for value in self.values:
                division_values /= value
        except ZeroDivisionError as err:
            return err
