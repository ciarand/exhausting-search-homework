""" Provides a solution (`solve`) to the EMST problem. """

from .graph import Graph

# Euclidean Minimum Spanning Tree (MST) algorithm
#
# input: a list of n Point objects
#
# output: a list of (p, q) tuples, where p and q are each input Point
# objects, and (p, q) should be connected in a minimum spanning tree
# of the input points
def solve(points):
    """ Solves the EMST problem """
    # it's not a list
    if not isinstance(points, list):
        raise TypeError("solve expects a list of n Point objects, received %s" % points)

    g = Graph(points)

    if g.num_edges() < 1:
        return []

    return []
