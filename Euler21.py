from euler_tools import divisors_of


def d(n):
    """Sum of all proper divisors of n"""
    return sum(divisors_of(n, include_self=False))


LIMIT = 10000

print(divisors_of(220, include_self=False))
print(sum(divisors_of(220, include_self=False)))
print(divisors_of(284, include_self=False))
print(sum(divisors_of(284, include_self=False)))

amicables = set()

for n in range(2, LIMIT + 1):
    if n not in amicables:
        val = d(n)
        if val != n and d(val) == n:
            amicables |= {
                n,
                val,
            }

print(amicables)
print(sum(amicables))
