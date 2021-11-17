"""Subtraction calculation that inherits value A and value B from the calculation class"""

from calc.calculation_base import Calculation

class Subtraction(Calculation):
    """Subtraction class method will get the result of A and B from the parent class"""
    def get_result(self):
        """Get result from calculation"""
        return self.value_a - self.value_b
