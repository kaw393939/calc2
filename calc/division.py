"""Divide calculation that inherits the value A and value B from the calculation class"""

from calc.calculation_base import Calculation

class Divide(Calculation):
    """Divide class has a method to get the result of calculation from the parent class"""
    def get_result(self):
        """Returns result from the function"""
        if self.value_b <= 0:
            return "Error"
        return self.value_a / self.value_b
