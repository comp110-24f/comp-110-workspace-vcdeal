"""File to define Fish class."""


class Fish:

    age: int  # constructs attribute

    def __init__(self):
        self.age = 0  # intitalizes output
        return None

    def one_day(self):
        self.age += 1  # increases age by one
        return None
