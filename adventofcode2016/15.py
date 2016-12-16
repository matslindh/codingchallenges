from math import gcd
s = 1
entries = []

for line in open("input/dec15_b").readlines():
    instr = line.strip().split()
    offset, positions, current = int(instr[1][1:]), int(instr[3]), int(instr[11].strip('.'))

    entries.append({'offset': offset, 'positions': positions, 'current': current})

t = 0
while True:
    found = True
    possible = []

    for e in entries:
        possible.append((e['offset'] + e['current'], e['positions']))
        if (t + e['offset'] + e['current']) % e['positions'] != 0:
            found = False
            break

    if found:
        print("Found one: " + str(t))
        print(possible)
        break

    t += 1