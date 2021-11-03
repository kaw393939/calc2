"""This is division operation object"""

from calc.calculation import Calculation

"""This is division operation class"""
class Division(Calculation):
    """Dividing two numbers"""
    def get_Result(self):
        return self.value_a / self.value_b
