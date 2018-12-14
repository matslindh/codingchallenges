from collections import Counter

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


primes = gen_primes(2**16)


def seq_it(n, n2, primes_wanted):
    current = [n, n2]
    factor = n2
    prime_count = 0
    ways = Counter()
    prime_sum = n2 if n2 in primes else 0 + n if n in primes else 0

    while prime_count < primes_wanted - 1:
        for i in range(0, len(current) - 1):
            ways.update([factor + current[i]])

        look_up = factor

        while True:
            look_up += 1

            if ways[look_up] == 1:
                current.append(look_up)
                factor = look_up

                if factor in primes:
                    prime_count += 1
                    prime_sum += factor

                break



    return prime_sum


print(seq_it(1, 3, 100))
