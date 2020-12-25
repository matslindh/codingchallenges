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

        s('left', left(t), t_def)
        s('right', right(t), t_def)
        s('top', top(t), t_def)
        s('bottom', bottom(t), t_def)

    for t_id, tile in tiles_to_parse.items():
        mirrored = flip_y(tile)
        populate(t_id, tile)

        for _ in range(0, 3):
            tile = rotate(tile)
            populate(t_id, tile)

        populate(t_id, mirrored)

        for _ in range(0, 3):
            mirrored = rotate(mirrored)
            populate(t_id, mirrored)

    return available


def layout_tiles(tiles, definition_struct):
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
        attempt_layout(tiles, tile_id, tile, data, dim, definition_struct)

        for _ in range(0, 3):
            tile = rotate(tile)
            attempt_layout(tiles, tile_id, tile, data, dim, definition_struct)

        tile = flip_y(tile)

        attempt_layout(tiles, tile_id, tile, data, dim, definition_struct)

        for _ in range(0, 3):
            tile = rotate(tile)
            attempt_layout(tiles, tile_id, tile, data, dim, definition_struct)

    return data


def print_id_layout(layout):
    print()

    for row in layout:
        for tile in row:
            print('None' if not tile else tile['id'], end='  ')

        print()

    print()


def print_solution(layout):
    print_id_layout(layout)
    print('Solution: ' + str(layout[0][0]['id'] * layout[-1][0]['id'] * layout[0][-1]['id'] * layout[-1][-1]['id']))
    img = make_image(layout)

    print('Seamonsters')

    img_flipped = flip_y(img)

    for _ in range(0, 4):
        seamonsters, waves = count_seamonsters(img)

        if seamonsters:
            print(waves)
            break

        seamonsters, waves = count_seamonsters(img_flipped)

        if seamonsters:
            print(waves)
            break

        img = rotate(img)
        img_flipped = rotate(img_flipped)
        print("rotate")

    import sys
    sys.exit()


def attempt_layout(tiles, tile_id, tile, data, dim, definition_struct, x=0, y=0):
    data['used'].add(tile_id)
    data['layout'][y][x] = {
        'id': tile_id,
        'tile': tile,
    }

    if x == dim - 1 and y == dim - 1:
        print_solution(data['layout'])

    next_x = x + 1
    next_y = y

    if next_x % dim == 0:
        next_y = y + 1
        next_x = 0

    if next_x > 0 and next_y > 0:
        r = ba2int(right(data['layout'][next_y][next_x-1]['tile']))
        b = ba2int(bottom(data['layout'][next_y-1][next_x]['tile']))

        if r in definition_struct['left'] and b in definition_struct['top']:
            possible = []

            for l_t in definition_struct['left'][r]:
                for t_t in definition_struct['top'][b]:
                    if l_t == t_t:
                        possible.append(l_t)

            for n_tile in possible:
                if n_tile['id'] in data['used']:
                    continue

                attempt_layout(tiles, n_tile['id'], n_tile['tile'], data=data, dim=dim, definition_struct=definition_struct, x=next_x, y=next_y)
    elif next_y > 0:
        r = ba2int(bottom(data['layout'][next_y-1][next_x]['tile']))

        if r in definition_struct['top']:
            for n_tile in definition_struct['top'][r]:
                if n_tile['id'] in data['used']:
                    continue

                attempt_layout(tiles, n_tile['id'], n_tile['tile'], data=data, dim=dim, definition_struct=definition_struct, x=next_x, y=next_y)
    else:
        r = ba2int(right(data['layout'][y][next_x-1]['tile']))

        if r in definition_struct['left']:
            for n_tile in definition_struct['left'][r]:
                if n_tile['id'] in data['used']:
                    continue

                attempt_layout(tiles, n_tile['id'], n_tile['tile'], data=data, dim=dim, definition_struct=definition_struct, x=next_x, y=next_y)

    data['layout'][y][x] = None
    data['used'].remove(tile_id)


def make_image(layout):
    from copy import deepcopy

    result = deepcopy(layout)

    for row in result:
        for tile in row:
            del tile['tile'][0]
            del tile['tile'][-1]

            for t_row in tile['tile']:
                del t_row[0]
                del t_row[-1]

    image = []

    for y in range(0, len(result)):
        for inner_y in range(0, 8):
            row = bitarray()

            for x in range(0, len(result)):
                row.extend(result[y][x]['tile'][inner_y])

            image.append(row)

    return image


def count_seamonsters(image):
    seamonster = [
        bitarray('00000000000000000010'),
        bitarray('10000110000110000111'),
        bitarray('01001001001001001000'),
    ]

    seamonster_row_len = len(seamonster[0])
    seamonsters = 0

    for y in range(0, len(image) - 2):
        for x in range(0, len(image[0]) - seamonster_row_len):
            found = True

            for ridx, r in enumerate(seamonster):
                if r & image[y+ridx][x:x+seamonster_row_len] != r:
                    found = False
                    break

            if found:
                print("found a seamonster at " + str(x) + ', ' + str(y))
                seamonsters += 1

                for ridx, r in enumerate(seamonster):
                    k = r[:]
                    k.invert()
                    image[y + ridx][x:x + seamonster_row_len] &= k

    c = 0

    for row in image:
        c += row.count()

    return seamonsters, c


#our_tiles = read_tiles('input/20.test')
#definition_struct_source = populate_definition_struct(our_tiles)
#print(layout_tiles(our_tiles, definition_struct=definition_struct_source))


our_tiles = read_tiles('input/20')
definition_struct_source = populate_definition_struct(our_tiles)
print(layout_tiles(our_tiles, definition_struct=definition_struct_source))


