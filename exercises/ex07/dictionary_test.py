"""Tests for our dictionary functions."""


__author__ = "730575415"


from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_keyerror() -> None:
    """Testing invert with a dictionary that contains a repeated value."""
    # Edge case
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_short() -> None:
    """Testing invert with a short regular dictionary."""
    xs: dict[str, str] = {'cat': 'oreo', 'dog': 'addy'}
    assert invert(xs) == {'oreo': 'cat', 'addy': 'dog'}


def test_invert_long() -> None:
    """Testing invert with a longer list."""
    xs: dict[str, str] = {'cat': 'oreo', 'dog': 'addy', 'bird': 'mango', 'cow': 'bessie', 'lizard': 'rango', 'chicken': 'hen solo'}
    assert invert(xs) == {'oreo': 'cat', 'addy': 'dog', 'mango': 'bird', 'bessie': 'cow', 'rango': 'lizard', 'hen solo': 'chicken'}


def test_favcolor_norepeats() -> None:
    """Testing favorite_color for a dict with no repeated colors."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "red"}
    assert favorite_color(xs) == 'yellow'


def test_favcolor_repeat() -> None:
    """Testing favorite_color for a dict with one color that is repeated and another color that isn't."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == 'blue'


def test_favcolor_comp110() -> None:
    """Testing favorite_color for a dict in which the group's favorite color is no color at all, but rather comp110."""
    xs: dict[str, str] = {"Marc": "comp110", "Ezri": "comp110", "Kris": "comp110", "Abigail": "blue"}
    assert favorite_color(xs) == 'comp110'


def test_count_no_repeats() -> None:
    """Testing count with a list that has no repeated strs."""
    xs: list[int] = ["s", "y", "l", "v", "i", "a"]
    assert count(xs) == {'s': 1, 'y': 1, 'l': 1, 'v': 1, 'i': 1, 'a': 1}


def test_count_repeats() -> None:
    """Testing count with a list that does have repeated strs."""
    assert count(["e", "s", "t", "e", "l", "l", "e"]) == {"e": 3, "s": 1, "t": 1, "l": 2}


def test_count_numberstrs() -> None:
    """Testing count with strings that consist of numbers."""
    assert count(["1", "2", "3", "4", "5"]) == {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}