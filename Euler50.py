# hypothesis: the largest sequence will likely be an odd length

from gmpy2 import is_prime
from time import perf_counter

LIMIT = 1000000

primes = [n for n in range(LIMIT) if is_prime(n)]
print(len(primes), "primes to be searched")

max_range = 0
max_prime = 0

start_time = perf_counter()
number_of_primes = len(primes)
for r in range(3, number_of_primes, 1):
    lower_bound = number_of_primes // r
    upper_bound = lower_bound + r
    for offset in range(0, -lower_bound - 1, -1):
        current_range = primes[lower_bound + offset : upper_bound + offset]
        if sum(current_range) > primes[-1]:
            continue

        if is_prime(sum(current_range)):
            max_range = r
            max_prime = sum(current_range)
            print(
                f"New chain of {max_range} adds up to {max_prime}\t{perf_counter() - start_time}s"
            )
            break
print(max_prime)
