from gmpy2 import is_prime

n = 884000

sum = 0

first_n_squares = [i**2 for i in range(1, n + 1)]
for s in first_n_squares:
    if s % 2:
        sum += s
print(sum)
