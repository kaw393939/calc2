"""This is division operation object"""

from calc.calculation import Calculation

class Division(Calculation):
    def get_result(self):
        """This is division class"""
        return self.value_a / self.value_b
