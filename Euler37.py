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


def generate_appended_primes(
    n: str, digit_pool: list[str] = POSSIBLE_INTERMEDIATE_DIGITS
):
    candidates: list[str] = []

    for d in POSSIBLE_INTERMEDIATE_DIGITS:
        if is_prime(int(n + d)):
            candidates.append(n + d)
            candidates = candidates + generate_appended_primes(n + d)

    return candidates


truncatable_primes = []

for d1 in POSSIBLE_STARTING_DIGITS:
    for p in generate_appended_primes(d1):
        if p[-1] in POSSIBLE_FINAL_DIGITS:
            for i in range(1, len(p)):
                if not is_prime(int(p[i:])):
                    break
            else:
                truncatable_primes.append(int(p))
                print(p)

print(sum(truncatable_primes))
