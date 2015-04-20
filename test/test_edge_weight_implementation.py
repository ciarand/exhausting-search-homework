""" """

import pytest

from exhaustive_search.graph import Edge
from exhaustive_search.point import Point
from exhaustive_search.euclidean_mst import solve

def test_raises_exception_when_created_with_duplicate_point():
    """ an Edge between two of the same points should raise an exception """
    with pytest.raises(ValueError):
        Edge(Point(0, 0), Point(0, 0))

def test_correctly_calculates_the_weight_of_a_straight_edge():
    """ weight() should be able to handle a straight distance calculation """
    assert Edge(Point(0, 3), Point(0, 0)).weight() == 3, __doc__
    assert Edge(Point(3, 0), Point(0, 0)).weight() == 3, __doc__

def test_probably_correctly_compares_two_weights():
    """ weight() should be able to correctly compare two simple dissimilar points"""
    smaller = Edge(Point(0, 3), Point(0, 0)).weight()
    larger = Edge(Point(0, 3), Point(5, 0)).weight()

    assert larger > smaller, __doc__
    assert larger >= smaller, __doc__

    assert not larger < smaller, __doc__
    assert not larger <= smaller, __doc__

    assert larger != smaller, __doc__

    assert smaller < larger, __doc__
    assert smaller <= larger, __doc__

    assert not smaller > larger, __doc__
    assert not smaller >= larger, __doc__
