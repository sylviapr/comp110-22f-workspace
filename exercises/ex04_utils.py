"""An exercise to better understand lists!"""

__author__ = "730575415"

# Given a list of ints and an int -> bool to indicate if all the ints in the list are the same as the lone int
# Returns false if the list is empty
# Function named all

def all(list: list[int], integer: int) -> bool:
    """Tells us if all of the ints in a list are equal to a specific int."""
    list_len: int = len(list)
    i: int = 0
    if len(list) == 0:
        return False
    while i < list_len:
        if list[i] != integer:
            return False
        else:
            i = i +1
    return True

def max(list: list[int]) -> int:
    """Given a list of int values, returns the largest one in the list."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    largest_int: int = list[0]
    if len(list) == 1:
        return list[0]
    while i < len(list):
        if list[i] > largest_int:
            largest_int = list[i]
        i = i + 1
    return largest_int

def is_equal(a: list[int], b: list[int]) -> bool:
    """When given two lists of ints, returns True if they are the same list at every index."""
    if len(a) != len(b):
        return False
    i: int = 0
    while len(a) == len(b) and i < len(a):
        if a[i] == b[i]:
            i = i + 1
        else: return False
    return True
    
        
        
