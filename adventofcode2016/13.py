from functools import lru_cache

magic = 1362

# test data
# magic = 10
# goal_x = 7
# goal_y = 4

# a
goal_x = 31
goal_y = 39

# b
max_steps = 51

visited = {}


@lru_cache(None)
def is_wall(x, y):
    factor = magic + x * x + 3 * x + 2 * x * y + y + y * y
    bits = 0

    while True:
        bits += factor & 1
        factor >>= 1

        if not factor:
            break

    return bits % 2


def is_visited(x, y):
    return y in visited and x in visited[y]


def visit(x, y):
    if y not in visited:
        visited[y] = {}

    visited[y][x] = True


def cnt():
    c = 0

    for y in visited:
        c += len(visited[y])

    return c


def draw():
    for y in range(0, 7):
        s = ''

        for x in range(0, 10):
            s += '# ' if is_wall(x, y) else '. '

        print(s)


queue = [(1, 1, 0)]

while queue:
    x, y, steps = queue.pop(0)

    if max_steps and steps == max_steps:
        print("We could have visited " + str(cnt()) + " locations before we got here")
        break

    visit(x, y)

    if x == goal_x and y == goal_y:
        print("We did it! We're like .. the best: " + str(steps))
        break

    if not is_wall(x+1, y) and not is_visited(x+1, y):
        queue.append((x+1, y, steps+1))

    if not is_wall(x, y+1) and not is_visited(x, y+1):
        queue.append((x, y+1, steps+1))

    if x > 0 and not is_wall(x-1, y) and not is_visited(x-1, y):
        queue.append((x-1, y, steps+1))

    if y > 0 and not is_wall(x, y-1) and not is_visited(x, y-1):
        queue.append((x, y-1, steps+1))

