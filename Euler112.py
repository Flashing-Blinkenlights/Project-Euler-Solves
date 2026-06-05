from time import perf_counter

start = perf_counter()

LIMIT = 99

bouncy = 0
current = 100


# @lru_cache
def is_bouncy(n_str: str) -> bool:
    increasing = False
    decreasing = False

    for a, b in zip(n_str, n_str[1:]):
        if a < b:
            increasing = True
        elif a > b:
            decreasing = True

        if increasing and decreasing:
            return True

    return False


while bouncy * 100 != current * LIMIT:
    current += 1
    if is_bouncy(str(current)):
        bouncy += 1

print(f"{current} at {bouncy / current:.0%} in {perf_counter() - start:.3f}s")
