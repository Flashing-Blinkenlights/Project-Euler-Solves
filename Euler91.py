# observation: for any box, there are 3 possible triangles
# observation: the triangles with hypothenuse along the axes exist for every value along the length of that axis
from fractions import Fraction
from itertools import product

import numpy as np

from euler_tools import print_update, triangle_number

MAX_GRID_SIZE = 5

def fit_triangles(grid_size:int):
    # all trivial cases
    right_angle_on_axis = grid_size**2 * 3

    right_angle_off_axis = 0

    LOWER_BOUNDS = np.zeros(2)
    UPPER_BOUNDS = np.full(2, grid_size)

    for x, y in product(range(1, grid_size+1), range(1, grid_size+1)):

        q = np.array([x, y])
        reduced_q = Fraction(x, y)
        v0 = np.array([reduced_q.numerator, reduced_q.denominator])

        v1 = np.array([v0[1], -v0[0]])
        k1 = 1
        p1 = q + k1*v1
        while np.all((LOWER_BOUNDS <= p1) & (p1 <= UPPER_BOUNDS)):
            right_angle_off_axis += 1
            k1 += 1
            p1 = q + k1 * v1

        v2 = -v1
        k2 = 1
        p2 = q + k2 * v2
        while np.all((LOWER_BOUNDS <= p2) & (p2 <= UPPER_BOUNDS)):
            right_angle_off_axis += 1
            k2 += 1
            p2 = q + k2 * v2

    total = right_angle_on_axis + right_angle_off_axis

    return total

for n in range(1, MAX_GRID_SIZE+1):
    print(n, "->", fit_triangles(n))

print(50, fit_triangles(50))