from gmpy2 import next_prime

primes = set()
last_prime = 2
LIMIT = 2000000

while last_prime < LIMIT:
    primes.add(last_prime)
    last_prime = next_prime(last_prime)

print(sum(primes))
