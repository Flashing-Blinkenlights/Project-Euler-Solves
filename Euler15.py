# observation: for an n*n grid, it always takes n steps right and n steps down to reach the point
# hypothesis: we must find the number of unique permutations in a binary set
# observation: this works, but is too slow
# observation: the number of paths branches until halfway, after which there is only a limited number of permutations.
# hypothesis: there are 2^n initial branches, each of which requiring a path to return. There are n^2 possible paths to return
# observation: the number of times each path meets a junction on the diagonal of the grid, the distribution is like a pascal's triangle.
# hypothesis: as each path meeting the junction on the diagonal then has the same amount of possibilities, the numbers of the layer can be raised to the power of two, then summed

from math import comb


def pascal_row(n):
    return [comb(n, k) for k in range(n + 1)]


SIDE_LENGTH = 20

print(sum(map(lambda x: x**2, pascal_row(SIDE_LENGTH))))
