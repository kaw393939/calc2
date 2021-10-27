class Calculator:
    """ This is the Calculator class"""

    def __init__(self):
        pass

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

    def multiply_number(self, value_a):
        """multiply result by number"""
        self.result = self.result * value_a
        return self.result

    def divide_number(self, value_a):
        """divide results by number"""
        if value_a == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = self.result / value_a
        return self.result
