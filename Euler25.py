from gmpy2 import fib

LIMIT = 1000000
TARGET = 1000

for n in range(LIMIT):
    a = fib(n + 1)
    print(a)
    if len(str(a)) >= TARGET:
        print(f"fib({n + 1}) meets target")
        exit()
