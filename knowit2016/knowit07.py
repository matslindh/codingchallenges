x, y = 0, 0

for line in open("input/knowit07"):
    _, dist, _, dir = line.strip().split()
    dist = int(dist)

    if dir == 'south':
        y -= dist
    elif dir == 'north':
        y += dist
    elif dir == 'east':
        x += dist
    elif dir == 'west':
        x -= dist
    else:
        print("Invalid dir: " + dir)

print(str(y) + "," + str(x*-1))