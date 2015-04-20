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

    # NOTE: this does some initialization work
    graph = Graph(points)

    if graph.num_edges() < 1:
        return []

    edges = graph.edges
    points = graph.points
    num_points = len(graph.points)

    start = points.pop()
    spanned = set([start])
    solution = []

    while len(solution) < num_points - 1:
        smallest_edge = None
        candidate_point = None

        for spanned_point in spanned:
            for candidate_edge in edges:
                # if the candidate isn't connected to our lil spanned set, ignore it
                if not candidate_edge.connected_to(spanned_point):
                    continue

                if smallest_edge is None or candidate_edge.weight() < smallest_edge.weight():
                    smallest_edge = candidate_edge

                    if spanned_point == smallest_edge.left:
                        candidate_point = smallest_edge.right
                    else:
                        candidate_point = smallest_edge.left

        spanned.add(candidate_point)

        edges.remove(smallest_edge)
        extension = (smallest_edge.left, smallest_edge.right)
        solution.append(extension)

    return solution
