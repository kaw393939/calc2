"""This is going to be the Calculator object"""

class Calculation:
    """Initializing variables"""
    def __init__(self, value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

# Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        """Using class method to create objects of all individual operations"""
        return cls(value_a,value_b)
