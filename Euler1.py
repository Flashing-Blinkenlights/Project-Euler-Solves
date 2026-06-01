from gmpy2 import is_prime
from math import ceil

limit = 1000
multiples_of = (3, 5)

sequence = {
    i * n
    for n in multiples_of
    for i in range(ceil(limit / min(multiples_of)) + 1)
    if i * n < limit
}
print(sequence)

print(sum(sequence))
