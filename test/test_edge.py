""" Tests that Edge is performing as expected """

import pytest

from exhaustive_search.graph import Edge
from exhaustive_search.point import Point

def test_duplicate_points_are_invalid():
    """ an Edge between two of the same points should raise an exception """
    with pytest.raises(ValueError):
        Edge(Point(0, 0), Point(0, 0))

def test_weight_calculation():
    """ weight() should be able to handle a straight distance calculation """

    assert Edge(Point(0, 3), Point(0, 0)).weight() == 3, __doc__
    assert Edge(Point(3, 0), Point(0, 0)).weight() == 3, __doc__

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

    assert Edge(Point(0, 0), Point(5, 5)).weight() > Edge(Point(0, 0), Point(4, 5)).weight(), \
        __doc__

def test_equality_is_order_independent():
    """ equality between two Edges should be calculated in such a way that the
    order of the points in the constructor is independent of the equality. """

    foo_edge = Edge(Point(0, 0), Point(1, 1))
    bar_edge = Edge(Point(1, 1), Point(0, 0))

    assert foo_edge == bar_edge, __doc__

def test_connected_to():
    """ Edges should be able to correctly report whether they are connected to
    a given Point """

    left, right = (Point(0, 0), Point(1, 1))
    left_to_right = Edge(left, right)
    right_to_left = Edge(right, left)

    for edge in [left_to_right, right_to_left]:
        assert edge.connected_to(Point(0, 0)), __doc__
        assert edge.connected_to(Point(1, 1)), __doc__
        assert not edge.connected_to(Point(0, 1)), __doc__
        assert not edge.connected_to(Point(1, 0)), __doc__
