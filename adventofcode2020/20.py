import pprint

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
            tile_id = line[5:-1]
            continue

        tile.append([x == '#' for x in line])

    if tile:
        tiles[tile_id] = tile

    return tiles

pprint.pprint(read_tiles('input/20.test'))
