import math
from multiprocessing import Pool

n = 9*9
prime_table = list(range(0, n + 1))
mm = int(math.sqrt(n))

for x in range(3, mm, 2):
    for y in range(x*2, n, x):
        prime_table[y] = 0


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0 or n < 2:
        return False

    return bool(prime_table[n])


def sum_digits(n):
    s = 0
    
    while n > 0:
        s += n % 10
        n //= 10
        
    return s


def is_harshad(n):
    d = sum_digits(n)

    if n % d == 0:
        return is_prime(d)
        
    return False
    

def test_is_harshad():
    assert is_harshad(1729)
    assert not is_harshad(1730)


def is_harshad_range(interval):
    s = 0

    for i in range(interval[0], interval[1]):
        if is_harshad(i):
            s += 1

    return s


if __name__ == '__main__':
    p = Pool(8)
    sums = p.map(is_harshad_range, [
        (1, 12345679),
        (12345679 * 1, 12345679 * 2),
        (12345679 * 2, 12345679 * 3),
        (12345679 * 3, 12345679 * 4),
        (12345679 * 4, 12345679 * 5),
        (12345679 * 5, 12345679 * 6),
        (12345679 * 6, 12345679 * 7),
        (12345679 * 7, 12345679 * 8+1),
    ])
    
    print(sum(sums))
