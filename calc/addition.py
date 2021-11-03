"""This is addition operation object"""

from calc.calculation import Calculation

"""This is addition operation class"""
class Addition(Calculation):
    """Adding two numbers"""
    def get_Result(self):
        return self.value_a + self.value_b
