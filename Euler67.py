# effectively the same problem as Euler67.py, but with a file as input

from collections.abc import Iterable

wall = ""

with open("0067_triangle.txt") as f:
    wall = f.read()

triangle = [list(map(int, row.split(" "))) for row in wall.strip().split("\n")]


def print2d(to_print: Iterable[Iterable]):
    print("[")
    for row in to_print:
        print(" ", row)
    print("]")


def get_next_pair(row, index, triangle):
    return (
        triangle[row + 1][index],
        triangle[row + 1][index + 1],
    )


def get_prev_pair(row, index, triangle):
    return (
        triangle[row - 1][index - 1],
        triangle[row - 1][index],
    )


# DEBUG:    print2d(triangle[:10])

for row in range(-2, -len(triangle) - 1, -1):
    for index in range(len(triangle[row])):
        triangle[row][index] += max(get_next_pair(row, index, triangle))
    triangle[row + 1] = []
    # DEBUG:    print2d(triangle[:10])

print(triangle[0][0])
