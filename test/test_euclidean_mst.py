""" Tests the implementation of the solution to the Euclidean Minimum Spanning
Tree (EMST) problem """

import pytest

from exhaustive_search.euclidean_mst import solve

def test_empty_mst_list():
    """ the (E)MST solution to an empty list is an empty list """
    assert solve([]) == [], __doc__

def test_non_list():
    """ this function should reject non-lists (invalid inputs) by raising
    a TypeError """

    with pytest.raises(TypeError):
        solve(True)

