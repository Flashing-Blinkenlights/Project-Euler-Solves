# problem: find the sum of all positive integers which cannot be written as the sum of two abundant numbers
# observation: all integers greater than 28123 can be written as a sum of two abundant numbers. this is the upper limit.
# observation: all integers smaller than 24 cannot be written as the sum of two abundant numbers. therefore, the sum must be at least sum(range(24))

LIMIT = 28123

from itertools import product

from sympy import factorint


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


def is_abundant(n):
    return sum(divisors_of(n, False)) > n


abundant = set()
abundant_sums = set()

for n in range(12, LIMIT + 1):
    if is_abundant(n):
        abundant.add(n)
        for a in abundant:
            abundant_sums.add(n + a)

non_abundant_sums: set[int] = set(range(LIMIT)) - abundant_sums
print(sum(non_abundant_sums))
