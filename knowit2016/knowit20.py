from collections import Counter

# we've got cycles to spare, lets confirm


def valid(s):
    counter = Counter(s)

    for c in counter:
        if counter[c] != 1:
            return False

    return True

best = None

for x in range(90000, 100000):
    for y in range(80000, 90000):
        if valid(str(x) + str(y)):
            if not best or (x*y) > best:
                print(x, y, x*y)
                best = x * yp