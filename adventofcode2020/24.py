from operator import add
from collections import deque
from copy import deepcopy

dirs = {
    'e': (1, -1, 0), 
    'se': (1, 0, -1), 
    'sw': (0, 1, -1), 
    'w': (-1, 1, 0),
    'nw': (-1, 0, 1), 
    'ne': (0, -1, 1),
}

tiles_present = [(0, 0, 0)]

def flip_tile(tiles, x, y, z):
    new = init_tile(tiles, x, y, z)
    tiles[x][y][z] = not tiles[x][y][z]
    return new


def init_tile(tiles, x, y, z):
    if x not in tiles:
        tiles[x] = {}

    if y not in tiles[x]:
        tiles[x][y] = {}

    if z not in tiles[x][y]:
        tiles[x][y][z] = True
        tiles_present.append((x, y, z))
        return True

    return False


def get_state(tiles, x, y, z):
    return tiles.get(x, {}).get(y, {}).get(z, True)


def has_tile(tiles, x, y, z):
    return z in tiles.get(x, {}).get(y, {})


def close_counts(tiles, x, y, z):
    black = 0

    for d, change in dirs.items():
        black += not get_state(tiles, x+change[0], y+change[1], z+change[2])

    return black, len(dirs) - black


def evolver(tiles):
    queue = deque(tiles_present)
    do_not_queue_further = {}
    new_tiles = deepcopy(tiles)

    while queue:
        current_coords = queue.popleft()
        (x, y, z) = current_coords

        currently_white = get_state(tiles, *current_coords)
        black, white = close_counts(tiles, *current_coords)

        if currently_white and black == 2:
            new_tiles[x][y][z] = False
        elif not currently_white and (black == 0 or black > 2):
            new_tiles[x][y][z] = True

        for d, change in dirs.items():
            new_coords = (x + change[0], y + change[1], z + change[2])

            if not has_tile(tiles, *new_coords) and current_coords not in do_not_queue_further:
                queue.append(new_coords)
                do_not_queue_further[new_coords] = True
                init_tile(new_tiles, *new_coords)

    return new_tiles


def navigate(instr):
    tiles = {}
    root = [0, 0, 0]

    for ins in instr:
        current = list(root)

        while ins:
            for d, change in dirs.items():
                if ins.startswith(d):
                    current = list(map(add, current, change))
                    ins = ins[len(d):]

        flip_tile(tiles, *current)

    return tiles


def count_tiles(tiles):
    c = 0
    
    for x in tiles.values():
        for y in x.values():
            for z in y.values():
                c += not z

    return c


def navigate_file(f):
    return navigate([x.strip() for x in open(f)])


def flippity_flip(tiles, days=3):
    for day in range(0, days):
        tiles = evolver(tiles)

    return tiles


def test_navigate_file():
    assert 10 == count_tiles(navigate_file('input/24.test'))


def test_flippity_flip():
    tiles = navigate_file('input/24.test')
    assert count_tiles(flippity_flip(tiles, days=1)) == 15
    assert count_tiles(flippity_flip(tiles, days=2)) == 12
    assert count_tiles(flippity_flip(tiles, days=3)) == 25


if __name__ == '__main__':
    source_tiles = navigate_file('input/24')
    print(count_tiles(source_tiles))
    print(count_tiles(flippity_flip(source_tiles, days=100)))
