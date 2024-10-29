"""Dictionary ???"""

__author__ = "730745012"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values"""

    dict_output: dict[str, str] = {}  # creates new dict in heap

    for key in dict_input:  # iterates over all keys in dict_input
        if dict_input[key] in dict_output:  # if that key is already dict_output
            raise KeyError(
                "Error: Cannot have multiples of the same key."
            )  # raise error
        dict_output[dict_input[key]] = (
            key  # value becomes key, key becomes value in output
        )

    return dict_output


def favorite_color(dict_input: dict[str, str]) -> str:
    """Returns color that appears most frequently"""

    color_tracker: dict[str, int] = {}  # starts with empty dict to track colors

    for name in dict_input:  # loops over dict_input
        color = dict_input[name]  # idenitfies each color
        if color in color_tracker:  # if color is already in tracker
            color_tracker[color] += 1  # add 1 to color_tracker
        else:
            color_tracker[color] = 1  # color stays at one

    max_count: int = 0  # max count starts at 0
    max_color: str = ""  # starts with empty string

    for name in dict_input:  # loops over color_tracker
        color = dict_input[name]  # identifies each color
        if (
            color_tracker[color] > max_count
        ):  # if value of color_tracker is greater than max count
            max_count = color_tracker[color]  # max count becomes color's value
            max_color = color  # color becomes max color

    return max_color


def count(list_input: list[str]) -> dict[str, int]:
    """Returns dict where list values are the key and the dict values are the frequency
    of appearance in the list."""

    dict_output: dict[str, int] = {}  # empty dict to store result

    for x in range(0, len(list_input)):  # loops over list
        if list_input[x] in dict_output:  # if value is a key in dict_output
            dict_output[list_input[x]] += 1  # add one to count
        else:
            dict_output[list_input[x]] = 1  # initialize count

    return dict_output


def alphabetizer(list_input: list[str]) -> dict[str, list[str]]:
    """Produces a dict wehre each key is a list and each value is a
    list of words that begin w the letter"""

    dict_output: dict[str, list[str]] = {}  # creates empty dict

    for word in list_input:  # iterates over list
        first_letter: str = word[0].lower()  # gets first lowercase letter of word
        if first_letter in dict_output:  # if letter is key in output
            dict_output[first_letter].append(word)  # appends word to list
        else:
            dict_output[first_letter] = [word]  # initialize list with word

    return dict_output


def update_attendance(dict_input: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance with new attendance info"""

    if day in dict_input:  # if day is already in dict
        if student not in dict_input[day]:  # if student is not already listed
            dict_input[day].append(student)  # adds student to list
    else:
        dict_input[day] = [student]  # creates new list w student
