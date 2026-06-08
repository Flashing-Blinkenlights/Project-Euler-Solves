from time import perf_counter
import numpy as np

from euler_tools import decimal_to_roman, roman_to_decimal, print_update

# FIXME: Approach is not suited to problem, consider a more theoretical approach...

ALLOWED_TIME = 600
ITERATIONS = 3
DOUBLE_CHECK = False
PRINT_UPDATE = False

ROMAN_NUMERAL_STR = "MDCLXVI#"

ROMAN_UNITS = 0b1010101

# bitmasks for MDCLXVI respectively
ELIMINATES = {
    "M": 0b0000000,
    "D": 0b1100000,
    "C": 0b0000000,
    "L": 0b1111000,
    "X": 0b1100000,
    "V": 0b1111110,
    "I": 0b1111000,
    "CM": 0b1110000,
    "CD": 0b1110000,
    "CC": 0b1100000,
    "XC": 0b1111100,
    "XL": 0b1111100,
    "XX": 0b1111000,
    "IX": 0b1111111,
    "IV": 0b1111111,
    "II": 0b1111110,
}


class RNGenerator:
    def __init__(self, batch_size=1_000_000):
        self.batch_size = batch_size
        self.rng = np.random.default_rng()

        self.lookup = np.array(
            [0 if r < 2 else 1 << ((r - 2) // 14) for r in range(100)],
            dtype=np.uint8,
        )

        self.buffer = np.array([])
        self.index = batch_size
        self._refill()

    def _refill(self):
        r = self.rng.integers(
            0,
            100,
            size=self.batch_size,
            dtype=np.uint8,
        )
        self.buffer = self.lookup[r]
        self.index = 0

    def next(self):
        if self.index >= self.batch_size:
            self._refill()

        value = int(self.buffer[self.index])
        self.index += 1
        return value


def generate_random_roman_number(rngen: RNGenerator):

    def binary_to_numeral(b):
        index = 7 - b.bit_length()
        return ROMAN_NUMERAL_STR[index]

    def valid_repeats(numeral, roman_number):
        return roman_number[-3:] != 3 * numeral

    def append_numeral(str_numeral: str, roman_number: str, pool: int):
        roman_number += str_numeral
        pool &= ~ELIMINATES[str_numeral]
        if roman_number[-2:] in ELIMINATES:
            pool &= ~ELIMINATES[roman_number[-2:]]

        return roman_number, pool

    roman_number = ""
    pool = (1 << 7) - 1

    while pool > 0:
        bin_numeral = rngen.next()

        # equivalent to '#' being drawn
        if bin_numeral == 0:
            break

        # character was not in pool
        if bin_numeral & pool == 0:
            continue

        str_numeral = binary_to_numeral(bin_numeral)

        if bin_numeral & ROMAN_UNITS != 0 and not valid_repeats(
            str_numeral, roman_number
        ):
            pool &= ~bin_numeral
            continue

        # continue if all is well
        roman_number, pool = append_numeral(str_numeral, roman_number, pool)

    return roman_number


def collect_random_roman_numbers():
    start_time = perf_counter()
    rngen = RNGenerator()

    total = 0
    counter = 0

    while perf_counter() - start_time < ALLOWED_TIME:
        if PRINT_UPDATE:
            print_update(str(counter))  # this does not slow down the generator

        roman_number = generate_random_roman_number(rngen)
        decimal_form = roman_to_decimal(roman_number)

        if DOUBLE_CHECK:  # costly check
            ideal_form = decimal_to_roman(decimal_form)
            if ideal_form != roman_number:
                raise RuntimeError(
                    f"{roman_number} is not in ideal form ({ideal_form})"
                )

        total += decimal_form
        counter += 1

    total_time = perf_counter() - start_time

    return total, counter, total_time


averages = []

for i in range(ITERATIONS):
    total, counter, total_time = collect_random_roman_numbers()
    average = total / counter
    print(f"Avg of {counter} samples is {average:.8f} took {total_time:.0f}s")
