import math

inp = 3004953
inp = 5

elves = []
next = {}

for i in range(0, inp):
    elves.append(i + 1)
    next[i] = None

src = 0
left = inp

def pick_next(src):
    dst = math.floor(left / 2 + src) % left

    return find_pointer(n)


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
    pick_next(src)
    dst = math.floor(len(elves) / 2 + src) % len(elves)

    del(elves[dst])

    if src == len(elves):
        src = 0
    else:
        src = (src + 1) % len(elves)

    if len(elves) % 10000 == 0:
        break

print(elves)
