""" Graph is provided to add some structure to the algorithms """

import random, math

from .point import Point

class Edge:
    """ Edge represents a connection between two Points """
    def __init__(self, left, right):
        # guards
        if not isinstance(left, Point):
            raise TypeError("expected Point, got %s" % type(left))

        if not isinstance(right, Point):
            raise TypeError("expected Point, got %s" % type(right))

        if left.x == right.x and left.y == right.y:
            raise ValueError("x and y cannot be the same point")


        # deterministically order so __eq__ and __hash__ checks are easy.
        # Left.x is always >= than right.x
        # When left.x == right.x, left.y is always >= right.y
        if (left.x < right.x) or (left.x == right.x and left.y < right.y):
            left, right = right, left

        self.left = left
        self.right = right

    def weight(self):
        """ Calculate the weight for this edge """
        return math.sqrt(((self.left.y - self.right.y) ** 2) + ((self.left.x - self.right.x) ** 2))

    def connected_to(self, candidate):
        """ connected_to determines whether the given Point is a part of this
        Edge """
        return candidate == self.left or candidate == self.right

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(''.join(str(v) for v in [self.left.x, self.left.y]))

class Graph:
    """ Graph represents a collection of edges and points """
    def __init__(self, points):
        self.edges = set([])
        self.points = set([])

        for origin in points:
            self.points.add(origin)

            for dest in points:
                if dest != origin:
                    self.edges.add(Edge(origin, dest))

    def num_edges(self):
        """ num_edges returns the number of edges in the graph """
        return len(self.edges)

    def num_points(self):
        """ num_points returns the number of points in the graph """
        return len(self.points)

    def random_edge(self):
        """ returns one of the edges in the graph, chosen pseudorandomly """
        sample = random.sample(self.edges, 1)

        return sample[0] if len(sample) != 0 else None

    def random_point(self):
        """ returns one of the edges in the graph, chosen pseudorandomly """
        sample = random.sample(self.points, 1)

        return sample[0] if len(sample) != 0 else None
