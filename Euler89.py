from euler_tools import decimal_to_roman, roman_to_decimal

with open("0089_roman.txt") as f:
    raw_numerals = f.read().strip().split("\n")

optimal_numerals = [""] * len(raw_numerals)

for index, numeral in enumerate(raw_numerals):
    optimal_numerals[index] = decimal_to_roman(roman_to_decimal(numeral))

print(sum(map(lambda x: len(x[0]) - len(x[1]), zip(raw_numerals, optimal_numerals))))
