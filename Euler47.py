from sympy import factorint

LIMIT = 1000000

DISTINCT_FACTORS = 4
TARGET_CONSECUTIVES = DISTINCT_FACTORS

consecutives = 0

for n in range(LIMIT):
    if len(factorint(n)) == DISTINCT_FACTORS:
        consecutives += 1
        if consecutives == TARGET_CONSECUTIVES:
            print(n - consecutives + 1)
            break
    else:
        consecutives = 0
