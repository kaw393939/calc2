"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """Division calculation object"""

    def get_result(self):
      try:
        """ divide two numbers and store the result"""
        result = 1.0
        for value in self.values:
            result = result / value
        return result
      except ZeroDivisionError:
            print("Divide by Zero")
