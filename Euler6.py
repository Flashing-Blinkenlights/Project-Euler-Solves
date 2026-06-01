# Find the difference between the sum of the squares
# of the first one hundred natural numbers
# and the square of the sum.

LIMIT = 100

print(sum(range(1, LIMIT + 1)) ** 2 - sum([n**2 for n in range(1, LIMIT + 1)]))
