from collections import defaultdict
from typing import Dict


def update_current_since(current_since, height, idx):
    for h in range(0, height + 1):
        current_since[h] = idx


def visible_tree_count(path):
    lines = open(path).read().splitlines()
    tree_map = []

    for line in lines:
        tree_map.append(list(map(int, line)))

    trees = defaultdict(lambda: defaultdict(dict))
    trees_range = defaultdict(lambda: defaultdict(dict))

    for y in range(1, len(tree_map) - 1):
        current = tree_map[y][0]
        current_since = {}
        update_current_since(current_since, current, 0)

        for x in range(1, len(tree_map[0]) - 1):
            trees[y][x]['left'] = current
            current = max(current, tree_map[y][x])
            trees_range[y][x]['left'] = x - current_since.get(tree_map[y][x], 0)
            update_current_since(current_since, tree_map[y][x], x)

    for y in range(1, len(tree_map) - 1):
        current = tree_map[y][len(tree_map[y]) - 1]
        current_since = {}
        update_current_since(current_since, current, len(tree_map[y]) - 1)

        for x in range(len(tree_map[0]) - 2, 0, -1):
            trees[y][x]['right'] = current
            current = max(current, tree_map[y][x])
            trees_range[y][x]['right'] = abs(x - current_since.get(tree_map[y][x], len(tree_map[y]) - 1))
            update_current_since(current_since, tree_map[y][x], x)

    for x in range(1, len(tree_map[0]) - 1):
        current = tree_map[0][x]
        current_since = {}
        update_current_since(current_since, current, 0)

        for y in range(1, len(tree_map) - 1):
            trees[y][x]['top'] = current
            current = max(current, tree_map[y][x])
            trees_range[y][x]['top'] = abs(y - current_since.get(tree_map[y][x], 0))
            update_current_since(current_since, tree_map[y][x], y)

    for x in range(1, len(tree_map[0]) - 1):
        current = tree_map[len(tree_map) - 1][x]
        current_since = {}
        update_current_since(current_since, current, len(tree_map) - 1)

        for y in range(len(tree_map) - 2, 0, -1):
            trees[y][x]['bottom'] = current
            current = max(current, tree_map[y][x])
            trees_range[y][x]['bottom'] = abs(y - current_since.get(tree_map[y][x], len(tree_map) - 1))
            update_current_since(current_since, tree_map[y][x], y)

    visible = 0

    for y, tree_row in trees.items():
        for x, directions in tree_row.items():
            for val in directions.values():
                if tree_map[y][x] > val:
                    visible += 1
                    break

    best_range = 0

    for y, tree_row in trees_range.items():
        for x, directions in tree_row.items():
            s = 1

            for r in directions.values():
                s *= r

            best_range = max(best_range, s)

    return visible + len(tree_map) * 2 + (len(tree_map[0]) - 2) * 2, best_range


def test_visible_tree_count():
    assert visible_tree_count('input/08.test') == (21, 8)


if __name__ == '__main__':
    print(visible_tree_count('input/08'))
