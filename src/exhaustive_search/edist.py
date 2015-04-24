import math

def edist(lpoint, rpoint):
    """ Calculates the Euclidean distance between two Points """
    return math.sqrt(((lpoint.x - rpoint.x) ** 2) + ((lpoint.y - rpoint.y) ** 2))

