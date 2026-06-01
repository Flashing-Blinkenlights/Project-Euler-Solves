# observation: there are always n rotations for an n-digit number

from gmpy2 import is_prime

LIMIT = 1000000


def rotations(n):
    str_n = str(n)
    double_str_n = 2 * str_n
    n_len = len(str_n)
    result = set()
    for i in range(len(str_n)):
        result.add(int(double_str_n[i : i + n_len]))
    return result


circular_primes = set()

for n in range(LIMIT):
    if n in circular_primes:
        continue
    rotations_of_n = rotations(n)
    if all(is_prime(r) for r in rotations_of_n):
        circular_primes |= rotations_of_n
        print(f"New circular primes: {rotations_of_n}")
print(len(circular_primes))
