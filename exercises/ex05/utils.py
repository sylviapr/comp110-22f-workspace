"""Some utility functions that help us manipulate lists without changing the inputs."""


__author__ = "730575415"


def only_evens(input: list[int]) -> list[int]:
    """User input is a list of ints, function returns only the even ints from the list."""
    output: list[int] = []
    for checking in input:
        if checking % 2 == 0:
            output.append(checking)
    return output


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """User inputs two lists of ints and the function returns the entirety of the first list followed by the entirety of the second."""
    output: list[int] = []
    for index_a in list_a:
        output.append(index_a)
    for index_b in list_b:
        output.append(index_b)
    return output


def sub(input: list[int], start_i: int, end_i: int):
    """Given a list of ints and two indexes, this function will list all the ints between those two indexes."""
    output: list[int] = []
    if start_i < 0:
        start_i = 0
    if end_i > len(input):
        end_i = len(input)
    if len(input) == 0 or start_i > len(input) or end_i < 0:
        return [] 
    i: int = start_i
    while i < end_i:
        output.append(input[i])
        i += 1
    return output
