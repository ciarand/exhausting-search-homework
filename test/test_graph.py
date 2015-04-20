""" Tests the graph implementation """

from exhaustive_search.graph import Graph, Edge
from exhaustive_search.point import Point

def test_empty_list():
    """ Instantiating a Graph with an empty list should return an empty Graph """
    assert Graph([]).num_edges() == 0, __doc__

def test_list_of_one():
    """ Instantiating a Graph with a list of 1 should return a Graph with
    0 edges """
    assert Graph([Point(0, 1)]).num_edges() == 0, __doc__

def test_list_of_two():
    """ Instantiating a Graph with a list of 2 should return a Graph with
    1 edge """
    assert Graph([Point(0, 1), Point(1, 0)]).num_edges() == 1, __doc__

def test_list_of_duplicate_points():
    """ Instantiating a Graph with duplicate points should ignore the dupes """

    assert Graph([Point(0, 1), Point(0, 1), Point(0, 1), Point(1, 0)]).num_edges() == 1, __doc__

def test_list_of_three_points():
    """ Instantiating a Graph with 3 different points should create 3 unique
    edges """

    graph = Graph([Point(0, 0), Point(1, 1), Point(2, 0)])

    assert graph.num_edges() == 3, __doc__
    assert graph.num_points() == 3, __doc__

def test_list_of_four_points():
    """ Instantiating a Graph with 4 different points should create 6 unique
    edges """

    graph = Graph([Point(0, 0), Point(1, 1), Point(1, 0), Point(0, 1)])

    assert graph.num_edges() == 6, __doc__
    assert graph.num_points() == 4, __doc__

def test_random_edge_returns_an_edge():
    """ the random_edge methods needs to return an Edge """

    redge = Graph([Point(0, 0), Point(1, 1), Point(1, 0), Point(0, 1)]) \
            .random_edge()

    assert isinstance(redge, Edge), __doc__

def test_random_point_returns_an_point():
    """ the random_point methods needs to return an point """

    rpoint = Graph([Point(0, 0), Point(1, 1), Point(1, 0), Point(0, 1)]) \
            .random_point()

    assert isinstance(rpoint, Point), __doc__
