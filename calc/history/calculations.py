"""Calculation history Class"""
class Calculations:
    """Calculation class"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """It will clear the history list"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """It will count the history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation():
        """It will get the last calculation from calculator"""
        return Calculations.history[-1]
    @staticmethod
    def get_first_calculation():
        """It will get the first calculation from calculator"""
        return Calculations.history[-1]
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)