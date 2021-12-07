def crabmover_2000(number_line, cost_function):
    positions = list(map(int, number_line.split(',')))
    max_pos = max(positions)
    min_pos = min(positions)
    best_distance = None

    for i in range(min_pos, max_pos+1):
        current_dist = sum([cost_function(abs(position - i)) for position in positions])

        if best_distance is None or best_distance > current_dist:
            best_distance = current_dist

    return best_distance


def test_crabmover_2000():
    assert crabmover_2000('16,1,2,0,4,2,7,1,2,14', lambda x: x) == 37
    assert crabmover_2000('16,1,2,0,4,2,7,1,2,14', lambda x: (x * (x + 1)) / 2) == 168


if __name__ == '__main__':
    print(crabmover_2000(open('input/07').read(), lambda x: x))
    print(crabmover_2000(open('input/07').read(), lambda x: (x * (x + 1)) / 2))
