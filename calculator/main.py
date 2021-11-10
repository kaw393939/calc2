""" This is the increment function"""


class Calculator:
    """ This is the Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add(self, value_a):
        """ Adding Numbers"""
        self.result = self.result + value_a
        return self.result

    def subtract(self, value_a):
        """ Subtracting numbers"""
        self.result = self.result - value_a
        return self.result

    def multiply(self, value_a, value_b):
        """ Multiplying Numbers"""
        self.result = value_a * value_b
        return self.result

    def division(self, div_1, div_2):
        """ Dividing Numbers"""
        div_1 = float(div_1)
        div_2 = float(div_2)
        if div_1 == 0 or div_2 == 0:
            raise ZeroDivisionError("Cannot divide by 0!")
        self.result = div_1 / div_2
        return self.result
