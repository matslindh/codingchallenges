from itertools import combinations


def expand_universe(lines):
    expanded_vertically = []

    for line in lines:
        expanded_vertically.append(line)

        if '#' not in line:
            expanded_vertically.append(line)

    expanded = [''] * len(expanded_vertically)

    for column in range(len(lines[0])):
        vertical_line = [line[column] for line in expanded_vertically]
        expand_this = '#' not in vertical_line

        for line_no, line in enumerate(expanded_vertically):
            expanded[line_no] += line[column]

            if expand_this:
                expanded[line_no] += line[column]

    return expanded


def expands_in(lines):
    expand_at = {
        'vertical': set(),
        'horizontal': set(),
    }

    for idx, line in enumerate(lines):
        if '#' not in line:
            expand_at['vertical'].add(idx)

    for column in range(len(lines[0])):
        vertical_line = [line[column] for line in lines]

        if '#' not in vertical_line:
            expand_at['horizontal'].add(column)

    return expand_at


def galaxy_coordinates(lines):
    coordinates = []

    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == '#':
                coordinates.append((x, y))

    return coordinates


def find_shortest_path_between_pairwise_galaxies(lines, multiplier=2):
    coordinates = galaxy_coordinates(lines)
    expands_at = expands_in(lines)
    dist = 0

    for galaxy_1, galaxy_2 in combinations(coordinates, r=2):
        min_x, max_x = min(galaxy_1[0], galaxy_2[0]), max(galaxy_1[0], galaxy_2[0])
        min_y, max_y = min(galaxy_1[1], galaxy_2[1]), max(galaxy_1[1], galaxy_2[1])

        for x in range(min_x + 1, max_x + 1):
            if x in expands_at['horizontal']:
                dist += multiplier
            else:
                dist += 1

        for y in range(min_y + 1, max_y + 1):
            if y in expands_at['vertical']:
                dist += multiplier
            else:
                dist += 1

    return dist


def test_expand_universe():
    input_universe = open("input/11.test").read().splitlines()
    assert_universe = open("input/11.test-assert").read().splitlines()

    assert expand_universe(input_universe) == assert_universe


def test_coordinates():
    input_universe = open("input/11.test").read().splitlines()
    expanded_universe = expand_universe(input_universe)

    assert galaxy_coordinates(expanded_universe)[:3] == [
        (4, 0),
        (9, 1),
        (0, 2),
    ]


def test_expands_in():
    input_universe = open("input/11.test").read().splitlines()
    assert expands_in(input_universe) == {
        'horizontal': {2, 5, 8},
        'vertical': {3, 7},
    }


def test_find_shortest_path_between_pairwise_galaxies():
    universe = open("input/11.test").read().splitlines()

    assert find_shortest_path_between_pairwise_galaxies(universe) == 374


def test_find_shortest_path_between_pairwise_galaxies_tenfold():
    universe = open("input/11.test").read().splitlines()

    assert find_shortest_path_between_pairwise_galaxies(universe, multiplier=10) == 1030


def test_find_shortest_path_between_pairwise_galaxies_hundredfold():
    universe = open("input/11.test").read().splitlines()

    assert find_shortest_path_between_pairwise_galaxies(universe, multiplier=100) == 8410


if __name__ == "__main__":
    universe = open("input/11").read().splitlines()
    print(find_shortest_path_between_pairwise_galaxies(universe))
    print(find_shortest_path_between_pairwise_galaxies(universe, multiplier=1000000))