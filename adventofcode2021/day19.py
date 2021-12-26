from typing import List, Tuple
from functools import lru_cache
import time
from itertools import combinations


def parse_lines(lines):
    sensors = []
    points = []

    for line in lines:
        if not line:
            sensors.append(points)
            points = []
            continue

        if line.startswith('---'):
            continue

        points.append(tuple(map(int, line.split(','))))

    if points:
        sensors.append(points)

    return sensors


def generate_rotated_sensors(sensors) -> Tuple[Tuple[Tuple[Tuple[int, int, int]]]]:
    generated_sensors = []

    for sensor in sensors:
        sensor_versions = [tuple(sensor)]
        current_sensor = sensor

        for _ in range(3):
            new_sensor = []

            for point in current_sensor:
                new_sensor.append(rotate_y(point))

            sensor_versions.append(tuple(new_sensor))
            current_sensor = new_sensor

        new_sensor = []

        for point in sensor:
            new_sensor.append(rotate_z(point))

        sensor_versions.append(tuple(new_sensor))

        new_sensor = []

        for point in sensor:
            new_sensor.append(rotate_z(rotate_z(rotate_z(point))))

        sensor_versions.append(tuple(new_sensor))

        for sensor_to_rotate in list(sensor_versions):
            current_sensor = sensor_to_rotate

            for _ in range(3):
                new_sensor = []

                for point in current_sensor:
                    new_sensor.append(rotate_x(point))

                sensor_versions.append(tuple(new_sensor))
                current_sensor = new_sensor

        generated_sensors.append(tuple(sensor_versions))

    return generated_sensors


# under 479
# [414, 427>

def count_beacons(lines):
    sensors = parse_lines(lines)
    complete_sensor_set = generate_rotated_sensors(sensors[1:])
    current_map = tuple(sensors[0])
    positions = []

    while complete_sensor_set:
        start = time.time()
        mapped = []

        for idx, sensor_set in enumerate(complete_sensor_set):
            has_overlap = sensor_set_overlaps(current_map, sensor_set)

            if has_overlap:
                overlap_idx, other_sensor_diff = has_overlap
                merged_map = set(current_map)
                positions.append(other_sensor_diff)

                for point in sensor_set[overlap_idx]:
                    merged_map.add((point[0] - other_sensor_diff[0], point[1] - other_sensor_diff[1], point[2] - other_sensor_diff[2]))

                current_map = tuple(merged_map)
                mapped.append(idx)
                print(f"Sensor {idx} overlaps current_map")

        for idx in sorted(mapped, reverse=True):
            print(" ! Found in iteration")
            del complete_sensor_set[idx]

        print(f"Iteration done, {time.time() - start}s, {len(complete_sensor_set)} sensors left, {len(current_map)} beacon count")

    longest_distance = max([
        abs(sensor1[0] - sensor2[0]) + abs(sensor1[1] - sensor2[1]) + abs(sensor1[2] - sensor2[2]) for sensor1, sensor2 in combinations(positions, 2)
    ])

    return len(current_map), longest_distance


@lru_cache(2048)
def sensor_set_overlaps(current_map, other_sensor_set):
    for other_idx, other_sensor in enumerate(other_sensor_set):
        idx_overlaps = overlaps(current_map, other_sensor)

        if idx_overlaps is not None:
            idx_i, idx_o = list(idx_overlaps.items())[0]
            diff_to_other_sensor = other_sensor[idx_o][0] - current_map[idx_i][0], other_sensor[idx_o][1] - current_map[idx_i][1], other_sensor[idx_o][2] - current_map[idx_i][2],
            return other_idx, diff_to_other_sensor

        # (459, -707, 401)
        # (391, 539, 444)

        # (390, -675, -793)
        # (322, 571, -750)

        # (-661, -816, -575)
        # (-729, 430, -532)

    return None


def rotate_x(coord):
    x, y, z = coord
    return x, -z, y


def rotate_y(coord):
    x, y, z = coord
    return z, y, -x


def rotate_z(coord):
    x, y, z = coord
    return -y, x, z


@lru_cache(2048)
def overlaps(sensor, sensor_two, minimum_overlap=12):
    s1 = convert_sensor_to_relative_distances(tuple(sensor))
    s2 = convert_sensor_to_relative_distances(tuple(sensor_two))

    for p1 in s1:
        p1_set = set(p1)

        for p2 in s2:
            p2_set = set(p2)
            overlapping_relative_distances = p1_set & p2_set

            if len(overlapping_relative_distances) >= minimum_overlap:
                idx_pointers = {}

                for relative_dist in overlapping_relative_distances:
                    idx_pointers[p1.index(relative_dist)] = p2.index(relative_dist)

                return idx_pointers

    return None


@lru_cache(2048)
def convert_sensor_to_relative_distances(sensor):
    sensor_relative_distances = []

    for point in sensor:
        distances = []

        for inner_point in sensor:
            distances.append((point[0] - inner_point[0], point[1] - inner_point[1], point[2] - inner_point[2]))

        sensor_relative_distances.append(tuple(distances))

    return tuple(sensor_relative_distances)


def test_beacon_count():
    assert count_beacons(open('input/19.test').read().splitlines()) == (79, 3621)
    pass


def test_parse_lines():
    assert parse_lines(open('input/19.test2').read().splitlines()) == [[(0, 2, 0), (4, 1, 0), (3, 3, 0)], [(-1, -1, 0), (-5, 0, 0), (-2, 1, 0)]]


def test_generate_rotated_sensors():
    assert True
    # assert generate_rotated_sensors([[(2, 0, 0)]]) == False


def test_convert_sensor_to_relative_distances():
    assert convert_sensor_to_relative_distances([(0, 2, 0), (4, 1, 0), (3, 3, 0)]) == [{(-4, 1, 0), (0, 0, 0), (-3, -1, 0)}, {(4, -1, 0), (1, -2, 0), (0, 0, 0)}, {(0, 0, 0), (3, 1, 0), (-1, 2, 0)}]


def test_overlaps():
    assert overlaps([(0, 2, 0), (4, 1, 0), (3, 3, 0)], [(-1, -1, 0), (-5, 0, 0), (-2, 1, 0)])


def test_rotate_x():
    assert rotate_x(rotate_x(rotate_x(rotate_x((2, 3, 18))))) == (2, 3, 18)


def test_rotate_y():
    assert rotate_y(rotate_y(rotate_y(rotate_y((2, 3, 18))))) == (2, 3, 18)


def test_rotate_z():
    assert rotate_z(rotate_z(rotate_z(rotate_z((2, 3, 18))))) == (2, 3, 18)


if __name__ == '__main__':
    print(count_beacons(open('input/19').read().splitlines()))