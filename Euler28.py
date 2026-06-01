"""
1 1x1 1
2 3x3 +3+5+7+9 = +24 = +4*2*(4)
3 5x5 +13+17+21+25 = +76 = +4*3
4 7x7 ...
...

"""

TARGET_SIDE_LENGTH = 1001
shells = TARGET_SIDE_LENGTH // 2 + 1

sum = 1
current = 1

for n in range(shells - 1):
    for _ in range(4):
        # print(current, end="->")
        current += 2 * (n + 1)
        sum += current
# print(current)
print(sum)
