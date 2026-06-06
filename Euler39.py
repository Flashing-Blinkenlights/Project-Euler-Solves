from math import sqrt

LIMIT = 1000

perimeter_scores = LIMIT*[0]

def generate_primitive_triples(min_perimeter = 12, max_perimeter = 120, include_mirrored=False):

    # perimeter = 2m**2 + 2*m*(m-1)
    min_m = int((sqrt(4 * min_perimeter + 1) + 1) / 4)
    max_m = int((sqrt(4 * max_perimeter + 1) + 1) / 4)

    primitive_triples = []

    for m in range(min_m, max_m+1):
        for n in range(m % 2 + 1, m, 2):  # all odd/even numbers up to m
            a, b = sorted([m**2 - n**2, 2 * m * n])
            c = m**2 + n**2
            print(a+b+c)

            primitive_triples.append((a, b, c))
            if include_mirrored:
                primitive_triples.append((b, a, c))

    return primitive_triples

def generate_integer_triangles(min_perimeter = 120, max_perimeter = 120, include_mirrored=False):

    triples = []
    a, b, c = 0, 0, 0

    for t in generate_primitive_triples(0, max_perimeter, include_mirrored):
        k = 1
        while a+b+c < max_perimeter:

            a, b, c = map(lambda x: x*k, )