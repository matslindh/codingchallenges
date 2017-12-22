from math import floor

def explore_virus(iterations, start, extended=False):
    start = [x.strip() for x in start]

    directions = {
        'u': {
            'r': 'r',
            'l': 'l',
            'reverse': 'd',
        },
        'd': {
            'r': 'l',
            'l': 'r',
            'reverse': 'u',
        },
        'l': {
            'r': 'u',
            'l': 'd',
            'reverse': 'r',
        },
        'r': {
            'r': 'd',
            'l': 'u',        
            'reverse': 'l',
        },
    }
    
    infections = 0
    lowest = 0
    highest = 0

    x = len(start[0]) // 2
    y = len(start) // 2
    dir = 'u'

    map = {}
    
    for ys in range(0, len(start)):
        if not ys in map:
            map[ys] = {}

        for xs in range(0, len(start[y])):
            map[ys][xs] = start[ys][xs]
 
    for i in range(0, iterations):
        # print_map(map, x, y)
    
        state = "not"

        if y not in map:
            map[y] = {}
            
        if x not in map[y]:
            map[y][x] = '.'
            
        if map[y][x] == '#':
            state = 'inf'

        if map[y][x] == 'W':
            state = 'weak'

        if map[y][x] == 'F':
            state = 'flagged'

        if state == 'not':
            dir = directions[dir]['l']
            map[y][x] = 'W' if extended else '#'
        elif state == 'weak':
            map[y][x] = '#'
        elif state == 'inf':
            dir = directions[dir]['r']
            map[y][x] = 'F' if extended else '.'
        elif state == 'flagged':
            dir = directions[dir]['reverse']
            map[y][x] = '.'

        if map[y][x] == '#':
            infections += 1

        if dir == 'u':
            y -= 1
        elif dir == 'd':
            y += 1
        elif dir == 'r':
            x += 1
        elif dir == 'l':
            x -= 1

    return infections


def print_map(map, pos_x, pos_y):
    keys = map.keys()
    
    lowest_y = min(keys)
    highest_y = max(keys)
    
    for y in range(lowest_y, highest_y + 1):
        if y not in map:
            print("")
            continue

        keysx = map[y].keys()
        
        lowest_x = min(keysx)
        highest_x = max(keysx)

        for x in range(lowest_x, highest_x + 1):
            if x not in map[y]:
                print(" ", end='')
                continue

            if pos_x == x and pos_y == y:
                print("O", end='')
            else:
                print(map[y][x], end='')

        print("")

    print("")


def test_explore_virus():
    assert 5 == explore_virus(7, open("input/dec22_test").readlines())
    assert 41 == explore_virus(70, open("input/dec22_test").readlines())
    assert 5587 == explore_virus(10000, open("input/dec22_test").readlines())


def test_explore_virus_extended():
    assert 26 == explore_virus(100, open("input/dec22_test").readlines(), extended=True)
    assert 2511944 == explore_virus(10000000, open("input/dec22_test").readlines(), extended=True)


if __name__ == "__main__":
    print(explore_virus(10000, open("input/dec22").readlines()))
    # 5576716 too high
    print(explore_virus(10000000, open("input/dec22").readlines()))
