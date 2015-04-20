""" Graph is provided to add some structure to the algorithms """

class Edge:
    def __init__(self, left, right):
        if left.x == right.x and left.y == right.y:
            raise ValueError("x and y cannot be the same point")

        self.left = left
        self.right = right

    def weight(self):
        return self.left.y - self.right.y

class Graph:
    def __init__(self, points):
        edges = []

        for origin in points:
            for dest in points:
                edges.append(Edge(origin, dest))

