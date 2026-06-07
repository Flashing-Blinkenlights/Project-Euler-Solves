from itertools import combinations

with open("0079_keylog.txt") as f:
    keylog = sorted(list(set(f.read().strip().split('\n'))))

print(keylog)

reference = {str(k): {"pre":set(), "post":set()} for k in range(0, 10)}

for code in keylog:
    for d1, d2 in combinations(code, 2):
        reference[d1]["post"].add(d2)
        reference[d2]["pre"].add(d1)

[print(k, v) for k, v in reference.items()]