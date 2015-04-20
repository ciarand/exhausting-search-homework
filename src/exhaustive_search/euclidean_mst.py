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

    graph = Graph(points)

    if graph.num_edges() < 1:
        return []

    edges = graph.edges
    num_points = graph.num_points()
    start = edges.pop()
    spanned = set([start])
    solution = [(start.left, start.right)]

    print("beginning main loop")
    while len(spanned) < num_points - 1:
        smallest_edge = None

        for spanned_edge in spanned:
            print("inner loop (spanned)")
            for candidate_edge in edges:
                print("inner loop (candidate_edge)")
                # if the candidate isn't connected to our lil spanned set,
                # ignore it
                if not candidate_edge.connected_to(spanned_edge.left) \
                        and not candidate_edge.connected_to(spanned_edge.right):

                    continue

                if smallest_edge is None or candidate_edge.weight() < smallest_edge.weight():
                    smallest_edge = candidate_edge

        print("extending edge %s" % smallest_edge)
        edges.remove(smallest_edge)
        spanned.add(smallest_edge)
        solution.append((smallest_edge.left, smallest_edge.right))

    return solution
