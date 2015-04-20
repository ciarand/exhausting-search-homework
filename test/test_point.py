""" Tests the Point class """

from exhaustive_search.point import Point

def test_equality_is_based_on_value():
    """ equality between two Points should be based off value, not address """
    # 50 ** 2 == 2500 runs
    maximum = 50
    universe_1, universe_a = [], []

    for x in range(maximum):
        for y in range(maximum):
            universe_1.append(Point(x, y))
            universe_a.append(Point(x, y))

    for leftkey, left in enumerate(universe_1):
        for rightkey, right in enumerate(universe_a):
            if leftkey == rightkey:
                assert left == right, __doc__
            else:
                assert left != right, __doc__
