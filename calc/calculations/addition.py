"""This is the addition calculation that inherits values from the calculations class"""
#This is called a namespace it is like files & folders.
#It looks like a folder & file path but it is a like a virtual representation
from calc.calculations.calculation import Calculation
#This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    """The addition class has one method to get the result of the calculation"""
    def get_result(self):
        """Get the addition result"""
        return self.value_a + self.value_b
