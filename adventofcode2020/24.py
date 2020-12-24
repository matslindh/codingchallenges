from operator import add

dirs = {
    'e': (1, -1, 0), 
    'se': (1, 0, -1), 
    'sw': (0, 1, -1), 
    'w': (-1, 1, 0),
    'nw': (-1, 0, 1), 
    'ne': (0, -1, 1),
}


def flip_tile(tiles, x, y, z):
    new = False
    
    if x not in tiles:
        tiles[x] = {}
            
    if y not in tiles[x]:
        tiles[x][y] = {}
            
    if z not in tiles[x][y]:
        new = True
        tiles[x][y][z] = True

    tiles[x][y][z] = not tiles[x][y][z]
    return new


def get_state(tiles, x, y, z):
    return tiles.get(x, {}).get(y, {}).get(z, True)


def close_black_count(tiles, x, y, z):
    c = 0 
    
    for d, change in dirs.items():
        c += not get_state(x+change[0], y+change[1], z+change[2])
    
    return c, len(dirs) - c


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
    

def test_navigate_file():
    assert 10 == count_tiles(navigate_file('input/24.test'))


def flippity_flip(tiles, count):
    pass


if __name__ == '__main__':
    tiles = navigate_file('input/24')
    print(count_tiles(tiles))
