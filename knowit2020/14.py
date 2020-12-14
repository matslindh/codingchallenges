def gen_primes(s):
    primes = [True] * s
    primes[0] = False
    primes[1] = False

    for x in range(2, s):
        for y in range(x*2, s, x):
            primes[y] = False

    return primes


print("Primes..")

primes = gen_primes(12000000)
seq = [0, 1]
lookup = {0: True, 1: True}


def mp(n):
    m = seq[n - 2] - n

    if m < 1 or m in lookup:
        m = seq[n - 2] + n

    seq.append(m)
    lookup[m] = True


print("Iterate")

for i in range(2, 1800813):
    mp(i)

print("Count")

prime_count = 0

for val in seq:
    prime_count += primes[val]

print(len(seq), prime_count)