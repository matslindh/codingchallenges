import json
import queue


def navigate_maze_struct(strategy, f='input/MAZE.txt'):
    rooms = json.load(open(f))
    counts = {'L': 0, 'R': 0, 'U': 0, 'D': 0}

    for row in rooms:
        for room in row:
            room['visited'] = False

    que = queue.PriorityQueue()
    que.put((0, rooms[0][0]))

    while not que.empty():
        pri, room = que.get()

        if room['visited']:
            continue

        room['visited'] = True

        if room['y'] == 499 and room['x'] == 499:
            return sum_visited(rooms)

        if room['y'] < 499 and not room['syd'] and not rooms[room['y'] + 1][room['x']]['visited']:
            que.put((strategy.index('D'), counts['D'], rooms[room['y'] + 1][room['x']]), )

        if room['y'] > 0 and not room['nord'] and not rooms[room['y'] - 1][room['x']]['visited']:
            que.put((strategy.index('U'), rooms[room['y'] - 1][room['x']]), )

        if room['x'] < 499 and not room['aust'] and not rooms[room['y']][room['x'] + 1]['visited']:
            que.put((strategy.index('R'), rooms[room['y']][room['x'] + 1]), )

        if room['x'] > 0 and not room['vest'] and not rooms[room['y']][room['x'] - 1]['visited']:
            print((strategy.index('L'), rooms[room['y']][room['x'] - 1]), )
            que.put((strategy.index('L'), rooms[room['y']][room['x'] - 1]), )

    return -1


def sum_visited(rooms):
    visited = 0

    for row in rooms:
        for room in row:
            visited += 1 if room['visited'] else 0

    return visited


print(str(navigate_maze_struct('DRLU')) + " woop")
print(navigate_maze_struct('RDLU'))