import re


def parse_coordinate_list(path):
    coordinates = []

    for line in open(path):
        matches = re.findall(r'x=([-0-9]+), y=([-0-9]+)', line)
        coordinates.append(((int(matches[0][0]), int(matches[0][1])), (int(matches[1][0]), int(matches[1][1]))))

    return coordinates


def unavailable_beacon_positions(path, y_to_test):
    coordinates = parse_coordinate_list(path)
    unpossible_locations = set()
    beacons_on_test_line = set()

    for sensor, beacon in coordinates:
        if beacon[1] == y_to_test:
            beacons_on_test_line.add(beacon[0])

        d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        d_sensor_to_test = abs(sensor[1] - y_to_test)

        if d_sensor_to_test > d:
            continue

        available_x = d - d_sensor_to_test
        unpossible_locations.add(sensor[0])

        for x in range(sensor[0] - available_x, sensor[0]):
            unpossible_locations.add(x)

        for x in range(sensor[0] + 1, sensor[0] + available_x + 1):
            unpossible_locations.add(x)

    return len(unpossible_locations - beacons_on_test_line)


def find_beacon_position(path, max_y):
    coordinates = parse_coordinate_list(path)
    rows = []

    for i in range(max_y + 1):
        rows.append([])

    for sensor, beacon in coordinates:
        d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

        for y in range(max(0, sensor[1] - d), min(max_y, sensor[1] + d) + 1):
            y_dist = abs(sensor[1] - y)
            available_x = d - y_dist
            rows[y].append((sensor[0] - available_x, sensor[0] + available_x))

    for y, row in enumerate(rows):
        intervals = sorted(row)

        max_x = intervals[0][0]

        for interval in intervals:
            if max_x < interval[0] - 1:
                return (max_x + 1) * 4_000_000 + y

            max_x = max(max_x, interval[1])

        pass


def test_parse_coordinate_list():
    assert parse_coordinate_list('input/15.test')[0] == ((2, 18), (-2, 15))


def test_unavailable_beacon_positions():
    assert unavailable_beacon_positions('input/15.test', y_to_test=10) == 26


def test_find_beacon_position():
    assert find_beacon_position('input/15.test', max_y=20) == 56000011


if __name__ == '__main__':
    print(unavailable_beacon_positions('input/15', y_to_test=2_000_000))
    print(find_beacon_position('input/15', max_y=4_000_000))


