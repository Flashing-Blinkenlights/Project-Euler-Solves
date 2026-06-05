from fractions import Fraction

ORDER = 1_000_000
NEXT_FRACTION = Fraction(3, 7)


c, d = NEXT_FRACTION.numerator, NEXT_FRACTION.denominator

# determine the previous fraction so that a/b and c/d are a pair
# d must be the largest denominator that has a valid c and fulfils b*c - a*d = 1
#   a = (b*c - 1)/d
# valid values for a occur every c integers, but with an offset we need to calculate:
#   b*c === 1 (mod d)  <=>  b === c^-1 (mod d)  <=>  pow(c, -1, d)
offset = pow(c, -1, d)
# applying the offset, we get another offset which we add to find the next greater valid d starting at n
b = ORDER - ((ORDER - offset) % d)
a = (b * c - 1) // d

print(Fraction(a, b))
