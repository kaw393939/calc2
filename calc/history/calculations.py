"""Calculation history Class"""
class Calculations:
    """class Calculations"""
    history = []
    # pylint: disable=too-few-public-methods
    """This is the history static property"""
    @staticmethod
    def clear_history():
        """ clear history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """ get count from history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """ get last calculation from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """ get a first calculation from history"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
