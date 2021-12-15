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
            
"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
