def gen_primes(s):
    primes = [True] * s
    primes[0] = False
    primes[1] = False

    for x in range(2, s):
        for y in range(x*2, s, x):
            primes[y] = False

    return primes


def previous_prime_table(primes):
    lookup = [None]*len(primes)
    previous = 0

    for idx, is_prime in enumerate(primes):
        if is_prime:
            previous = idx

        lookup[idx] = previous

    return lookup


prime_table = gen_primes(5433000)
previous_table = previous_prime_table(prime_table)


def packet_delivered_count(packets_to_be_delivered):
    n = 0
    delivered = 0

    while n < packets_to_be_delivered:
        if '7' in str(n):
            n += previous_table[n] + 1
        else:
            delivered += 1
            n += 1

    return delivered


def test_packet_delivered_count():
    assert packet_delivered_count(10) == 7
    assert packet_delivered_count(20) == 9
    assert packet_delivered_count(10000) == 32


print(packet_delivered_count(5433000))