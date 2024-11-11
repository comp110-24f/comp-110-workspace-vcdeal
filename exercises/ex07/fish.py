"""File to define Fish class."""

__author__ = "730745012"


class Fish:
    """Basic Fish!"""

    age: int  # constructs attribute

    def __init__(self):
        """All fish are 0 when born."""
        self.age = 0  # intitalizes output
        return None

    def one_day(self):
        """Simulates day of fish."""
        self.age += 1  # increases age by one
        return None
