from math import sqrt

# a^2+b^2=c^2
# a+b+c=1000
# a+b+c-1000=a^2+b^2-c^2
# 1000=a^2-a+b^2-b+b^2-c-c^2
# 1<=a<
# 2<=b<c<997
# 3<=c<997

# Extreme cases:
# a=1, b=2, c=997
# a=1, b=499, c=500
# a=332, b=333, c=335
# a=332, b=333, c=335

# c=1000-a-b, c>335
# c=sqrt(a^2+b^2)
#

LIMIT = 1000

b_max = 1000  # LIMIT // 3

for b in range(b_max, 3, -1):
    for a in range(1, b):
        c = 1000 - a - b
        if not a < b < c:
            continue
        print(
            f"Checking {a}, {b}, {c}; sum={sum((a, b, c))}, pythagorean={a**2 + b**2 == c**2}"
        )
        if a**2 + b**2 == c**2:
            print(a, b, 1000 - a - b, "---", a * b * c)
            exit()
