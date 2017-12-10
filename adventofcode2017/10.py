from math import ceil

def hash(bs, input, steps=None, rounds=1):
    l = list(range(0, bs))
    pos = 0
    skip = 0
    step = 0

    for round in range(0, rounds):
        for rev in input:
            for i in range(0, ceil(rev/2)):
                start = (pos + i) % bs
                end = ((pos + rev) - i - 1) % bs

                l[start], l[end] = l[end], l[start]

            pos += rev + skip
            skip += 1        
            step += 1
        
            if step == steps:
                return [l, pos, skip]
        
    return l[0] * l[1], l 


def hash_dense(input, size=256):
    input = [ord(chr) for chr in input] + [17, 31, 73, 47, 23]
    _, h = hash(size, input, rounds=64)
    s = ''
    
    for i in range(0, 16):
        s += convert_sequence(h[16*i:(16*i)+16])

    return s
    
def convert_sequence(vals):
    v = vals[0]
        
    for j in range(1, 16):
        v ^= vals[j]

    return ('0' + hex(v)[2:])[-2:]

65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22    
def test_hash():
    assert [[2,1,0,3,4], 3, 1] == hash(5, [3, 4, 1, 5], 1)
    assert 12 == hash(5, [3, 4, 1, 5])[0]


def test_hash_dense():
    assert 'a2582a3a0e66e6e86e3812dcb672a272' == hash_dense('')
    assert '33efeb34ea91902bb2f59c9920caa6cd' == hash_dense('AoC 2017')
    assert '3efbe78a8d82f29979031a4aa0b16a9d' == hash_dense('1,2,3')
    assert '63960835bcdc130f0b66d7ff4f6a5a8e' == hash_dense('1,2,4') 

if __name__ == "__main__":
    print(hash(256, [int(x) for x in open('input/dec10').read().strip().split(',')])[0])
    print(hash_dense(open('input/dec10').read().strip()))
