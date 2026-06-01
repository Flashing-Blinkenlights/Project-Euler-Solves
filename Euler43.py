PRIMES = [2, 3, 5, 7, 11, 13, 17]

from functools import lru_cache
from itertools import permutations
from collections import deque
from time import perf_counter


@lru_cache
def is_divisible_by(n, d):
    return not bool(n % p)


matches = []

start_time = perf_counter()
all_permutations = filter(
    lambda x: int(x[3]) % 2 + int(x[5]) % 5 == 0,  # filter out trivial mismatches
    ["".join(p) for p in permutations("".join(str(d) for d in range(10)))],
)
for n in all_permutations:
    print(n, end="\r")
    for i, p in enumerate(PRIMES):
        if not is_divisible_by(int(n[1 + i : 4 + i]), p):
            break
    else:
        matches += [n]
        print(n, "\t", perf_counter() - start_time, "s")
print(sum(map(int, matches)))
