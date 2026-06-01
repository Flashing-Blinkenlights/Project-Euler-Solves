from gmpy2 import is_prime
from itertools import permutations, combinations

DIGIT_LIMIT = 4

for n in range(10 ** (DIGIT_LIMIT - 1), 10**DIGIT_LIMIT):
    if not is_prime(n):
        continue
    candidates = list(
        filter(
            lambda x: is_prime(x) and len(str(x)) == DIGIT_LIMIT,  # a valid candidate
            sorted(
                set(int("".join(permutation)) for permutation in permutations(str(n)))
            ),  # all permutations converted into int
        )
    )
    for c in combinations(candidates, 3):
        if c[2] - c[1] == c[1] - c[0]:
            print(c)
            break
