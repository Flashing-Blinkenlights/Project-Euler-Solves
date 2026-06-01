from sympy import factorint
from itertools import product


def all_factors(n):
    factors = factorint(n)  # {prime: exponent}

    # build exponent ranges
    exponents = [[p**e for e in range(exp + 1)] for p, exp in factors.items()]

    # Cartesian product of all combinations
    divisors = []
    for combo in product(*exponents):
        d = 1
        for x in combo:
            d *= x
        divisors.append(d)

    return sorted(divisors)


def triangle_numbers(max_n=None):
    n = 1
    while max_n is None or n <= max_n:
        yield n * (n + 1) // 2
        n += 1


DIVISOR_LIMIT = 500
LIMIT = 1000000

for t in triangle_numbers(LIMIT):
    if len(all_factors(t)) > DIVISOR_LIMIT:
        print(f"Crossed {DIVISOR_LIMIT} divisors with triangle number {t}")
        break
