def flow_it(source):
    rows = [list(line.strip()) for line in open(source, "r").readlines()]

    for row in rows:
        in_mountain = False
        start_at = None

        for idx, column in enumerate(row):
            if column == '#' and not in_mountain:
                if start_at:
                    for x in range(start_at, idx):
                        row[x] = '~'

                    start_at = None

                in_mountain = True

            if column == ' ' and in_mountain:
                start_at = idx
                in_mountain = False

    watery_depths = 0

    for row in rows:
        watery_depths += row.count('~')

    return watery_depths


def print_map(rows):
    for row in rows:
        print(''.join(row))


def test_flow_it():
    assert 4 == flow_it('input/02.test')


if __name__ == '__main__':
    print(flow_it('input/02'))
