from gmpy2 import fac

# definition: SoaFiDiFac: sum of all first digit's factorials
#
# observation: no limits are provided: There must be an implicit finite space
# observation: single digits do not result in sums: 10 is the starting point
# observation: each addend must be the factorial of a single digit, resulting in limited options
#
# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# 6! = 720
# 7! = 5040
# 8! = 40320
# 9! = 362880
#
# observation: a match cannot contain a digit, where the factorial of a single digit is larger than the current number
# 10-99: only permissible digits are 0-4: 10-44
# 100-999: only permissible digits are 0-6: 100-666
# 1000-9999: only permissible digits are 0-7: 1000-7777
# 10000-99999: only permissible digits are 0-8: 10000-88888
# 100000+: all digits available
#
# experiment: trial possibilities within two-digit range:
# f(10) != 2
# f(11) != 2
# f(12) != 3
# f(13) != 7
# f(14) != 25  # observation: SoaFiDiFac is running away: solution must include a 4, and must be >= 25
# f(34) != 30
# f(40) = f(41) != 25  # observation: digits are commutable, further limiting space
# f(42) != 28
# f(43) != 30
# f(44) != 48  # hypothesis: good check of maximum range
#
# observation: starting point within range can be severely limit to the first two-digit combination that result in a two-digit SoaFiDiFac
# hypothesis: lowest potential match appears to be 'lowest single-digit factorial + #digits - 1'
# hypothesis: combinations of valid single-digit factorials shall be checked, rather than target numbers
# hypothesis: could have a recursive solution
#
# observation: 0 and 1 are interchangable for the SoaFiDiFac
# observation: smaller solution space when starting off with SoaFiDiFac
# experiment: try using SoaFiDiFac to find matches
# f2(1, 0) = 2 -> under 2-digit
# f2(1, 1) = 2 -> under 2-digit
# f2(1, 2) = 3 -> under 2-digit
# ...
# f2(1, 4) = 25 -> 2-digit, but does not match 14 or 41
# f2(1, 5) = 121 -> over 2-digit, reached digit limit (0-4)
# f2(2, 4) = 28 -> 2-digit, but does not match 24 or 42
# f2(3, 4) = 30 -> 2-digit, but does not match 34 or 43
# f2(4, 4) = 28 -> 2-digit, but does not match 44
# === ALL 2-DIGIT POSSIBILITIES EXHAUSTED ===
# # start with smallest number containing three digits
# f2(1, 0, 5) = 122 -> not 105 or 501
# f2(1, 0, 6) = 722 -> not 106 or 601
# f2(1, 0, 7) = 5042 -> OVERSHOOT
# f2(1, 1, 5) = 122 -> not 115, 151, 511
# f2(1, 1, 6) = 722 -> not 116, 161, 611
# f2(1, 2, 5) =

from itertools import permutations, chain

DIGIT_FACTORIALS = tuple(fac(n) for n in range(10))
POSSIBLE_DIGITS = ((), (0, 1, 2, 3), (4,), (5, 6), (7,), (8,), (9,))


def possible_digits(number_of_target_digits):
    if number_of_target_digits > len(POSSIBLE_DIGITS):
        number_of_target_digits = len(POSSIBLE_DIGITS)
    return chain.from_iterable(POSSIBLE_DIGITS[: number_of_target_digits + 1])


def factorials(iterable):
    return [fac(i) for i in iterable]


def permutated_digits(iterable):
    return list(filter(lambda x: x[0] > 0, permutations(iterable)))


def generate_digit_set(
    number_of_target_digits: int, allow_leading_zeros=False, possible_digit_list=None
):
    if number_of_target_digits == 0:
        yield []
        return
    possible_digit_list = possible_digit_list or list(
        possible_digits(number_of_target_digits)
    )
    for n in possible_digit_list:
        if not allow_leading_zeros and n == 0:
            continue
        for s in generate_digit_set(
            number_of_target_digits - 1,
            allow_leading_zeros=True,
            possible_digit_list=possible_digit_list,
        ):
            yield [n] + s


LIMIT = 6  # digits
ONLY_PRINT_MATCHES = True

matches = []

for n in range(2, LIMIT + 1):
    for s in generate_digit_set(n):
        number = int("".join(map(str, s)))
        fact_sum = sum(factorials(s))
        print(f"Checking {number}: ", end="")
        if number == fact_sum:
            matches.append(number)
            print("MATCHED!")
        elif ONLY_PRINT_MATCHES:
            print("...", end="\r")
        else:
            print(f"no match ({fact_sum})")

print(f"All matches up to {LIMIT} digits:\n\t{matches}")
print(f"Sum of matches: {sum(matches)}")
