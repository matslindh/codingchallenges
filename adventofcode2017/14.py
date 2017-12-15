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


def bits_set_in_128(k):
    c = 0
    disk = []

    for i in range(0, 128):
        x = hash_dense(k + "-" + str(i))
        v = int(x, 16)
        cnt = 0
        row = []

        for i in range(127, -1, -1):
            c += 1 if v & 2**i else 0
            cnt += 1
            row.append(v & 2**i > 0)

        disk.append(row)

    return c, disk

def find_region_count(disk):
    idx = 0
    sy = 0

    while True:
        n = find_next_region(disk, sy)

        if n is None:
            break
        
        idx += 1
        queue = [n]
        sy = n[1]

        while queue:
            x, y = queue.pop(0)

            if not disk[y][x] is True:
                continue

            disk[y][x] = idx
    
            if y > 0 and disk[y-1][x] is True:
                queue.append((x, y-1))

            if y < (len(disk) - 1) and disk[y+1][x] is True:
                queue.append((x, y+1))

            if x > 0 and disk[y][x-1] is True:
                queue.append((x-1, y))

            if x < (len(disk[y]) - 1) and disk[y][x+1] is True:
                queue.append((x+1, y))
            
    return idx


def find_next_region(disk, sy):
    for y in range(sy, len(disk)):
        for x in range(0, len(disk[y])):
            if disk[y][x] is True:
                return x, y

    return None

def test_bits_set():
    assert 8108 == bits_set_in_128("flqrgnkx")[0]


def test_find_region_count():
    assert 1242 == find_region_count(bits_set_in_128("flqrgnkx")[1])


def test_hash():
    assert [[2,1,0,3,4], 3, 1] == hash(5, [3, 4, 1, 5], 1)
    assert 12 == hash(5, [3, 4, 1, 5])[0]


def test_hash_dense():
    assert 'a2582a3a0e66e6e86e3812dcb672a272' == hash_dense('')
    assert '33efeb34ea91902bb2f59c9920caa6cd' == hash_dense('AoC 2017')
    assert '3efbe78a8d82f29979031a4aa0b16a9d' == hash_dense('1,2,3')
    assert '63960835bcdc130f0b66d7ff4f6a5a8e' == hash_dense('1,2,4') 

if __name__ == "__main__":
    # print(bits_set_in_128("ffayrhll")[0])
    print(find_region_count(bits_set_in_128("ffayrhll")[1]))
