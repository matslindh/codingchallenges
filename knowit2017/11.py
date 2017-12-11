from math import ceil, sqrt


def prime_table(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False

    for i in range(2, ceil(sqrt(n))):
        for x in range(i*2, n, i):
            primes[x] = False

    return primes


def is_mirp_number(table, n):
    n_rev = int(str(n)[::-1])
    t_l = len(table)
    return n < t_l and n_rev < t_l and table[n] and table[n_rev] and n_rev != n


def test_is_mirp_number():
    table = prime_table(150)
    assert is_mirp_number(table, 13) is True
    assert is_mirp_number(table, 23) is False
    assert is_mirp_number(table, 5) is False
    assert is_mirp_number(table, 101) is False


if __name__ == "__main__":
    table = prime_table(1000)
    c = 0

    for n in range(0, 1000):
        if is_mirp_number(table, n):
            c += 1

    print(c)