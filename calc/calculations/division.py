"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Calculation division class"""
    def get_result(self):
        """Get the division results"""
        return self.value_a / self.value_b
