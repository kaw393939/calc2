"""This is addition operation object"""

from calc.calculation import Calculation

class Addition(Calculation):
    def get_result(self):
        """This is addition class"""
        return self.value_a + self.value_b
