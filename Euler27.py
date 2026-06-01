# problem: find highest consecutive sequence of primes for f(n), where f(n) = n**2+an+b, where |a|<1000 and |b|<=1000, then return a*b
# observation: range for a is [-999, 999], range for b is [-1000,1000]

from gmpy2 import is_prime

LIMIT_A = 999
LIMIT_B = 1000

max_consecutive_primes = 0
max_a = 0
max_b = 0

a = LIMIT_A
while a >= -LIMIT_A:
    b = LIMIT_B
    while b >= -LIMIT_B:
        if not is_prime(b):
            b -= 1
            continue
        result = 2  # temporary prime
        consecutive_primes = -1  # to offset the temporary prime
        n = 0
        print(f"Checking f(n) for a={a}, b={b}: ", end="")
        while is_prime(result):
            consecutive_primes += 1
            result = n**2 + a * n + b
            n += 1
        print(f"{consecutive_primes} consecutive primes", end="")
        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            max_a, max_b = a, b
            print(" (NEW MAX)")
        else:
            print("", end="\r")
        b -= 1
    a -= 1
print(max_a, max_b, max_a * max_b)
