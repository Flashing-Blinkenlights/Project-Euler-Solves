LIMIT = 10000000
POWER = 5

total = 0

for n in range(10, LIMIT):
    digits = list(map(int, str(n)[:]))
    raised_digits = map(lambda x: x**POWER, digits)
    if n == sum(raised_digits):
        total += n
        print(f"Found new match with {n}")
print(total)
