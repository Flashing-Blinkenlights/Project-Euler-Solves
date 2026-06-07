# perimeter of the largest possible triangle
from math import isqrt
from euler_tools import is_square

# observation: don't need to calculate the area, only prove that it's integral

LIMIT = 1_000_000_000
OFFSETS = {-1, 1}


def is_isoscelese_with_integral_area(s1: int, s2: int):
    return is_square(4 * s1**2 - s2**2)


total_perimeter = 0

# will stop at perimeter of 3*(LIMIT//3) + 1, may cause off-by-one
for s1 in range(3, LIMIT // 3 + 1, 2):
    # test with smaller third side
    for i in OFFSETS:
        if is_isoscelese_with_integral_area(s1, s1 + i):
            total_perimeter += 3 * s1 + i
            print(f"Matched triangle {s1}-{s1}-{s1 + i}")

print(total_perimeter)
