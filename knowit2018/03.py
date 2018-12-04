import math


def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return memodict(f)


def gen_primes(s):
    primes = [True] * s
    primes[0] = False
    primes[1] = False

    for x in range(2, s):
        for y in range(x*2, s, x):
            primes[y] = False

    result = []

    for idx, prime in enumerate(primes):
        if prime:
            result.append(idx)

    return result


primes = gen_primes(int(math.sqrt(2**32)))


@memoize
def factorize(n):
    # print("factorize", n)
    a = n
    factors = []

    if n in primes:
        #print("Is prime")
        return [n]

    for p in primes:
        #print(" is ", n, p)
        if n % p == 0:
            #print("in p", n, p)
            factors.append(p)
            # print("calling ", n // p, factorize(n // p))
            n //= p
            factors += factorize(n)
            #print("got factored", factors, n)
            break

        if len(factors) > 24:
            return factors

        if n == 1:
            break

        if p > math.sqrt(n):
            break

    return factors


def is_christmas_number(n):
    return len(factorize(n)) == 24


def test_gen_primes():
    assert [2, 3, 5, 7] == gen_primes(10)


def test_factorize():
    assert [5] == factorize(5)
    assert [2, 5] == factorize(10)
    assert [5, 5] == factorize(25)


def test_christmas_number():
    to_test = [10240000, 32089034, 16777216, 55023912, 25165824]
    c = 0

    assert is_christmas_number(62914560)

    for t in to_test:
        if is_christmas_number(t):
            c += 1

    assert c == 2


if __name__ == '__main__':
    c = 0

    for x in range(2**24, 2**32 - 2**24):
        if is_christmas_number(x):
            c += 1

    print(c)
