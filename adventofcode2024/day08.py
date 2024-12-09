from collections import defaultdict
from itertools import combinations


def find_anti_nodes(path, max_iterations=1):
    mapdata = open(path).read().splitlines()
    nodes = defaultdict(list)
    anti_nodes = set()

    for y, row in enumerate(mapdata):
        for x, c in enumerate(row):
            if c == '.':
                continue

            nodes[c].append((x, y))

            if max_iterations > 1:
                anti_nodes.add((x, y))

    max_y = len(mapdata)
    max_x = len(mapdata[0])

    for ch, coords in nodes.items():
        for c1, c2 in combinations(coords, 2):
            for idx in range(1, max_iterations + 1):
                d_x, d_y = c1[0] - c2[0], c1[1] - c2[1]

                an1 = c1[0] + d_x * idx, c1[1] + d_y * idx
                an2 = c2[0] - d_x * idx, c2[1] - d_y * idx
                both_outside = True

                if 0 <= an1[0] < max_x and 0 <= an1[1] < max_y:
                    both_outside = False
                    anti_nodes.add(an1)

                if 0 <= an2[0] < max_x and 0 <= an2[1] < max_y:
                    both_outside = False
                    anti_nodes.add(an2)

                if both_outside:
                    break

    return len(anti_nodes)


def test_find_anti_nodes():
    assert find_anti_nodes("input/08.test") == 14


def test_find_anti_nodes_max_iterations():
    assert find_anti_nodes("input/08.test", max_iterations=200) == 34


if __name__ == '__main__':
    print(find_anti_nodes("input/08"))
    print(find_anti_nodes("input/08", max_iterations=200))
