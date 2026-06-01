with open("0022_names.txt") as f:
    names = sorted(f.read().replace('"', "").split(","))

scores = [0] * len(names)

for n in range(len(names)):
    scores[n] = sum([ord(c) - ord("A") + 1 for c in names[n]]) * (n + 1)

print(sum(scores))
