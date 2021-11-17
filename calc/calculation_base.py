"""This is our calculation base class / Abstract Class"""
class Calculation: # pylint: disable=too-few-public-methods
    """Base class for calculation """
    #contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self,value_a, value_b):
        """Initiate and encapsulate the values"""
        self.value_a = value_a
        self.value_b = value_b
    # Class Factory Method <- bound to the class and not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        """ Clear function"""
        return cls(value_a,value_b)
