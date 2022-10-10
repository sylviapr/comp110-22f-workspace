"""Dictionary functions."""

__author__ = "730575415"

def invert(input: dict[str, str]) -> dict[str, str]:
    """A function that takes in a dictionary[str, str] and returns a new dictionary that has inverted the keys and values of the original."""
    result: dict[str, str]
    result = dict()
    for key in input:
        result = {[input[key]]: key}


        # result[input[key]] == key
    return result
