from collections import deque

def find_matches(n=5, seed_a=65, seed_b=8921, factor_a=16807, factor_b=48271, multiply_a=1, multiply_b=1):
    a = seed_a
    b = seed_b
    p = 2**31 - 1
    c = 0
    i = 0
    consider_a = deque()
    consider_b = deque()

    while i < n:    
        a = (a * factor_a) % p 
        b = (b * factor_b) % p

        if a % multiply_a == 0:
            consider_a.append(a)            
        
        if b % multiply_b == 0:
            consider_b.append(b)

        if consider_a and consider_b:
            c_a = consider_a.popleft()
            c_b = consider_b.popleft()

            if c_a & 65535 == c_b & 65535:
                c += 1

            i += 1

        #if i % 200000 == 0 and i > 0:
        #    print(i)

    return c
    

def test_find_matches():
    assert 1 == find_matches(5)
    assert 0 == find_matches(5, multiply_a=4, multiply_b=8)
    assert 1 == find_matches(2000, multiply_a=4, multiply_b=8)
    assert 588 == find_matches(40000000)
    assert 309 == find_matches(5000000, multiply_a=4, multiply_b=8)


if __name__ == "__main__":
    print(find_matches(40000000, seed_a=618, seed_b=814))
    print(find_matches(5000000, seed_a=618, seed_b=814, multiply_a=4, multiply_b=8))
