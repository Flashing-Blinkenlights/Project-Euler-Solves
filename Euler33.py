# observation: we are reducing fractions to single-digit numerators and denominators
# observation: all fractions must be less than one in value, the numerator must always be smaller than the denominator
# observation: the digit 0 shall never occur
# observation: there are four possible cases:
#   nx/mx = n/m, where x is any non-0 digit
#   nx/xm = n/m, where x is any digit smaller or equal to m
#   xn/xm = n/m, where x is any non-0 digit
#   xn/mx = n/m, where x is any non-0 digit

# 1/2
# 1/3, 2/3
# 1/4, 2/4, 3/4
# etc.

NON_ZERO_DIGITS = list(map(str, range(1,10)))

def generate_proper_fractions(values = NON_ZERO_DIGITS):
    values = sorted(values)
    
    for i, d1 in enumerate(values, 1):
        for d2 in values[:i-1]:
            yield (d2, d1)

digit_cancelling_fractions = []

for num, den in generate_proper_fractions():

    target = int(num)/int(den)

    for d in NON_ZERO_DIGITS:
        # case 1
        if int(num+d) / int(den+d) == target:
            digit_cancelling_fractions.append((num+d, den+d))
        if int(num+d) / int(d+den) == target:
            digit_cancelling_fractions.append((num+d, d+den))
        if int(d+num) / int(d+den) == target:
            digit_cancelling_fractions.append((d+num, d+den))
        if int(d+num) / int(den+d) == target:
            digit_cancelling_fractions.append((d+num, den+d))

print(digit_cancelling_fractions)