###############################################################################
# CPSC 335 Project 2
# Spring 2015
#
# Authors: <FILL IN YOUR NAME(S) HERE>
###############################################################################

# constant parameters
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
CANVAS_MARGIN = 20
POINT_COLOR = 'gray'
MST_EDGE_COLOR = 'red'
TSP_EDGE_COLOR = 'navy'
POINT_RADIUS = 3
OUTLINE_WIDTH = 2

import enum, math, random, time, tkinter

# Class representing one 2D point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Euclidean Minimum Spanning Tree (MST) algorithm
#
# input: a list of n Point objects
#
# output: a list of (p, q) tuples, where p and q are each input Point
# objects, and (p, q) should be connected in a minimum spanning tree
# of the input points
def euclidean_mst(points):
    # clearly incorrect
    n = len(points)
    return [ (points[i], points[(i+1) % n]) for i in range(n) ]

# Euclidean Traveling Salesperson (TSP) algorithm
#
# input: a list of n Point objects
#
# output: a permutation of the points corresponding to a correct
# Hamiltonian cycle of minimum total distance
def euclidean_tsp(points):
    # clearly incorrect
    return points

###############################################################################
# The following code is responsible for generating instances of random
# points and visualizing them. You can leave it unchanged.
###############################################################################

# input: an integer n >= 0
# output: n Point objects with all coordinates in the range [0, 1]
def random_points(n):
    return [Point(random.random(), random.random())
            for i in range(n)]

# translate coordinates in [0, 1] to canvas coordinates
def canvas_x(x):
    return CANVAS_MARGIN + x * (CANVAS_WIDTH - 2*CANVAS_MARGIN)
def canvas_y(y):
    return CANVAS_MARGIN + y * (CANVAS_HEIGHT - 2*CANVAS_MARGIN)

# extract the x-coordinates (or y-coordinates respectively) from a
# list of Point objects
def xs(points):
    return [p.x for p in points]
def ys(points):
    return [p.y for p in points]

# input: a non-empty list of numbers
# output: the mean average of the list
def mean(numbers):
    return sum(numbers) / len(numbers)

# input: list of Point objects
# output: list of the same objects, in clockwise order
def clockwise(points):
    if len(points) <= 2:
        return points
    else:
        center_x = mean(xs(points))
        center_y = mean(ys(points))
        return sorted(points,
                      key=lambda p: math.atan2(p.y - center_y,
                                               p.x - center_x),
                      reverse=True)

# Run one trial of one or both of the algorithms.
#
# 1. Generates an instance of n random points.
# 2. If do_box is True, run the bounding_box algorithm and display its output.
# 3. Likewise if do_hull is True, run the convex_hull algorithm and display
#    its output.
# 4. The run-times of the two algorithms are measured and printed to standard
#    output.

def generate_points(n):
    print('generating n=' + str(n) + ' points...')
    return random_points(n)
   

def time_trial(message, points, func):
    print(message)

    start = time.perf_counter()
    output = func(points)
    end = time.perf_counter()

    print('elapsed time = ' + str(end - start) + ' seconds')

    return output

def setup_canvas(points):
    w = tkinter.Canvas(tkinter.Tk(),
                       width=CANVAS_WIDTH, 
                       height=CANVAS_HEIGHT)
    w.pack()

    for p in points:
        w.create_oval(canvas_x(p.x) - POINT_RADIUS,
                      canvas_y(p.y) - POINT_RADIUS,
                      canvas_x(p.x) + POINT_RADIUS,
                      canvas_y(p.y) + POINT_RADIUS,
                      fill=POINT_COLOR)

    return w

def draw_edge(w, p, q, color):
    w.create_line(canvas_x(p.x), canvas_y(p.y),
                  canvas_x(q.x), canvas_y(q.y),
                  fill=color)

def mst_trial(n):
    points = generate_points(n)
    edges = time_trial('minimum spanning tree...', points, euclidean_mst)

    w = setup_canvas(points)
    for (p, q) in edges:
        draw_edge(w, p, q, MST_EDGE_COLOR)

    tkinter.mainloop()

def tsp_trial(n):
    points = generate_points(n)
    cycle = time_trial('traveling salesperson...', points, euclidean_tsp)

    w = setup_canvas(points)
    for i in range(n):
        p = cycle[i]
        q = cycle[(i + 1) % n]

        draw_edge(w, p, q, TSP_EDGE_COLOR)

        w.create_text(canvas_x(p.x), canvas_y(p.y) - POINT_RADIUS,
                      text=str(i),
                      anchor=tkinter.S)

    tkinter.mainloop()

###############################################################################
# This main() function runs multiple trials of the algorithms to
# gather empirical performance evidence. You should rewrite it to
# gather the evidence you need.
###############################################################################
def main():
    mst_trial(1000)
    #tsp_trial(9)

if __name__ == '__main__':
    main()
