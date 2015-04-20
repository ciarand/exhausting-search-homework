""" Graph is provided to add some structure to the algorithms """

import math

class Edge:
    def __init__(self, left, right):
        if left.x == right.x and left.y == right.y:
            raise ValueError("x and y cannot be the same point")

        # deterministically order so __eq__ and __hash__ checks are easy
        if (left.x < right.x) or (left.x == right.x and left.y < right.y):
            left, right = right, left

        self.left = left
        self.right = right

    def weight(self):
        return math.sqrt(((self.left.y - self.right.y) ** 2) + ((self.left.x - self.right.x) ** 2))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash(''.join(str(v) for v in [self.left.x, self.left.y]))

class Graph:
    def __init__(self, points):
        self.edges = set([])

        for origin in points:
            for dest in points:
                if dest != origin:
                    self.edges.add(Edge(origin, dest))

    def num_edges(self):
        return len(self.edges)

    def __iter__(self):
        return iter(self.edges)
