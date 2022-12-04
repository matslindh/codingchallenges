def christmas_that_paper(path):
    lines = open(path).read().splitlines()
    used = 0

    for line in lines[1:]:
        dims = list(map(int, line.split(',')))
        d_x_z = dims[0] + dims[2]
        d_y_z = dims[1] + dims[2]

        if d_y_z <= d_x_z <= 55:
            used += d_y_z
        elif d_x_z <= d_y_z <= 55:
            used += d_x_z
        else:
            used += min(d_x_z, d_y_z) * 2

        print(dims, used)

    return used


def test_christmas_that_paper():
    assert christmas_that_paper('input/03-pakker-test.csv') == 215


if __name__ == '__main__':
    print(christmas_that_paper('input/03-pakker.csv'))