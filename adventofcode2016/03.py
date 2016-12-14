valid = 0
data = []

for line in open("input/dec03").readlines():
    sides = [int(x) for x in line.strip().split()]
    data.append(sides)

for x in range(0, len(data), 3):
    for y in range(0, 3):
        print(x, y)
        d = sorted([data[x][y], data[x+1][y], data[x+2][y]])
        print(d)

        if (d[0] + d[1]) <= d[2]:
            # invalid
            continue

        valid += 1

print(valid)