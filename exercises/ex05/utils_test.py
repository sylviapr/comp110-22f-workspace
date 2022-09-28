"""Tests for each of our functions in EX05."""


__author__ = "730575415"


from exercises.ex05.utils import only_evens


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_one_ten() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_only_evens_odds() -> None:
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_two_eight() -> None:
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


from exercises.ex05.utils import concat


def test_concat_normal() -> None:
    a: list[int] = [1, 2, 3, 4]
    b: list[int] = [5, 6, 7, 8]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_no_b() -> None:
    a: list[int] = [1, 2, 3, 4]
    b: list[int] = []
    assert concat(a, b) == [1, 2, 3, 4]


def test_concat_tens() -> None:
    a: list[int] = [10, 20, 30, 40]
    b: list[int] = [50, 60, 70, 80]
    assert concat(a, b) == [10, 20, 30, 40, 50, 60, 70, 80]


from exercises.ex05.utils import sub


def test_sub_no_list() -> None:
    l: list[int] = []
    a: int = 1
    b: int = 3
    assert sub(l, a, b) == []


def test_sub_normal() -> None:
    l: list[int] = [10, 20, 30, 40, 50]
    a: int = 1
    b: int = 4
    assert sub(l, a, b) == [20, 30, 40]


def test_sub_start_negative() -> None:
    l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    a: int = -2
    b: int = 3
    assert sub(l, a, b) == [1, 2, 3]
