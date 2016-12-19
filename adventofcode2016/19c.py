import math

inp = 3004953
inp = 5

elves = []
next = {}
prev = {}

for i in range(0, inp):
    elves.append(i + 1)
    next[i] = None
    prev[i] = None

src = 0
left = inp


def pick_next(src):
    dst = math.floor(inp / 2 + src) % inp

    return find_pointer(dst)


def remove_entry(idx):
    next[idx] = find_pointer(idx-1)


def find_pointer(idx):
    n = idx
    seq = []

    # resolve this idx
    while next[n]:
        n = next[n]
        seq.append(n)

    # update skips
    for s in seq:
        next[s] = n

    return n


while left > 1:
    # pick elf
    dst = pick_next(src)
    print(next)
    print('dst: ', dst, 'src:', src, ' act: ', elves[src], ' takes from ', elves[dst])

    # remove dst from sequence
    remove_entry(dst)
    left -= 1

    if src + 1 > inp:
        src = 0
    else:
        src += 1

    print(src, dst)
    src = find_pointer(src)
    print(src, dst)

print(next)
