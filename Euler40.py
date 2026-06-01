num = ""

n = 1
while len(num) < 1000000:
    num += str(n)
    n += 1

product = 1

for i in range(7):
    print(f"{10**i}th number is {num[10**i - 1]}")
    product *= int(num[10**i - 1])

print(product)
