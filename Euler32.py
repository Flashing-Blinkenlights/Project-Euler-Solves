# observation: full term must consist of exactly 9 digits

# hypothesis: it must always follow the format _ _ x _ _ _ = _ _ _ _ or _ x _ _ _ _ = _ _ _ _

from itertools import permutations

products = set()

for p in permutations(list(range(1, 10))):
    a = 10 * p[0] + p[1]
    b = 100 * p[2] + 10 * p[3] + p[4]
    c = 1000 * p[5] + 100 * p[6] + 10 * p[7] + p[8]
    if a * b == c:
        products.add(c)
        print(f"{a}*{b}={c}")
    d = p[0]
    e = 1000 * p[1] + b
    if d * e == c:
        products.add(c)
        print(f"{d}*{e}={c}")

print(products, sum(products))
