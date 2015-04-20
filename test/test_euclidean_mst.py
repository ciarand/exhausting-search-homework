""" Tests the implementation of the solution to the Euclidean Minimum Spanning
Tree (EMST) problem """

import pytest

from exhaustive_search.point import Point
from exhaustive_search.euclidean_mst import solve

def compare_solutions(actual, expected):
    assert len(actual) == len(expected), "expected %d to equal %d" % (len(actual), len(expected))

    for result in actual:
        aleft, aright = result
        found = False

        for expectation in expected:
            eleft, eright = expectation

            if (aleft == eleft and aright == eright) or (aright == eleft and aleft == eright):
                found = True
                continue

        assert found, "expected to find edge (%s, %s) in result" % (aleft, aright)

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

    actual = solve([one, two])
    assert actual == [(one, two)] or actual == [(two, one)], __doc__

def test_triangle():
    """ Given a list of points L:

        L = [Point(0, 0), Point(3, 0), Point(6, 0)]

    The solution is:

        [(Point(0, 0), Point(3, 0)), (Point(3, 0), Point(6, 0))]
    """
    graph = [Point(0, 0), Point(3, 0), Point(6, 0)]

    actual = solve(graph)

    compare_solutions(actual, [(Point(0, 0), Point(3, 0)), (Point(3, 0), Point(6, 0))])

    for result in actual:
        left, right = result

        if left == Point(0, 0) or left == Point(6, 0):
            assert right == Point(3, 0), \
                "expected right (%s) to == %s (left is %s)" % (right, Point(3, 0), left)
        else:
            assert right == Point(0, 0) or right == Point(6, 0), \
                "expected right (%s) to == %s or %s" % (right, Point(0, 0), Point(6, 0))
