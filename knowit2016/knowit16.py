from math import ceil, sqrt

x = ceil(sqrt(100000))

def sum_digits(n):
    s = 0

    for d in str(n):
        s += int(d)

    return s

while True:
    n = x*x

    if n > 1e6:
        break

    if sum_digits(n) == 43:
        print(n)

    x += 1
