import math

n = 9*9
prime_table = list(range(0, n + 1))
mm = int(math.sqrt(n))

for x in range(3, mm, 2):
    for y in range(x*2, n, x):
        prime_table[y] = 0


def is_prime(n):
    if n % 2 == 0 or n < 2:
        return False

    return bool(prime_table[n])


def sum_digits(n):
    s = 0
    
    while n > 10:
        s += n%10
        n //= 10
        
    s += n
    
    return s


def is_harshad(n):
    d = sum_digits(n)
    if n % d == 0:
        return is_prime(d)
        
    return False
    

def test_is_harshad():
    assert is_harshad(1729)
    assert not is_harshad(1730)


if __name__ == '__main__':
    s = 0
    
    for i in range(1, 98765433):
        if is_harshad(i):
            s += 1

        if i % 1000000 == 0:
            print(i)

    print(s)
