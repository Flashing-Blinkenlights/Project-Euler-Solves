ones = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
teens = (
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
)
tens = (
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
)
powers_of_ten = (None, "ten", "hundred", "thousand")


def written_number(n):
    n_thousands, n_hundreds, n_tens, n_ones = (
        int(n // 1000),
        int(n % 1000 // 100),
        int(n % 100 // 10),
        int(n % 10),
    )
    result = f"{ones[n_thousands]} thousand" if n_thousands else ""
    result += " and " if n_thousands and any((n_hundreds, n_tens, n_ones)) else ""
    result += f"{ones[n_hundreds]} hundred" if n_hundreds else ""
    result += " and " if n_hundreds and any((n_tens, n_ones)) else ""
    if n_tens == 1:
        result += teens[n_ones]
    else:
        result += f"{tens[n_tens]} {ones[n_ones]}"
    return result


def count_letters(s):
    return len(s.replace(" ", "").strip())


LIMIT = 1000

sum = 0

for n in range(1, LIMIT + 1):
    lettered_number = written_number(n)
    letter_count = count_letters(lettered_number)
    sum += letter_count
    print(f"{n}:\t{lettered_number} ({letter_count})")

print(sum)
