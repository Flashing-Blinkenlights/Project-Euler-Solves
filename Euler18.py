# observation: for every diamond, there is always an optimal path.
# problem: how can these diamonds be overlapped?
#     a
#    b c
#   d e f
#  g h i j
# contains the diamonds a-b|c-e, b-d|e-h, c-e|f-i
# observation: the closer to the center a node is, the more likely it is to be included in the result
# observation: leading to the last row are several half-diamonds. There is always a clear winner in this case for each element

# hypothesis: graph theory may be the way to go. We could rebuild the graph first, then prune it
# hypothesis: put this one step further -> collapse each row from the bottom up, leaving only the greatest sum

from collections.abc import Iterable


triangle = [
    list(map(int, row.split(" ")))
    for row in """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".strip().split("\n")
]


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


print2d(triangle)

for row in range(-2, -len(triangle) - 1, -1):
    for index in range(len(triangle[row])):
        triangle[row][index] += max(get_next_pair(row, index, triangle))
    triangle[row + 1] = []
    print2d(triangle)
