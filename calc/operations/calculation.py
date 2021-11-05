"""Operation"""


class Calculation:  # pylint: disable=too-few-public-methods
    """Operation Class"""

    def __init__(self, *args):
        """default constructor setting up value variables"""
        self.values = args

    @classmethod
    def create(cls, *args):
        """class method create"""
        return cls(args)
