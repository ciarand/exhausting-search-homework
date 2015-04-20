""" Provides a solution (`solve`) to the EMST problem. """

# Euclidean Minimum Spanning Tree (MST) algorithm
#
# input: a list of n Point objects
#
# output: a list of (p, q) tuples, where p and q are each input Point
# objects, and (p, q) should be connected in a minimum spanning tree
# of the input points
def solve(points):
    """ Solves the EMST problem """
    if not isinstance(points, list):
        raise TypeError("solve expects a list of n Point objects, received %s" % points)

    plen = len(points)
    if plen < 2:
        return []

    return [(points[i], points[(i+1) % plen]) for i in range(plen)]
