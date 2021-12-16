def lowest_risk_finder_5000(field, multiply_map=False):
    queue = [(0, 0)]
    nodes = {}

    for y, row in enumerate(field):
        for x, risk in enumerate(row):
            nodes[(x, y)] = {
                'risk': int(risk),
                'best': None,
            }

    max_x = len(field[0])
    max_y = len(field)

    if multiply_map:
        max_x *= 5
        max_y *= 5

        for mul in range(1, 5):
            for y in range(len(field)):
                for x in range(len(field[0])):
                    new_risk = nodes[x, y]['risk'] + mul

                    if new_risk > 9:
                        new_risk -= 9

                    nodes[x + len(field[0]) * mul, y] = {
                        'best': None,
                        'risk': new_risk,
                    }

        for mul in range(1, 5):
            for y in range(len(field)):
                for x in range(max_x):
                    new_risk = nodes[x, y]['risk'] + mul

                    if new_risk > 9:
                        new_risk -= 9

                    nodes[x, y + len(field[0]) * mul] = {
                        'best': None,
                        'risk': new_risk,
                    }

    nodes[0, 0]['best'] = 0

    def append_if_valid(current, x_v, y_v):
        next_node = nodes[x_v, y_v]

        if next_node['best'] is None or (current['best'] + next_node['risk']) < next_node['best']:
            next_node['best'] = current['best'] + next_node['risk']
            queue.append((x_v, y_v))

    while queue:
        x, y = queue.pop(0)
        node = nodes[x, y]

        if x > 0:
            append_if_valid(node, x - 1, y)

        if x < max_x - 1:
            append_if_valid(node, x + 1, y)

        if y > 0:
            append_if_valid(node, x, y - 1)

        if y < max_y - 1:
            append_if_valid(node, x, y + 1)

        pass

    return nodes[max_x - 1, max_y - 1]['best']


def test_lowest_risk_finder_5000():
    assert lowest_risk_finder_5000(open('input/15.test').read().splitlines()) == 40
    assert lowest_risk_finder_5000(open('input/15.test').read().splitlines(), multiply_map=True) == 315


if __name__ == '__main__':
    print(lowest_risk_finder_5000(open('input/15').read().splitlines()))
    print(lowest_risk_finder_5000(open('input/15').read().splitlines(), multiply_map=True))
