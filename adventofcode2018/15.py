class Player:
    def __init__(self, type_):
        self.hp = 200
        self.type = type_


def combat_simulation(f):
    map = []
    players = []

    for line in f.readlines():
        row = []

        for c in line.strip():
            if c == '#':
                row.append(False)
            elif c == '.':
                row.append(True)
            elif c == 'G':
                p = Player('G')
                row.append(p)
                players.append(p)
            elif c == 'E':
                p = Player('E')
                row.append(p)
                players.append(p)

        map.append(row)

    print_map(map)


def move_to(map, source, type_):
    queue = [source]
    visited = {}

    while queue:
        x, y = queue.pop(0)

        if y not in visited:
            visited[y] = {}

        if x in visited[y]:
            continue

        visited[y][x] = True

        if y > 1:
            val = map[y-1][x]

            if val is True:
                queue.append((x, y - 1))
            elif isinstance(val, Player) and val.type != type_:
                # we have a possible location to consider
                pass

        if y < (len(map) - 1):
            if map[y+1][x] is True:
                queue.append((x, y + 1))

        if x > 1:
            if map[y][x-1] is True:
                queue.append((x - 1, y))

        if x < (len(map[0]) - 1):
            if map[y+1][x] is True:
                queue.append((x + 1, y))



def print_map(map):
    for row in map:
        for cell in row:
            if cell is False:
                print('#', end='')
            elif cell is True:
                print('.', end='')
            elif isinstance(cell, Player):
                print(cell.type, end='')

        print()


def test_combat_simulation():
    assert combat_simulation(open('input/15.demo')) == 27730
    assert combat_simulation(open('input/15.test')) == 27730
    assert combat_simulation(open('input/15-1.test')) == 36334
    assert combat_simulation(open('input/15-2.test')) == 39514
    assert combat_simulation(open('input/15-3.test')) == 27755
    assert combat_simulation(open('input/15-4.test')) == 28944
    assert combat_simulation(open('input/15-5.test')) == 18740
