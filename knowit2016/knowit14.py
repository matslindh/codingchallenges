from math import factorial

best = None
limit = 2.25e32

fac = {}
vals = {}
initial = []

for x in range(1, 17):
    fac[x] = factorial(x)
    vals[x] = x ** x
    initial.append(x)

queue = [(initial, [], 0, 1)]
seen = {}


def checksum(l):
    return str(sorted(l))


while queue:
    (left, used, score, defense) = queue.pop(0)

    if defense > limit:
        if not best or score < best:
            print('new best score: ' + str(score))
            print(used)
            best = score

        continue

    cs = checksum(left)

    if cs in seen:
        continue

    seen[cs] = True

    for x in range(0, len(left)):
        for y in range(x+1, len(left)):
            u = used[:]
            l = left[:]

            v2 = l.pop(y)
            v1 = l.pop(x)

            new_score = score + fac[v1] + fac[v2]
            new_defense = defense * vals[v1] * vals[v2]

            u.append(v1)
            u.append(v2)

            queue.append((l, u, new_score, new_defense))

