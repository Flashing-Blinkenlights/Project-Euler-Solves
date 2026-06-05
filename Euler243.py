from sympy.functions.combinatorial.numbers import totient
from fractions import Fraction
from gmpy2 import is_prime

LIMIT = int(10e8)
TARGET = Fraction(15499, 94744)#(4, 10)

min_resilience = 1
last_notable_denominator = 0
step = 1
den = 2

print(f"Target: {TARGET} ({TARGET:.2%})")

while den <= LIMIT:

    resilience = Fraction(int(totient(den)), den - 1)

    if resilience < min_resilience:
        step = den-last_notable_denominator
        print(f"+{den-step}")
        print(f"{den}: {resilience} ({resilience:.2%} / {TARGET:.2%})")
        min_resilience = resilience
        last_notable_denominator = den

    if resilience < TARGET:
        print(f"Target met: {resilience} < {TARGET} at a denominator of {den}")
        break
    
    den += step

    