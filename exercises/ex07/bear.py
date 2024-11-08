"""File to define Bear class."""


class Bear:

    age: int  # constructs attributes
    hunger_score: int

    def __init__(self):
        self.age = 0  # initializes outputs
        self.hunger_score = 0
        return None

    def one_day(self):
        self.age += 1  # increases age by 1
        return None
