from copy import deepcopy
from math import ceil


class Grid:
    def __init__(self, initial_state, cycles=6):
        i_w = len(initial_state) // 2
        s = cycles + (i_w) + 1
        grid = {}
        self.low = -s
        self.hi = s - 1

        for w in range(-s, s):
            if w not in grid:
                grid[w] = {}

            for z in range(-s, s):
                if z not in grid[w]:
                    grid[w][z] = {}

                for y in range(-s, s):
                    if y not in grid[w][z]:
                        grid[w][z][y] = {}

                    for x in range(-s, s):
                        grid[w][z][y][x] = False

        self.grid = grid

        for y in range(-i_w, ceil(len(initial_state) / 2)):
            for x in range(-i_w, ceil(len(initial_state) / 2)):
                self.grid[0][0][y][x] = initial_state[y+i_w][x+i_w]

    def evolve(self):
        new_grid = deepcopy(self.grid)

        for w, timeslice in self.grid.items():
            for z, slice in timeslice.items():
                for y, row in slice.items():
                    for x, val in row.items():
                        count = self.check_neigbours(x, y, z, w)

                        if val:
                            new_grid[w][z][y][x] = 2 <= count <= 3
                        else:
                            new_grid[w][z][y][x] = count == 3

        self.grid = new_grid

    def check_neigbours(self, x, y, z, w):
        valid_count = 0

        for w_d in range(max(w-1, self.low), min(w+2, self.hi)):
            for z_d in range(max(z-1, self.low), min(z+2, self.hi)):
                for y_d in range(max(y-1, self.low), min(y+2, self.hi)):
                    for x_d in range(max(x-1, self.low), min(x+2, self.hi)):
                        if w_d == w and z_d == z and y_d == y and x_d == x:
                            continue

                        valid_count += self.grid[w_d][z_d][y_d][x_d]

                        if valid_count > 3:
                            # anything above three is treated the same way anyway
                            return valid_count

        return valid_count

    def get_active_count(self):
        count = 0

        for w, timeslice in self.grid.items():
            for z, slice in timeslice.items():
                for y, row in slice.items():
                    for x, val in row.items():
                        count += val

        return count

    def print_grid(self):
        for w, timeslice in self.grid.items():
            for z, slice in timeslice.items():
                print('W=' + str(w) + ', Z=' + str(z))

                for y, row in slice.items():
                    for x, val in row.items():
                        print('#' if val else '.', end='')

                    print()

                print()


def test_grid():
    g = Grid(initial_state=[[False, True,   False],
                            [False, False,  True],
                            [True,  True,   True],
                            ])

    assert g.get_active_count() == 5

    #assert g.check_neigbours(z=-2, y=0, x=0) ==

    g.evolve()
    g.print_grid()
    assert g.get_active_count() == 29


if __name__ == '__main__':
    inp = []

    for line in [x.strip() for x in open('input/17').readlines()]:
        l = []

        for c in line:
            if c == '#':
                l.append(True)
            else:
                l.append(False)

        inp.append(l)

    g = Grid(initial_state=inp)

    # 6 cycles
    for x in range(0, 6):
        print("evolve " + str(x))
        g.evolve()

    print(g.get_active_count())