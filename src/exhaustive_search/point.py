""" Point represents my additions to the Point class. StubPoint is the provided
Point class. """

import math

class StubPoint:
    """ Represents a single 2D point. """

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point(StubPoint):
    """ Point provides some helpful additions on top of the StubPoint implementation """
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return math.floor(1000 * self.x) + math.floor(self.y)
        return int("{0:0>16}{1:0>16}".format(self.x, self.y))

    def __str__(self):
        return "Point(x=%d, y=%d)" % (self.x, self.y)
