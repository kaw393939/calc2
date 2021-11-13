""" This is the increment function"""
#1st import he addition namespace
from calc.additon import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def get_results_of_first_calculation_added_to_history():
        return Calculator.history[0].getResult()

    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_results_of_last_calculation_added_to_history():
        #-1 gets last item added to list
        return Calculator.history[-1].getResult()
    @staticmethod
    #this is an example of a calling method
    def add_number(value_a, value_b):
        """ adds number to result"""
        #create an addition object using the factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_results_of_last_calculation_added_to_history()
    @staticmethod
    #this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        # create a subtraction object using the factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_results_of_last_calculation_added_to_history()
    @staticmethod
    #this is an example of a calling method
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        # create a multiplication object using the factory we created on the calculation class
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_results_of_last_calculation_added_to_history()
