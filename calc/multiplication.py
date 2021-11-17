"""Multiplication calculation that inherits the value A and value B from the calculation class"""

from calc.calculation_base import Calculation

class Multiplication(Calculation):
    """Multiplication class has a method to get the result of calculation from the parent class"""
    def get_result(self):
        """Returns result from the function"""
        return self.value_a * self.value_b
