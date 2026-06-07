ROMAN_DIGITS_TO_DECIMAL = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}

DECIMAL_TO_ROMAN_DIGITS = {val: key for key, val in ROMAN_DIGITS_TO_DECIMAL.items()}

roman_numbers = [
    DECIMAL_TO_ROMAN_DIGITS[val] if val in DECIMAL_TO_ROMAN_DIGITS else None
    for val in range(1, 1 + max(DECIMAL_TO_ROMAN_DIGITS.keys()))
]

def roman_to_decimal(numeral):
    sequence = [ROMAN_DIGITS_TO_DECIMAL[char] for char in numeral]
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i + 1]:  # identified a subtractive combination
            sequence[i] *= -1  # according to rules, only e.g. XIX and not XIIIX are permitted
    return sum(sequence)


def decimal_to_roman(n):
    global roman_numbers

    result = ""

    for value in reversed(DECIMAL_TO_ROMAN_DIGITS.keys()):
        while n >= value:
            n -= value
            result += DECIMAL_TO_ROMAN_DIGITS[value]

    return result


with open("0089_roman.txt") as f:
    raw_numerals = f.read().strip().split("\n")

optimal_numerals = [""] * len(raw_numerals)

for index, numeral in enumerate(raw_numerals):
    optimal_numerals[index] = decimal_to_roman(roman_to_decimal(numeral))

print(sum(map(lambda x: len(x[0]) - len(x[1]), zip(raw_numerals, optimal_numerals))))
