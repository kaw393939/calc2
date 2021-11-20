"""History calculation class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class Calculations:
    """Calculations class for history of calculations"""

    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """Clears history values"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """Gets count of history file"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """Gets last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation_object():
        """Gets first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_last_calculation_result():
        """Gets last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation_result():
        """Gets first calculation"""
        calculation = Calculations.get_first_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_calculation(num):
        """Gets calculation"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """Adds calculation to history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """Adds addition object to history"""
        Calculations.add_calculation(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Adds subtraction object to history"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Adds multiplication object to history"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Adds division object to history"""
        Calculations.add_calculation(Division.create(values))
        return True
