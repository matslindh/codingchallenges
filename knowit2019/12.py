from collections import Counter

def get_down_to_6174_mr_president(n):
    if len(Counter(str(n))) == 1:
        return 0

    iters = 0
    
    while n != 6174:
        iters += 1
        
        s = '{:04d}'.format(n)
        n1 = int(''.join(sorted(s)))
        n2 = int(''.join(sorted(s, reverse=True)))
        
        n = abs(n1 - n2)

    return iters


def test_get_down():
    assert 5 == get_down_to_6174_mr_president(1000)


if __name__ == '__main__':
    c = 0
    
    for i in range(1000, 10000):
        c += 1 if get_down_to_6174_mr_president(i) == 7 else 0
         
    print(c)   
