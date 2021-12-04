"""This is the division calculation that inherits the values from the calculations class"""
#This is called a namespace it is like files & folders.
#It looks like a folder & file path but it is a like a virtual representation

from calc.calculations.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Division(Calculation):
    """The addition class has one method to get the result of the calculation"""
    def get_result(self):
        """you need to use self to reference the data contained in the instance of the object"""
        #return self.value_a / self.value_b
        #initial_value = 1.0
        for index, value in enumerate(self.values):
            if index == 0:
                division_value = value
            else:
                division_value = division_value / value
        return round(division_value, 5)
