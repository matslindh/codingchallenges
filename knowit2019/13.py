import json


def navigate_maze_struct(strategy, f='input/MAZE.txt'):
    rooms = json.load(open(f))
    queue = [(0, 0)]

    while queue:
        y, x = queue.pop()
        room = rooms[y][x]

        if 'visited' in room:
            continue

        room['visited'] = True

        if room['y'] == 499 and room['x'] == 499:
            return sum_visited(rooms)

        for d in strategy:
            if d == 'D' and room['y'] < 499 and not room['syd']:
                queue.append((y + 1, x), )
            elif d == 'U' and y > 0 and not room['nord']:
                queue.append((y - 1, x), )
            elif d == 'R' and x < 499 and not room['aust']:
                queue.append((y, x + 1), )
            elif d == 'L' and x > 0 and not room['vest']:
                queue.append((y, x - 1), )

    return None


def sum_visited(rooms):
    return sum([sum(['visited' in room for room in row]) for row in rooms])


print(abs(navigate_maze_struct('ULRD') - navigate_maze_struct('ULDR')))
