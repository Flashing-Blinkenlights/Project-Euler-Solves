LIMIT = 1000000

max_length = 0
max_n = None
found = {1: 1}

for n in range(LIMIT, 1, -1):
    current = n
    length = 1
    while current not in found:
        # print(f"{current}->", end="")
        if current % 2 == 0:
            current //= 2
        else:
            current = 3 * current + 1
        length += 1
    length += found[current] - 1
    found[n] = length
    # print(f"[{current}]. {length} steps")
    if length > max_length:
        max_length = length
        max_n = n
        print(f"New max length {max_length} for n={n}")

print(found, "\n", max_n, max_length)
