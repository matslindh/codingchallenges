def grid_cabler(path1, path2, print_it=False):
    grid = {}
    intersections = []

    populate_grid_from_path(1, grid, path1, intersections)
    populate_grid_from_path(2, grid, path2, intersections)

    if print_it:
        print_grid(grid, 500)

    d = 99999999999999
    print(intersections)

    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])

        if dist < d:
            d = dist

    return d


def populate_grid_from_path(idx, grid, path, intersections):
    instructions = path.split(',')
    x, y = 0, 0

    for inst in instructions:
        delta_x, delta_y = 0, 0

        if inst[0] == 'R':
            delta_x = 1
        if inst[0] == 'L':
            delta_x = -1
        if inst[0] == 'U':
            delta_y = 1
        if inst[0] == 'D':
            delta_y = -1

        for i in range(0, int(inst[1:])):
            x += delta_x
            y += delta_y

            if y not in grid:
                grid[y] = {}

            if x not in grid[y]:
                grid[y][x] = 0

            if grid[y][x] > 0 and grid[y][x] != idx:
                intersections.append((x, y))

            grid[y][x] = idx


def print_grid(grid, dim):
    dim_2 = int(dim/2)
    for y in range(-dim_2, dim_2):
        row = ''

        for x in range(-dim_2, dim_2):
            if y in grid and x in grid[y]:
                row += str(grid[y][x])
            else:
                row += '.'

        print(row)


def test_grid_cabler():
    assert 6 == grid_cabler('R8,U5,L5,D3', 'U7,R6,D4,L4')
    assert 135 == grid_cabler('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')
    assert 159 == grid_cabler('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83', print_it=True)


if __name__ == '__main__':
    lines = open('input/03').readlines()
    print(grid_cabler(lines[0].strip(), lines[1].strip()))