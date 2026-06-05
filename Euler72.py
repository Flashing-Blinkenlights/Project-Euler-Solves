from sympy.functions.combinatorial.numbers import totient

LIMIT = 1_000_000
percentage = LIMIT // 100

sum = 0

for d in range(2, LIMIT + 1):
    sum += int(totient(d))
    if not d % percentage:
        print(f"{d // percentage}%", end="\r")

print(sum)
