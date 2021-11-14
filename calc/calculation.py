"""This is our calculation base class & abstract class"""
class Calculation: # pylint: disable=too-few-public-methods
    """constructor & it is the 1st function called when an object of the class is instantiated"""
    def __init__(self, value_a, value_b): # pylint: disable=too-few-public-methods
        """class factory method"""
        self.value_a = value_a
        self.value_b = value_b
    @classmethod
    def create(cls, value_a, value_b):
        """class method"""
        return cls(value_a, value_b)
