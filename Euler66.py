# x**2 - D*y**2 = 1
# x = sqrt(1 + D*y**2)

from math import isqrt

from euler_tools import force_timeout, is_square, print_update

timeout = force_timeout()

LIMIT = 1000

def find_x(d:int):

    x = 0
    y = 0

    while x**2 - d * y**2 != 1:
        print_update(f"{x}**2\t- {d}\t* {y}**2\t!= 1")
        y += 1
        x = isqrt(1 + d * y**2)

    print(f"{x}**2\t- {d}\t* {y}**2\t== 1")

    return x

def pell_equation(D):
    """Uses continued fractions of sqrt(D) to find x and y.

    Taken from https://www.numberanalytics.com/blog/pell-equation-algorithmic-number-theory
    """
    a0 = int(D**0.5)
    if a0 * a0 == D:
        return None
    m = 0
    d = 1
    a = a0
    x_prev = 1
    x = a
    y_prev = 0
    y = 1
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        p_next = a * x + x_prev
        q_next = a * y + y_prev
        x_prev = x
        x = p_next
        y_prev = y
        y = q_next
        if x * x - D * y * y == 1:
            return (x, y)

max_x = 0
best_d = 0

for d in range(1, LIMIT+1):
    if is_square(d):
        continue

    x, _ = pell_equation(d)
    if x > max_x:
        max_x = x
        best_d = d
        print(f"New max x={x} for D={d}")


print(max_x, best_d)

timeout.cancel()