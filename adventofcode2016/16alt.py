i = "10011111011011001"
i = [int(x) for x in i]
limit = 272

# b
limit = 35651584


def print_bin(b):
    print(''.join([str(x) for x in b]))


def checksum(l):
    while len(l) % 2 == 0:
        x = []

        for j in range(0, len(l), 2):
            x.append(int(not (l[j] ^ l[j+1])))

        l = x

    return l


def inverted(l):
    return [int(not x) for x in l]


while len(i) < limit:
    print(len(i))
    i = i + [0] + inverted(reversed(i))

# chop and checksum
print_bin(checksum(i[:limit]))