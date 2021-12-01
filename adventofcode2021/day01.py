test_data = """199
200
208
210
200
207
240
269
260
263"""


def count_depth_increases(measurements, sliding_window=1):
    increase_count = 0
    current_depth = sum(measurements[0:sliding_window])

    for idx in range(1, len(measurements) - sliding_window + 1):
        avg_measurement = sum(measurements[idx:idx+sliding_window])

        if avg_measurement > current_depth:
            increase_count += 1

        current_depth = avg_measurement

    return increase_count


def run_count_depth_increases(raw_input, sliding_window=1):
    depths = [int(line.strip()) for line in raw_input.split("\n")]
    return count_depth_increases(depths, sliding_window=sliding_window)


def test_count_depth_increases():
    assert run_count_depth_increases(test_data) == 7


def test_count_depth_increases_sliding_window():
    assert run_count_depth_increases(test_data, sliding_window=3) == 5


if __name__ == '__main__':
    with open("input/01") as f:
        actual_data = f.read()
        print(run_count_depth_increases(actual_data))
        print(run_count_depth_increases(actual_data, sliding_window=3))
