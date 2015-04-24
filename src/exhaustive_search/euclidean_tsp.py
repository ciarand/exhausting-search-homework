""" Provides a solution (`solve`) to the ETSP problem. """

from .edist import edist
import itertools

# Euclidean Traveling Salesperson (TSP) algorithm
#
# input: a list of n Point objects
#
# output: a permutation of the points corresponding to a correct
# Hamiltonian cycle of minimum total distance
def solve(points):
    """ Solves the ETSP problem """

    best_weight = None
    best_route = None

    for candidate in itertools.permutations(points, len(points)):
        candidate_weight = calculate_candidate_weight(candidate)
        if best_weight is None or candidate_weight < best_weight:
            best_weight = candidate_weight
            best_route = candidate

    return best_route

def calculate_candidate_weight(candidate):
    weight = 0
    for i in range(len(candidate) - 1):
        weight += edist(candidate[i], candidate[i+1])

    # then hook it back around
    weight += edist(candidate[0], candidate[-1])

    return weight

