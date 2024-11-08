"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int):
        """Removes a certain amount of fish from river"""
        for _ in range(amount):  # iterates over all of fish up to amount
            self.fish.pop(0)  # pops first fish in given list

    def check_ages(self):

        bear_survivors: list[Bear] = []  # creates new empty list
        for x in self.bears:  # iterates over self.bears
            if x.age < 5:  # if a bear is younger than 5
                bear_survivors.append(x)  # they are a survivor

        fish_survivors: list[Fish] = []  # new empty list
        for x in self.fish:
            if x.age < 3:
                fish_survivors.append(x)  # appends survivors

        self.bears = bear_survivors  # updates lists to just include survivors
        self.fish = fish_survivors
        return None

    def bears_eating(self):
        return None

    def check_hunger(self):
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        print(f"~~~ Day {self.day} ~~~")
        print(f"Fish population: {len(self.fish)}")  # prints length of fish list
        print(f"Bear population: {len(self.bears)}")  # prints length of bear list
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        """Simulates one week of life in the river"""
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)  # runs function 7 times
