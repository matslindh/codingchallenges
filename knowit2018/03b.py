import time
start = time.clock()


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


def prime_index_product(l):
    number = 1

    for idx in l:
        number *= primes[idx]

    return number


def gen_christmas_numbers(limit, factors=24):
    prime_index = [0] * factors
    christnumbers = {}

    while True:
        increment = 0
        number = prime_index_product(prime_index)

        while number > limit:
            increment += 1

            if increment > 14:
                return christnumbers

            prime_index[increment] += 1

            for y in range(0, increment):
                prime_index[y] = prime_index[increment]

            number = prime_index_product(prime_index)

        # print(prime_index)
        christnumbers[number] = True
        prime_index[0] += 1


def test_christmas_number():
    to_test = [10240000, 32089034, 16777216, 55023912, 25165824, 62914560]
    c = 0

    numbers = gen_christmas_numbers(2**32+1)

    for number in to_test:
        if number in numbers:
            c += 1

    assert c == 3


if __name__ == '__main__':
    numbers = gen_christmas_numbers(2**32+1)
    print(len(numbers))

    print("time: " + str(time.clock() - start))


