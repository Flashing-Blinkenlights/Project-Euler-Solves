# What is the largest prime factor of the number 600851475143?

from gmpy2 import is_prime

n = 600851475143

largest_prime_factor = None

# Check for factors starting from 2
for i in range(2, int(n**0.5) + 1):
    while n % i == 0:
        largest_prime_factor = i
        n //= i

if n > 1:
    largest_prime_factor = n

print(largest_prime_factor)
