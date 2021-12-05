"""Calculation history Class"""

class CalculatorResult:
    """Calculations class manages the history of calculations"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clear the history of calculations"""
        CalculatorResult.history.clear()
        return True

    @staticmethod
    def count_history():
        """Get number ofCalculatorResult items in history"""
        return len(CalculatorResult.history)

    @staticmethod
    def get_last_calculation_object():
        """Get last calculation"""
        return CalculatorResult.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """Get last calculation convenience method"""
        calculation = CalculatorResult.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """Get first calculation"""
        return CalculatorResult.history[0]

    @staticmethod
    def get_calculation_from_history(num):
        """Get a specific calculation from history"""
        return CalculatorResult.history[num]

    @staticmethod
    def add_calculation_to_history(num):
        """Get a generic calculation from history"""
        return CalculatorResult.history.append(num)
