""" Tests the implementation of the solution to the Euclidean Minimum Spanning
Tree (EMST) problem """

import pytest

from exhaustive_search.point import Point
from exhaustive_search.euclidean_mst import solve

def test_empty_mst_list():
    """ the (E)MST solution to an empty list is an empty list """
    assert solve([]) == [], __doc__

def test_non_list():
    """ this function should reject non-lists (invalid inputs) by raising
    a TypeError """

    with pytest.raises(TypeError):
        solve(True)

def test_list_of_one():
    """ the (E)MST solution to a list of one is an empty list """
    assert solve([True]) == [], __doc__

def test_list_of_two():
    """ the (E)MST solution to a list of two points (i.e. [a, b]) is a list
    containing a tuple of points (i.e. [(a, b)]) """
    one, two = Point(3, 1), Point(1, 3)
    assert solve([one, two]) == [(one, two)], __doc__
