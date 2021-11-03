"""This is multiplication operation object"""

from calc.calculation import Calculation

"""This is multiplication operation class"""
class Multiplication(Calculation):
    """Multiplying two numbers"""
    def get_Result(self):
        return self.value_a * self.value_b
