def generate_sequence(n):
    l = [0]
    idx = 0
    
    for i in range(1, 2018):
        idx = (idx + n) % len(l) 

        l.insert(idx + 1, i)
        idx += 1
        
    return l[idx + 1], l[1]


def find_second(n, iters):
    i_1 = 0
    idx = 0
    
    for i in range(1, iters+1):
        idx = (idx + n) % i
        
        if idx == 0:
            i_1 = i
        
        idx += 1
            
    return i_1

def test_generate_sequence():
    assert 638 == generate_sequence(3)[0]
    assert generate_sequence(3)[1] == find_second(3, 2017)


if __name__ == "__main__":
    print(generate_sequence(312))
    print(find_second(312, 50000000))
