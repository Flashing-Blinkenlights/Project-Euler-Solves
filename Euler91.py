# observation: for any box, there are 3 possible triangles
# observation: the triangles with hypothenuse along the axes exist for every value along the length of that axis

# FIXME: Is not good enough, should do vector-based search...

from euler_tools import print_update, triangle_number

MAX_GRID_SIZE = 5

def fit_triangles(grid_size:int):
    # all trivial cases
    right_angle_on_axis = grid_size**2 * 3

    # all triangles along the diagonal line
    right_angle_on_diagonal = (grid_size) ** 2 // 2

    # all triangles with right angles on the internal lattice between axis and diagonal
    n = grid_size - 2
    right_angle_off_diagonal = 2*max(0,
        n * (n + 1) // 2
        if n % 2 == 0
        else (n + 1)**2 // 2 - 1
    )
    total = right_angle_on_axis + right_angle_on_diagonal + right_angle_off_diagonal

    return total

for n in range(1, MAX_GRID_SIZE+1):
    print(n, fit_triangles(n))

print(50, fit_triangles(50))