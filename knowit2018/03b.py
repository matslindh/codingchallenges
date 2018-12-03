import math
from functools import reduce


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


primes = gen_primes(2**10)


def gen_christmas_numbers(limit, factors = 24):
    prime_index = [0] * factors
    christnumbers = {}

    increment = 0
    max_increment = 0

    while increment < 2:
        while True:
            number = 1
            print(prime_index)

            for idx in prime_index:
                number *= primes[idx]

            if number > limit:
                increment += 1
                prime_index[increment] += 1

                for y in range(0, increment):
                    prime_index[y] = prime_index[increment]

                break

            christnumbers[number] = True
            prime_index[increment] += 1

    return christnumbers


def test_christmas_number():
    to_test = [10240000, 32089034, 16777216, 55023912, 25165824, 62914560]
    c = 0

    numbers = gen_christmas_numbers(2**32+1)

    for number in to_test:
        if number in numbers:
            c += 1

    assert c == 3


numbers = gen_christmas_numbers(2**32+1)
print(len(numbers))
