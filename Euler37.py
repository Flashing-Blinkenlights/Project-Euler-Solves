from gmpy2 import is_prime

LIMIT = 10000

POSSIBLE_STARTING_DIGITS: list[str] = list(map(str, [2, 3, 5, 7]))
POSSIBLE_INTERMEDIATE_DIGITS: list[str] = list(map(str, [1, 3, 7, 9]))
POSSIBLE_FINAL_DIGITS: list[str] = list(map(str, [3, 7]))

# observation: both the first and last digit of the final number must be prime
# observation: all digits between the first and last digit must be "pseudoprime" (neither 0, 5, or even)
# hypothesis: "sandwitched" digits may not be prime
# observation: 2 can only ever be the first digit, as it can only be a prime when a single digit
# hypothesis: build a number on the way up, then test it on the way down again using dfs
# observation: it is stated there are only 11 possible primes, hence we should stop after finding 11 primes
# observation: only 2-digit+ values are valid tructable primes

def generate_appended_primes(n, digit_pool : list[str] = POSSIBLE_INTERMEDIATE_DIGITS):
    candidates: list[str] = []
    
    for d in POSSIBLE_INTERMEDIATE_DIGITS:
        if is_prime(int(n+d)):
            candidates.append(n+d)
            candidates = candidates + generate_appended_primes(n+d)


truncatable_primes = set()


for d1 in POSSIBLE_STARTING_DIGITS:
    

print(sum(truncatable_primes))