from math import sqrt
from os import close

from gmpy2 import is_prime
import bisect


LIMIT = 1000000

squares_twice = [2]


def not_over(values, target):
    i = bisect.bisect_right(values, target)
    return values[:i]


def squares_twice_not_over(n):
    global squares_twice

    while squares_twice[-1] < n:  # calculate squares_twice
        i = len(squares_twice) + 1
        squares_twice.append(2 * i**2)

    return not_over(squares_twice, n)


for n in range(3, LIMIT, 2):
    if is_prime(n):
        print(f"{n} is prime")
        continue
    for square_twice in squares_twice_not_over(n):
        if is_prime(n - square_twice):
            print(f"{n} = {n - square_twice}+2*{int(sqrt(square_twice / 2))}^2")
            break
    else:
        print(squares_twice, squares_twice_not_over(n))
        print(n)
        break
