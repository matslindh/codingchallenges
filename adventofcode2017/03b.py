from itertools import repeat
from math import floor

map = []

s_y = s_x = 1001

for y in range(0, s_y):
    map.append(list(repeat(0, s_x)))

x = y = floor(s_x/2)
map[y][x] = 1
x += 1
dir = 'R'
written = 0

while written <= 289326:
    if dir == 'R':
        if not map[y-1][x]:
            dir = 'U'
        else:
            x += 1    
    
    elif dir == 'U':
        if not map[y][x-1]:
            dir = 'L'
        else:
            y -= 1
    
    elif dir == 'L':
        if not map[y+1][x]:
            dir = 'D'
        else:
            x -= 1
    
    elif dir == 'D':
        if not map[y][x+1]:
            dir = 'R'
        else:
            y += 1

    written = map[y-1][x-1] + map[y-1][x] + map[y-1][x+1] + \
              map[y][x-1] + map[y][x+1] + \
              map[y+1][x-1] + map[y+1][x] + map[y+1][x+1]

    print(dir, x, y, written)

    map[y][x] = written

