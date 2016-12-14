lines = open("input/dec02").readlines()


def resolve_line(line):
    line = line.strip()
    keys = [[1,2,3], [4,5,6], [7,8,9]]
    x = 1
    y = 1

    for c in line:
        if c == 'U' and y > 0:
            y -= 1
        elif c == 'D' and y < 2:
            y += 1
        elif c == 'R' and x < 2:
            x += 1
        elif c == 'L' and x > 0:
            x -= 1

    return str(keys[y][x])


def resolve_line_2(line):
    line = line.strip()
    keys = [[None, None, 1, None, None], [None, 2, 3, 4, None], [5, 6, 7, 8, 9], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
    x = 2
    y = 2

    for c in line:
        if c == 'U' and y > 0 and keys[y-1][x] is not None:
            y -= 1
        elif c == 'D' and y < 4 and keys[y+1][x] is not None:
            y += 1
        elif c == 'R' and x < 4 and keys[y][x+1] is not None:
            x += 1
        elif c == 'L' and x > 0 and keys[y][x-1] is not None:
            x -= 1

    return str(keys[y][x])

sol = []
sol2 = []

for line in lines:
    sol.append(resolve_line(line))
    sol2.append(resolve_line_2(line))

print('First: ' + ''.join(sol))
print('Second: ' + ''.join(sol2))