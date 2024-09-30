"""Basic syntax of lists."""

# Creating a list

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor
# print(my_numbers)

# String Analogy
# my_name: str = "" #literal
# my_name: str = str() # constructor

# Adding a value to a list

my_numbers.append(1.5)
my_numbers.append(2.3)
# print(my_numbers)

# Creating an already populated list

game_points: list[int] = [102, 86, 94]
# print(game_points)

# Subscription Notation/Indexing

# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# Modifying by Index

game_points[1] = 72
# print(game_points)

# Length of lists

len(game_points)
# print(len(game_points))

# Remove an item from a list

game_points.pop(1)
# print(game_points)

# Practice Making a list


def display(list_input: list) -> None:
    """Displays all elements of a given list."""
    index: int = 0
    while index < len(
        list_input
    ):  # while the index is less than the length of the list
        print(list_input[index])  # print list value at given index
        index += 1  # add one to index


display(list_input=game_points)
