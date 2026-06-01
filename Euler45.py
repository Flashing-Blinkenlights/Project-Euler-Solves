# for triangles, pentagons, and hexagons
STARTING_VALUES = 285, 165, 143

# observation: hexagonal numbers progress the fastest, this should be used as an iterator.
# observation: every hexagonal number is also a triangle number
# observation: every other triangle number is also a hexagonal number
# observation: hexnumber(n) = trinumber(n*2-1)

# hypothesis: given a hexagonal number, if (24*hexnumber + 1) is a square number, it could be a pentagonal number
#             furthermore, if (sqrt(24*hexnumber + 1) + 1) is divisible by six, then it is confirmed.

from math import isqrt

from euler_tools import get_pentagonal_index

LIMIT = 10e9


def nth_hex_number(n):
    return n * (2 * n - 1)


def tri_index_from_hex_index(n):
    return n * 2 - 1


def is_square(n):
    r = isqrt(n)
    return r**2 == n


hex_n = STARTING_VALUES[2] - 1
hexnumber = nth_hex_number(hex_n)

while hexnumber <= LIMIT:
    hex_n += 1
    hexnumber = nth_hex_number(hex_n)
    print(f"Checking p({hex_n})={hexnumber}", end="\r")
    pent_n = get_pentagonal_index(hexnumber)
    if pent_n is not None:
        print(
            f"Match at {hexnumber}: t({tri_index_from_hex_index(hex_n)})=p({pent_n})=h({hex_n})"
        )
