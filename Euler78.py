from functools import lru_cache
from time import perf_counter

from sympy import partition

from euler_tools import force_timeout

timeout = force_timeout()
start_time = perf_counter()

LIMIT=1000000
TARGET_MODULUS = 1_000_000

for coins in range(1, LIMIT):
    print(coins, end='\r')
    if partition(coins) % TARGET_MODULUS == 0:
        print(coins)
        break

timeout.cancel()