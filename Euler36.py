LIMIT = 1000000


def is_double_palindrome(n):
    s = str(n)
    if s == s[::-1] and bin(n)[2:] == bin(n)[2:][::-1]:
        print(f"{n} is a double palindrome ({bin(n)})")
        return True
    return


print(sum(i for i in range(LIMIT) if is_double_palindrome(i)))
