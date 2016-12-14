data = open("input/dec01").read().split(',')

coords = {'x': 0, 'y': 0}
been_here = {}
dir_lookup = ['north', 'right', 'down', 'left']
dir_idx = 0


def populate(x, y):
    if x in been_here and y in been_here[x]:
        print("We've been here before: " + str(x) + "," + str(y) + " d: " + str(abs(x)+abs(y)))

    if x not in been_here:
        been_here[x] = {y: True}
    else:
        been_here[x][y] = True

populate(0, 0)

for ins in data:
    ins = ins.strip()
    if ins[0] == 'R':
        dir_idx = (dir_idx + 1) % 4
    else:
        dir_idx = (dir_idx - 1) % 4

    d = int(ins[1:])
    y_delta = 0
    x_delta = 0

    # north
    if dir_idx == 0:
        for y in range(1, d+1):
            populate(coords['x'], coords['y'] + y)

        coords['y'] += d
    # north
    elif dir_idx == 1:
        for x in range(1, d + 1):
            populate(coords['x'] + x, coords['y'])

        coords['x'] += d
    # north
    elif dir_idx == 2:
        for y in range(1, d + 1):
            populate(coords['x'], coords['y'] - y)

        coords['y'] -= d
    # north
    elif dir_idx == 3:
        for x in range(1, d + 1):
            populate(coords['x'] - x, coords['y'])

        coords['x'] -= d

    print(coords)

print(abs(coords['x']) + abs(coords['y']))