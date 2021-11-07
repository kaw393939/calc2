""" A collection of calculator functions """
class Calculator:
    """ This class is a collection of calculator functions """
    result = 0
    # Addition of two numbers
    def add(self, num1_a, num2_b):
        """ Function to add two numbers """
        self.num_a =  num1_a
        self.result = self.num_a + num2_b
        return self.result

    # Subtraction of two numbers
    def subtract(self, num1_a, num2_b):
        """ Function to subtract two numbers """
        self.num_a = num1_a
        self.result = self.num_a - num2_b
        return self.result

    # Multiplication of two numbers
    def multiply(self, num1_a, num2_b):
        """ Function to multiply two numbers """
        self.num_a = num1_a
        self.result = self.num_a * num2_b
        return self.result

    # Division of numbers and exception for division by 0
    def divide(self, num1_a, num2_b):
        """ Function to divide two numbers """
        self.num_a = num1_a
        if num2_b <= 0:
            return "Error: A number cannot be divided by 0"
        self.result = self.num_a / num2_b
        return self.result

    # Increment a number by 1
    def increment(self, num1_a):
        """ Function to increment a number by 1 """
        self.num_a = num1_a
        self.result = self.num_a + 1
        return self.result
