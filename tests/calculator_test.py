"""Testing the Calculator"""
import unittest
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1
def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(2,2)
    assert result == 4

def test_calculator_division():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result = calc.division_numbers(2,2)
    assert result == 1

class MyTestCase(unittest.TestCase):
    """A test case is the individual unit of testing.unittest provides a base class"""
    def test_calculator_divide_by_zero(self):
        """Testing the divide method of the calculator when dividing by zero"""
        with self.assertRaises(ZeroDivisionError):
            calc = Calculator()
            calc.division_numbers(2,0)
if __name__ == '__main__':
    unittest.main()
