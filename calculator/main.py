""" main.py: holds the Calculator class definition"""
class Calculator:
    """ This is the Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_number(self, value_a, value_b):
        """multiply result by number"""
        self.result = value_a * value_b
        return self.result

    def divide_number(self, value_a, value_b):
        """divide results by number"""
        if value_b == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = value_a / value_b
        return self.result
