wormholes = []

best = 2000000
max_x = 99999
max_y = 99999

for line in open("input/knowit17").readlines():
    line = line.strip().split('-')

    x1, y1 = line[0].split(',')
    x2, y2 = line[1].split(',')

    wormholes.append({
        'x': int(x1), 'y': int(y1),
        'x2': int(x2), 'y2': int(y2),
        'best_here': 2000000,
    })

    wormholes.append({
        'x': int(x2), 'y': int(y2),
        'x2': int(x1), 'y2': int(y1),
        'best_here': 2000000,
    })

queue = [([], wormholes, 0, 0, 0)]

while queue:
    (used, left, d, x, y) = queue.pop(0)

    if d > best:
        continue

    if (d + max_x - x + max_y - y) < best:
        best = d + max_x - x + max_y - y
        print("new best: " + str(best))

    for widx in range(0, len(left)):
        wh = left[widx]
        new_left = []

        if widx > 0:
            new_left += left[:widx]

        if widx < (len(left) - 1):
            new_left += left[widx+1:]

        new_d = d + abs(x - wh['x']) + abs(y - wh['y'])
        new_x, new_y = wh['x2'], wh['y2']

        if new_d < wh['best_here']:
            wh['best_here'] = new_d
        else:
            continue

        queue.append((used + [wh], new_left, new_d, new_x, new_y))

print(best)