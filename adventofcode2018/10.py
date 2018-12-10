def i_give_it_five_stars(f):
    points = []

    for line in f.readlines():
        parts = line.strip().split('=')
        p_x, p_y, _ = [x.strip('>').strip(',') for x in parts[1][1:].split(' ') if x]
        v_x, v_y = [x.strip('>').strip(',') for x in parts[2][1:].split(' ') if x]

        points.append({
            'x': int(p_x),
            'y': int(p_y),
            'vx': int(v_x),
            'vy': int(v_y),
        })

    prev_m_x = 999999
    i = 0

    while True:
        i += 1
        width = []

        for point in points:
            point['x'] += point['vx']
            point['y'] += point['vy']

            width.append(point['x'])

        m_x = max(width) - min(width)

        if m_x - prev_m_x >= 0:
            for point in points:
                point['x'] -= point['vx']
                point['y'] -= point['vy']

            points = sorted(points, key=lambda point: (point['y'], point['x']))
            prev_y = 0
            prev_x = 0

            for point in points:
                for y in range(prev_y, point['y']):
                    print("")
                    prev_x = 0

                for x in range(prev_x + 1, point['x']):
                    print(' ', end='')

                if point['x'] != prev_x:
                    print('#', end='')

                prev_x = point['x']
                prev_y = point['y']

            return i - 1

        prev_m_x = m_x


def test_i_give_it_five_stars():
    assert i_give_it_five_stars(open('input/10.test')) == 3


if __name__ == '__main__':
    print(i_give_it_five_stars(open('input/10')))
