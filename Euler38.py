from itertools import permutations
from time import perf_counter
from euler_tools import print_update


def is_pandigital(s: str):
    return set(s) == set(NON_ZERO_DIGITS)


NON_ZERO_DIGITS = "".join(list(map(str, range(1, 10))))
POSSIBLE_MULTIPLICANDS = [
    int("".join(p)) for i in range(1, 9) for p in permutations(NON_ZERO_DIGITS, i)
]

max_concat_product = "0"

for multiplicand in range(2, 100000000):
    print_update(str(multiplicand))

    if multiplicand % 10 == 0:
        continue

    concat_product = str(multiplicand)

    for multiplier in range(2, 10):
        concat_product += str(multiplicand * multiplier)

        # this will also trip if the string is longer than 9 digits
        if len(concat_product) > 9:
            # print(concat_product, " using ", multiplicand, " failed.")
            break

        if (
            len(concat_product) == 9
            and is_pandigital(concat_product)
            and concat_product > max_concat_product
        ):
            max_concat_product = concat_product
            print(max_concat_product, " is new max!")
            break
    else:
        raise RuntimeError("Ran out of multipliers, this shouldn't happen...")


print(max_concat_product)
