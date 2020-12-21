from bitarray import bitarray
from bitarray.util import ba2int
import pprint
from math import sqrt


def read_tiles(f):
    tiles = {}
    tile_id = None
    tile = []

    for line in [x.strip() for x in open(f)]:
        if not line:
            tiles[tile_id] = tile
            tile = []
            continue

        if line.startswith('Tile '):
            tile_id = int(line[5:-1])
            continue

        tile.append(bitarray([x == '#' for x in line]))

    if tile:
        tiles[tile_id] = tile

    return tiles


def right(tile):
    t = bitarray()

    for row in tile:
        t.append(row[-1])

    return t


def left(tile):
    t = bitarray()

    for row in tile:
        t.append(row[0])

    return t


def top(tile):
    return tile[0]


def bottom(tile):
    return tile[-1]


def flip_y(tile):
    return tile[::-1]


def rotate(tile):
    rotated = []

    for xidx in range(0, len(tile[0])):
        r = bitarray()

        for row in tile:
            r.append(row[xidx])

        rotated.append(r[::-1])

    return rotated


def test_rotate():
    assert rotate([bitarray('010'),
                   bitarray('111'),
                   bitarray('101')]) == [bitarray('110'),
                                         bitarray('011'),
                                         bitarray('110')]

    assert rotate([bitarray('110'),
                   bitarray('011'),
                   bitarray('111')]) == [bitarray('101'),
                                         bitarray('111'),
                                         bitarray('110')]


def test_flip_y():
    assert flip_y([bitarray('010'),
                   bitarray('111'),
                   bitarray('101')]) == [bitarray('101'),
                                         bitarray('111'),
                                         bitarray('010')]


def test_directionality():
    tile = [bitarray('010'),
            bitarray('110'),
            bitarray('101')]

    assert left(tile) == bitarray('011')
    assert bottom(tile) == bitarray('101')
    assert right(tile) == bitarray('001')
    assert top(tile) == bitarray('010')


def populate_definition_struct(tiles_to_parse):
    available = {
        'left': {},
        'right': {},
        'top': {},
        'bottom': {},
    }

    def populate(k, t):
        def s(k_1, k_2, val):
            k_2 = ba2int(k_2)
            if k_2 not in available[k_1]:
                available[k_1][k_2] = []

            available[k_1][k_2].append(val)

        t_def = {
            'id': k,
            'tile': t,
        }

        s('left', left(tile), t_def)
        s('right', right(tile), t_def)
        s('top', top(tile), t_def)
        s('bottom', bottom(tile), t_def)

    for t_id, tile in tiles_to_parse.items():
        mirrored = flip_y(tile)
        populate(t_id, tile)
        populate(t_id, mirrored)

    return available


def layout_tiles(tiles):
    dim = int(sqrt(len(tiles)))
    layout = []

    for y in range(0, dim):
        row = []
        for x in range(0, dim):
            row.append(None)

        layout.append(row)

    data = {
        'used': set(),
        'layout': layout,
    }

    for tile_id, tile in tiles.items():
        attempt_layout(tiles, tile_id, tile, data)

        for _ in range(0, 3):
            tile = rotate(tile)
            attempt_layout(tiles, tile_id, tile, data)

        flip_y(tile)

        attempt_layout(tiles, tile_id, tile, data)

        for _ in range(0, 3):
            tile = rotate(tile)
            attempt_layout(tiles, tile_id, tile, data)


def attempt_layout(tiles, tile_id, tile, data, x=0, y=0):
    data['used'].add(tile_id)
    data['layout'][x][y] = tile

    if x > 0 and y > 0:
        # consider top and left IF SPACE
        # FIXME: We need to determine how to switch x/y to next row before iterating
        pass
    elif y > 0:
        # consider top only
        pass
    else:
        # consider left only
        pass

    data['layout'][x][y] = None
    data['user'].remove(tile_id)



our_tiles = read_tiles('input/20.test')
layout_tiles(our_tiles)
# Spprint.pprint(populate_definition_struct(our_tiles))


