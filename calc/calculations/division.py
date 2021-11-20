"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Class to divide"""

    def get_result(self):
        """Gets division results with error if dividing by 0"""
        quotient = self.values[0]
        for value in self.values[1:]:
            if value == 0.0:
                return "Cannot divide by zero"
            quotient = quotient / value
        return quotient
