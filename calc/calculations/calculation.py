#"""This is our calculation base class & abstract class"""
#class Calculation: # pylint: disable=too-few-public-methods
#    """constructor & it is the 1st function called when an object of the class is instantiated"""
#    def __init__(self, value_a, value_b): # pylint: disable=too-few-public-methods
#        """class factory method"""
#        self.value_a = value_a
#        self.value_b = value_b
#    @classmethod
#    def create(cls, value_a, value_b):
#        """class method"""
#        return cls(value_a, value_b)
"""Calculation Class"""
from abc import abstractmethod

class Calculation:
    """ calculation abstract base class"""
    def __init__(self,values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """ standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float

    @classmethod
    def create(cls, values: tuple):
        """Factory method -class method to create objects of all individual operations"""
        return cls(values)

    @abstractmethod
    def get_result(self):
        """creating this class to show overriding polymorphism"""
        return True
