"""EX05 utils"""


__author__ = "730575415"


def only_evens(input: list[int]) -> list[int]:
    """User input is a list of ints, function returns only the even ints from the list."""
    output: list[int] = []
    for result in input:
        if result % 2 == 0:
            output.append(result)
    print(output)


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """User inputs two lists of ints and the function returns the entirety of the first list followed by the entirety of the second."""
    