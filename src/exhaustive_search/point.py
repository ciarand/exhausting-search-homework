""" Point is copied directly from the provided stubcode """

class Point:
    """ Represents a single 2D point. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
