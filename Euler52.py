# observation: the double must have the same number of digits to the original
# hypothesis: the largest possible number for n digits is 10^n/2-1
# observation: the same must be said for 3x, 4x, 5x, and 6x
# hypothesis: the largest possible number for n digits is 10^n/6-1


def digits_contained(n):
    return set(str(n))


LIMIT = 1000000
MULTIPLES = 6

for n in range(1, LIMIT):
    for f in range(2, MULTIPLES + 1):
        if digits_contained(n) != digits_contained(n * f):
            break
    else:
        print(n)
        break
