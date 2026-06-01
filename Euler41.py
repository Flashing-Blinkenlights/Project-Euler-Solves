from itertools import permutations
from gmpy2 import is_prime

digits = "".join(map(str, range(9, 0, -1)))

for r in range(len(digits)):
    current_set = digits[r:]
    for p in map(int, ["".join(p) for p in permutations(current_set)]):
        if is_prime(p):
            print(p)
            exit()
