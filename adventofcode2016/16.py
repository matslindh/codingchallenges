# goal - solve it using mostly just binary operators
# .. naive. slow for large sets of data. didn't spend much time after confirming that the brute force list version just Works (tm)
from math import floor

# test
i = 0b10000
limit = 20

# a
i = 0b10011111011011001
limit = 272

# b
limit = 35651584


def checksum(cs):
    width = cs.bit_length()

    while width % 2 == 0:
        x = 0

        for j in range(0, cs.bit_length(), 2):
            j_x = floor(j/2)

            # not j xor j+1
            x |= (not ((cs >> j) & 1) ^ ((cs >> j+1) & 1)) << j_x

        # if we have a pair of 0's first
        if width - cs.bit_length() == 2:
            x |= 1 << j_x + 1

        cs = x
        width = floor(width / 2)

    return cs, width

while i.bit_length() < limit:
    x = (i << i.bit_length() + 1)

    for y in range(0, i.bit_length()):
        x |= ((i >> y & 1) ^ 1) << (i.bit_length() - y - 1)

    # print(bin(x), x.bit_length())
    i = x

# chop chop chop
i >>= i.bit_length() - limit
cs = checksum(i)

print('{:0{width}b}'.format(cs[0], width=cs[1]))

#print(bin()

