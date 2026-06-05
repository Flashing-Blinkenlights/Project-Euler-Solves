from collections.abc import Generator
from fractions import Fraction
from sympy.functions.combinatorial.numbers import totient
from bisect import bisect_left, bisect_right

LIMIT = 12000
LOWER_FRACTION = Fraction(1, 3)
UPPER_FRACTION = Fraction(1, 2)

# quesiton: how many fractions are there in the limit?
# FALSE hypothesis: there will be 1-UPPER_FRACTION-LOWER_FRACTION * total_fractions fractions INCLUDING duplicates
# observation: there are 1+2+3...n-1 possible fractions, or n(n-1)/2


def limited_farey_sequence(
    n: int, lower_limit: Fraction = Fraction(0), upper_limit: Fraction = Fraction(1)
) -> Generator[Fraction]:
    """
    Print the n'th Farey sequence from lower_limit to upper_limit (both inclusive).

    >>> print(*farey_sequence(5), sep=' ')
    0 1/5 1/4 1/3 2/5 1/2 3/5 2/3 3/4 4/5 1

    SOURCE: Modified from "Farey Sequence - Wikipedia"
    """
    a, b = lower_limit.numerator, lower_limit.denominator
    # determine the next fraction so that a/b and c/d are a pair
    # d must be the largest denominator that has a valid c and fulfils b*c - a*d = 1
    #   c = (a*d + 1)/b
    # valid values for d occur every b integers, but with an offset we need to calculate:
    #   a*d === -1 (mod b)  <=>  d === -a^-1 (mod b)  <=>  pow(-a, -1, b)
    offset = pow(-a, -1, b)
    # applying the offset, we get another offset which we subtract to find the next smaller valid d starting at n
    d = n - ((n - offset) % b)
    c = (a * d + 1) // b

    yield Fraction(a, b)
    while 0 <= c <= n and Fraction(a, b) < upper_limit:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        # debug: print(f"{a}/{b}", end="\r")
        yield Fraction(a, b)


sequence = list(limited_farey_sequence(LIMIT, LOWER_FRACTION, UPPER_FRACTION))[1:-1]
print(sequence)
print(len(sequence))
