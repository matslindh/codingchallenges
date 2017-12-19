buffer = {}
low_x = low_y = high_x = high_y = 0
x = y = 0

instructions = open("input/dec19").readlines()

for instr in instructions:
    dist, dir = instr.strip().split(", ")
    dx = 0
    dy = 0
    
    if dir == 'east':
        dx = int(dist)

    if dir == 'west':
        dx = -int(dist)

    if dir == 'south':
        dy = -int(dist)

    if dir == 'north':
        dy = int(dist)

    for ix in range(0, abs(dx)):
        if y not in buffer:
            buffer[y] = {}
            
        x += 1 if dx > 0 else -1
        buffer[y][x] = 1

    for iy in range(0, abs(dy)):
        y += 1 if dy > 0 else -1

        if y not in buffer:
            buffer[y] = {}
            
        buffer[y][x] = 1

    if y < low_y:
        low_y = y

    if y > high_y:
        high_y = y

    if x < low_x:
        low_x = x

    if x > high_x:
        high_x = x


for y in range(low_y, high_y + 1):
    if y not in buffer:
        print('')
        continue

    for x in range(low_x, high_x + 1):
        print('x' if x in buffer[y] else ' ', end='')

    print('')