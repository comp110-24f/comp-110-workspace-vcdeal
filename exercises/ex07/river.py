"""File to define River class."""

__author__ = "730745012"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int):
        """Removes a certain amount of fish from river."""
        for _ in range(amount):  # iterates over all of fish up to amount
            self.fish.pop(0)  # pops first fish in given list

    def check_ages(self):
        """Kills old animals rip."""
        bear_survivors: list[Bear] = []  # creates new empty list
        for bear in self.bears:  # iterates over self.bears
            if bear.age <= 5:  # if a bear is younger/equal than 5
                bear_survivors.append(bear)  # they are a survivor

        fish_survivors: list[Fish] = []  # new empty list
        for fish in self.fish:
            if fish.age <= 3:
                fish_survivors.append(fish)  # appends survivors

        self.bears = bear_survivors  # updates lists to just include survivors
        self.fish = fish_survivors
        return None

    def bears_eating(self):
        """Bears eat fish."""
        for bear in self.bears:  # iterates over bears
            if len(self.fish) >= 5:  # if there are more than 5 fish
                River.remove_fish(self, 3)  # remove three fish
                Bear.eat(
                    bear, 3
                )  # bear eats three fish, idk if self = bear is correct?
        return None

    def check_hunger(self):
        """Bears die if they are too hungry."""
        alive_bears: list[Bear] = []  # creates new empty list

        for bear in self.bears:  # iterates over bears
            if bear.hunger_score >= 0:  # if bear's hunger score is good
                alive_bears.append(bear)  # they stay alive

        self.bears = alive_bears  # only alive bears make it

        return None

    def repopulate_fish(self):
        """New fish, making babies."""
        new_fish_amt = (len(self.fish) // 2) * 4

        for _ in range(new_fish_amt):  # for each new fish
            self.fish.append(Fish())  # append a fish

        return None

    def repopulate_bears(self):
        """New bears, making babies."""
        new_bears_amt = len(self.bears) // 2

        for _ in range(new_bears_amt):  # for the amount of new bears
            self.bears.append(Bear())  # append a bear
        return None

    def view_river(self):
        """Gives output."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")  # prints length of fish list
        print(f"Bear population: {len(self.bears)}")  # prints length of bear list
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week of life in the river."""
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)  # runs function 7 times
