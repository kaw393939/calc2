"""This is subtraction operation object"""

from calc.calculation import Calculation

"""This is subtraction operation class"""
class Subtraction(Calculation):
    """Subtracting two numbers"""
    def get_Result(self):
        return self.value_a - self.value_b
