import math

inp = 3004953
#inp = 11

data = list(range(1, inp+1))
# data_len = len(data_len)

src = 0

while len(data) > 1:
    dst = (math.floor(len(data) / 2) + src) % len(data)

    #print('len', len(data), 'src', src, 'dst', dst)

    # print(data)
    # print(data[src],
    #      'takes',
    #      data[dst])

    del data[dst]

    if src < dst:
        src += 1

    if src >= len(data):
        src = 0

    if src % 1000 == 0:
        print(len(data))

print(data)