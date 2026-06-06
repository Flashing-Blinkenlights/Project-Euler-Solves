from itertools import product
from math import sqrt

from gmpy2 import gcd
from sympy import factorint
from sympy.external.gmpy import is_square


def divisors_of(n, include_self=True):
    factors = factorint(n)  # {prime: exponent}

    # build exponent ranges
    exponents = [[p**e for e in range(exp + 1)] for p, exp in factors.items()]

    # Cartesian product of all combinations
    divisors = []
    for combo in product(*exponents):
        d = 1
        for x in combo:
            d *= x
        if include_self or d != n:
            divisors.append(d)

    return divisors


def coprimes_to(n):
    return [i for i in range(1, n) if gcd(i, n) == 1]


def get_pentagonal_index(n):
    d = 24 * n + 1
    if is_square(d):
        step_1 = sqrt(d) + 1
        if step_1 % 6 == 0:
            return int(step_1 / 6)
    return None


def is_pentagonal(n):
    return bool(get_pentagonal_index(n))
