"""This is the subtraction calculation that inherits the value A and value B from the calculations class"""
#This is called a namespace it is like files & folders. The classes are files and the folders organize the classes
#It looks like a folder & file path but it is a like a virtual representation of how the program is oganized

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    """The addition class has one method to get the result of the calculation. The calculation for value A & value B comes from the calculation parent class"""
    def getResult(self):
        #you need to use self to reference the data contained in the instance of the object. This is encapsulation
        return self.value_a - self.value_b

