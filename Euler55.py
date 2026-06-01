from bisect import bisect_left


LIMIT = 10000
DEPTH_LIMIT = 50

non_lychrel = set()
proven_lychrel = set()


def reverse_number(n):
    return int("".join(reversed(str(n))))


def is_palindrome(s):
    return s == s[::-1]


for n in range(LIMIT, 0, -1):
    if n in proven_lychrel or n in non_lychrel:
        continue
    checked_numbers = {
        n,
    }
    current = n
    for _ in range(DEPTH_LIMIT):
        current += reverse_number(current)
        if is_palindrome(str(current)):
            non_lychrel |= checked_numbers
            print(f"Found sequence of non-Lychrels starting with {n}")
            break
        checked_numbers.add(current)
    else:
        proven_lychrel |= checked_numbers
        print(f"Found sequence of Lychrels starting with {n}")

result = sorted(list(proven_lychrel))
result = result[: bisect_left(result, LIMIT)]
print(len(result))
