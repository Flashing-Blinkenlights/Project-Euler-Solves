LIMIT = 4000000


# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def fib_upto(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


fibs = {f for f in fib_upto(LIMIT) if f % 2 == 0}
print(sum(fibs))
