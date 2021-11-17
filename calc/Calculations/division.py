"""Divide Class"""
# pylint: skip-file
from calc.Calculations.calculation_base import Calculation


class Divide(Calculation):
    """divide calculation object"""
    def get_result(self):
        """get the divide results"""
        if self.value_b <= 0:
            return "Error"
        return self.value_a / self.value_b