from cachetools import cached
from math import sqrt


# @cached(cache={})
def divisors(n):
    divs = {1, n}
    
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            divs.add(x)
            divs.add(n // x)

    return divs


def test_divisors():
    assert divisors(12) == {1, 2, 3, 4, 6, 12}


if __name__ == '__main__':
    c = 0
    for x in range(2, 1000000):
        divs = divisors(x)
        s = sum(divs)

        if s > 2*x:
            diff = s - 2*x
            f = sqrt(diff)

            if int(f)**2 == diff:
                c += 1
                print(x, c)

    print("---")
    print(c)
