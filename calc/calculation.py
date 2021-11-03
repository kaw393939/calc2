"""This is going to be the Calculator object"""

class Calculation:
    """Initializing variables"""
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

# Class Factory Method
    """Using class method to create objects of the individual operations methods"""
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
