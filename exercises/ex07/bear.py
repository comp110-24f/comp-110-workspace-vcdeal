"""File to define Bear class."""

__author__ = "730745012"


class Bear:
    """Basic Bear!"""

    age: int  # constructs attributes
    hunger_score: int

    def __init__(self):
        """All bears are 0 and hungry."""
        self.age = 0  # initializes outputs
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulates day of bear."""
        self.age += 1  # increases age by 1
        self.hunger_score -= 1  # decreases hunger by one
        return None

    def eat(self, num_fish: int):
        """Bear eats fish."""
        self.hunger_score += num_fish
        return None
