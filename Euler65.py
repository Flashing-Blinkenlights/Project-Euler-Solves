from fractions import Fraction


def simple_continued_fraction(nums):
    result = Fraction(nums[0])
    if len(nums) > 1:
        result += Fraction(1, simple_continued_fraction(nums[1:]))
    return result

LIMIT = 100

e_sequence = [2] + [d for k in range(1, LIMIT) for d in [1, 2 * k, 1]][:LIMIT-1]
print(e_sequence)

convergent = simple_continued_fraction(e_sequence)
print(convergent)
print(sum(map(int, str(convergent.numerator))))