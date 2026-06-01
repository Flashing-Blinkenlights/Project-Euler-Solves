from euler_tools import is_pentagonal

LIMIT = 1000000

pentagonals = []

for n in range(1, LIMIT):
    p1 = n * (3 * n - 1) // 2
    pentagonals.append(p1)
    for p2 in reversed(pentagonals):
        if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
            print(f"{p1}+-{p2}={p1 + p2}, {p1 - p2}")
            exit()
