from random import choices
from time import perf_counter

from euler_tools import decimal_to_roman, roman_to_decimal

ALLOWED_TIME = 30

VALID_SUCCESSORS = [
    {'I', 'V', 'X', 'L', 'C', 'D', 'M'},
    {'I': {'I', 'V'}}, {'V': {'I'}}]

ROMAN_UNITS = ['M', 'C', 'X', 'I']
ROMAN_FIVES = ['D', 'L', 'V']
ROMAN_NUMERALS = 

VALID_SUCCESSORS = [{k: v} for i, k in enumerate(ROMAN_NUMERALS) for v in ROMAN_NUMERALS[i:]]

VALID_SUCCESSORS = {
    "": set(ROMAN_NUMERALS),
    } # case with no characters: it doesn't matter

VALID_SUCCESSORS.update({})

VALID_PAIRS = [
    "II", "IV", "IX",
    "VI",
    "XI", "XV", "XX", "XL", "XC",
    "LI", "LV", "LX",
    "CI", "CV", "CX", "CL", "CC", "CD", "CM",
    "DI", "DV", "DX", "DL", "DC",
    "MI", "MV", "MX", "ML", "MC", "MD", "MM"
    ]

start_time = perf_counter()

current_numeral = ""
numbers = []

while perf_counter() - start_time < ALLOWED_TIME:

    next_char = choices(["#", "I", "V", "X", "L", "C", "D", "M"], [2]+7*[14])[0]

    # finish this numeral
    if next_char == "#":
        decimal_form = roman_to_decimal(current_numeral)
        ideal_form = decimal_to_roman(decimal_form)
        numbers.append(decimal_form)
        if decimal_to_roman(decimal_form) != current_numeral:
            raise RuntimeError(f"{current_numeral} is not in ideal form ({ideal_form})")

        current_numeral = ""
        continue

    if next_char not in VALID_SUCCESSORS[len(current_numeral)]:
        continue


    # check for invalid next_char
    if len(current_numeral) != 0:
        last_char = current_numeral[-1]
        if last_char+next_char not in VALID_PAIRS:
            continue

    # continue if all is well
    current_numeral += next_char
