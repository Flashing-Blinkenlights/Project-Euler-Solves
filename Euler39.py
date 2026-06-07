from math import sqrt
from euler_tools import is_coprime

LOWER_LIMIT = 12
UPPER_LIMIT = 1000

perimeter_scores = (UPPER_LIMIT - LOWER_LIMIT + 1) * [0]


def generate_primitive_triples(
    min_perimeter=12, max_perimeter=120, include_mirrored=False
):

    # largest perimeter is achieved with n=1
    # perimeter = 2m*(1+m)
    min_m = int((-1 + sqrt(1 + 2 * min_perimeter)) / 2)
    max_m = int((-1 + sqrt(1 + 2 * max_perimeter)) / 2)

    primitive_triples = []

    for m in range(min_m, max_m + 1):
        for n in range(m % 2 + 1, m, 2):  # all odd/even numbers up to m
            if not is_coprime(m, n):
                continue

            a, b = sorted([m**2 - n**2, 2 * m * n])
            c = m**2 + n**2

            primitive_triples.append((a, b, c))
            if include_mirrored:
                primitive_triples.append((b, a, c))

    return primitive_triples


def generate_integer_triangles(
    min_perimeter=120,
    max_perimeter=120,
    include_mirrored=False,
    as_dictionary=False,
    counter=None,
):

    if as_dictionary:
        triples = {}
    else:
        triples = []

    for t in generate_primitive_triples(0, max_perimeter, include_mirrored):
        k = 1
        perimeter = 0
        while perimeter < max_perimeter:
            a, b, c = map(lambda x: x * k, t)
            perimeter = a + b + c
            if min_perimeter <= perimeter <= max_perimeter:
                if as_dictionary:
                    if perimeter not in triples.keys():
                        triples[perimeter] = []
                    triples[perimeter].append((a, b, c))
                else:
                    triples.append((a, b, c))
                if counter is not None:
                    counter[perimeter - min_perimeter] += 1
            k += 1

    return triples if as_dictionary else sorted(triples)


triples = generate_integer_triangles(
    min_perimeter=LOWER_LIMIT,
    max_perimeter=UPPER_LIMIT,
    as_dictionary=True,
    counter=perimeter_scores,
)
winner = LOWER_LIMIT + perimeter_scores.index(max(perimeter_scores))

print(
    winner,
    triples[winner],
)
