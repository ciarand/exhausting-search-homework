""" Provides a solution (`solve`) to the EMST problem. """

from .edist import edist
from operator import itemgetter

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

    plen = len(points)
    if plen < 2:
        return []

    # preallocate a simple map to tell us whether a Point is spanned
    spanned = [False] * plen
    # span the first point
    spanned[0] = True
    edges = []
    result = []

    for lkey, left in enumerate(points):
        for rkey, right in enumerate(points):
            #if left != right:
            edges.append((lkey, rkey, edist(left, right)))

    edges.sort(key=itemgetter(2))

    while len(result) < plen - 1:
        for edge in edges:
            lkey, rkey, _ = edge
            if spanned[lkey] != spanned[rkey]:
                result.append((points[lkey], points[rkey]))
                spanned[lkey] = spanned[rkey] = True
                break

    return result
