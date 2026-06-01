from gmpy2 import is_prime
from time import time

count = 0
result = []


def A272999(time_limit=10):
    """Numbers k such that (11*10^k + 49)/3 is prime.

    runs for time_limit seconds and returns the list of numbers k such that (11*10^k + 49)/3 is prime, as well as how many numbers were checked.
    prints the current count every iteration to show progress, overwriting the previous count to avoid cluttering the output.
    """
    global count, result
    start_time = time()

    k = 0
    n = 20  # k=0 → (11*1 + 49)/3 = 60/3 = 20

    while time_limit < 1 or time() - start_time < time_limit:
        if is_prime(n):
            print(f"Found prime for k={k}")
            result.append(k)

        # recurrence: n_{k+1} = 10*n - 147
        n = 10 * n - 147

        k += 1
        count += 1

        print(f"Checked {count} numbers...", end="\r")

    return result, count


if __name__ == "__main__":
    try:
        time_limit = int(input("Enter time limit in seconds: "))
        A272999(time_limit)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    print(f"Checked {count} numbers, found primes for k values: {result}")
