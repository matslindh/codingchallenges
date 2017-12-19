buffer = {}
low_x = low_y = high_x = high_y = 0
x = y = 0

instructions = open("input/dec19").readlines()

for instr in instructions:
    dist, dir = instr.strip().split(",")
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

    for ix in range(0, dx):
        if y not in buffer:
            buffer[y] = {}
            
        x += 1
        buffer[y][x] = 1

    for iy in range(0, dy):
        if y not in buffer:
            buffer[y] = {}
            
        y += 1
        buffer[y][x] = 1
