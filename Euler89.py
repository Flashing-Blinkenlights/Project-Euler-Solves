ROMAN_DIGITS_TO_DECIMAL = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
DECIMAL_TO_ROMAN_DIGITS = {val: key for key, val in ROMAN_DIGITS_TO_DECIMAL.items()}

roman_numbers = [
    DECIMAL_TO_ROMAN_DIGITS[val] if val in DECIMAL_TO_ROMAN_DIGITS else None
    for val in range(1, 1 + max(DECIMAL_TO_ROMAN_DIGITS.keys()))
]

(((n - 1) % 9) + 1) * 10^((n - 1)//9)

def roman_to_decimal(numeral):
    sequence = [ROMAN_DIGITS_TO_DECIMAL[char] for char in numeral]
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:  # identified a subtractive combination
            sequence[i] *= -1  # according to rules, only e.g. XIX and not XIIIX are permitted
    return sum(sequence)


def decimal_to_roman(n):
    global roman_numbers

    result = ""

    # reduce to value < largest single digit
    max_roman_digit = max(DECIMAL_TO_ROMAN_DIGITS.keys())
    while n > max_roman_digit:
        n -= max_roman_digit
        result += DECIMAL_TO_ROMAN_DIGITS[max_roman_digit]

    if roman_numbers[n] is None:
        for key in sorted(DECIMAL_TO_ROMAN_DIGITS.keys(), reverse=True):
            if 
    else:
        result += roman_numbers[n]
    return result


with open("0089_roman.txt") as f:
    raw_numerals = f.read().strip().split("\n")

optimal_numerals = [""] * len(raw_numerals)

for index, numeral in enumerate(raw_numerals):
    optimal_numerals[index] = decimal_to_roman(roman_to_decimal(numeral))
