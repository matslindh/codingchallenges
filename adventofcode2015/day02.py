def area(s):
    dims = tuple(int(num) for num in s.split('x'))
    areas = [
        dims[0] * dims[1],
        dims[0] * dims[2],
        dims[1] * dims[2],
    ]

    return 2 * areas[0] + 2 * areas[1] + 2 * areas[2] + min(areas)


def ribbon(s):
    dims = tuple(int(num) for num in s.split('x'))
    perimeters = [
        2 * (dims[0] + dims[1]),
        2 * (dims[0] + dims[2]),
        2 * (dims[1] + dims[2]),
    ]

    return min(perimeters) + dims[0] * dims[1] *  dims[2]


def test_area():
    assert area('2x3x4') == 58
    assert area('1x1x10') == 43


def test_ribbon():
    assert ribbon("2x3x4") == 34
    assert ribbon("1x1x10") == 14


if __name__ == '__main__':
    print(sum(
        area(line) for line in open("input/02").read().splitlines()
    ))

    print(sum(
        ribbon(line) for line in open("input/02").read().splitlines()
    ))