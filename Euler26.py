# observation: the best numbers will all be coprime to 10

from euler_tools import is_coprime

LIMIT = 1000

max_d = 0
max_cycle_length = 0

for d in range(2, LIMIT):
    print(f"Checking {d}...", end="\r")
    if not is_coprime(10, d):
        continue
    cycle_length = 0
    remainder = 0  # impossible, as they are coprime
    while remainder != 1:
        print(remainder, end=">")
        if remainder == 0:
            remainder = 1  # steped into loop
        remainder = (remainder * 10) % d  # simulate a step in long division
        cycle_length += 1
    print()
    if cycle_length > max_cycle_length:
        max_d = d
        max_cycle_length = cycle_length

print(f"max_d={max_d} with cycle length {max_cycle_length}")
