"""This is the addition calculation that is being inherits the value
A and value B from the calculation class"""
#this is called a namespace it is like files and
# folders the classes are files and the folders organize the classes
#It looks like a folder and file path but it
# is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Division(Calculation):
    """This is how you extend the Addition class with the Calculation"""

    def __init__(self, value_a, value_b):
        super().__init__(value_a, value_b)
        self.result = round((float(self.value_a) / float(self.value_b)), 9)

    def getresult(self):
        """you need to use self to reference the data contained in the instance of the object. """
        return self.result
