from functools import lru_cache
from time import perf_counter

from euler_tools import force_timeout, print_update

timeout = force_timeout()
start_time = perf_counter()

LIMIT = 10_000_000

ends = [0]*89
ends[0] = 1
ends[88] = 89

@lru_cache
def end_of_chain(n:int):
    if len(ends) < n:
        ends.extend([0]*(n-len(ends)))
    if ends[n-1] == 0:
        next_n = 0
        for d in str(n):
            next_n += int(d) ** 2
        ends[n - 1] = end_of_chain(next_n)
    return ends[n - 1]

end_with_1 = 0
end_with_89 = 0

for n in range(1, LIMIT):
    print_update(n)
    end_for_n = end_of_chain(n)
    if end_for_n == 1:
        end_with_1 += 1
    elif end_for_n == 89:
        end_with_89 += 1
    else:
        raise RuntimeError("Found another end! This shouldn't happen...")

print(end_with_89)
print(f"{perf_counter()-start_time:.3f},s")

timeout.cancel()