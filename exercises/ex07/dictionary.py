"""Dictionary functions."""

__author__ = "730575415"

def invert(input: dict[str, str]) -> dict[str, str]:
    """A function that takes in a dictionary[str, str] and returns a new dictionary that has inverted the keys and values of the original."""
    result: dict[str, str] = {}
    for key in input:
        if input[key] in result:
            raise KeyError("Make sure that no values are repeated in the input dictionary.")
        result[input[key]] = key
    return result


def favorite_color(names: dict[str, str]) -> str:
    """Given an input of a dict[str, str] consisting of names and favorite colors, returns a str that says the color that appears the most frequently in the input."""
    colors: list[str] = []
    counted_colors: dict[str, int] = {}
    max: int = 0
    max_color: str = ""
    for name in names:
        colors.append(names[name])
    counted_colors = count(colors)
    
    for i in counted_colors:
        if counted_colors[i] > max:
            max = counted_colors[i]
            max_color = i
    return max_color
    

def count(letters: list[str]) -> dict[str, int]:
    """Takes a list of strings and returns a dict that contains list values as keys and the number of times they were in the list as values."""
    result: dict[str, int] = {}
    for item in letters:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result