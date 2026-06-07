import os
from itertools import product
from math import isqrt, sqrt
from threading import Timer
from time import perf_counter

from sympy import factorint


def force_timeout(seconds=60):

    def action():
        print(f"Timeout reached after {seconds} seconds. Terminating.")
        os._exit(1)

    timer = Timer(seconds, action)
    timer.start()
    return timer


def print_update(value: str, seconds: float = 0.5):
    if int(100000 * perf_counter()) % int(100000 * seconds) == 0:
        print(value, end="\r")


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


def is_coprime(a, b):
    return set(divisors_of(a)) & set(divisors_of(b)) == {
        1,
    }


def coprimes_to(n):
    return [i for i in range(1, n) if gcd(i, n) == 1]



def triangle_number(n: int):
    return n * (n + 1) // 2


def is_square(n):
    r = isqrt(n)
    return r**2 == n


def is_pentagonal(n):
    return bool(get_pentagonal_index(n))


def get_pentagonal_index(n):
    d = 24 * n + 1
    if is_square(d):
        step_1 = sqrt(d) + 1
        if step_1 % 6 == 0:
            return int(step_1 / 6)
    return None
