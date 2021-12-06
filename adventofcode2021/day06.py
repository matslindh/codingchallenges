from collections import Counter


def simulate_fish_cycles(sequence, iterations):
    fishies = list(map(int, sequence.split(',')))

    for iteration in range(iterations):
        for idx in range(len(fishies)):
            fishies[idx] -= 1

            if fishies[idx] == -1:
                fishies[idx] = 6
                fishies.append(8)

        print(','.join(map(str, fishies)))

    return len(fishies)


def counter_based_fish_cycle_simulator(sequence, iterations):
    fishies = dict(Counter(map(int, sequence.split(','))))

    for iteration in range(iterations):
        new_fishies = {}

        for day in range(9):
            if day > 0:
                new_fishies[day - 1] = new_fishies.get(day - 1, 0) + fishies.get(day, 0)
            else:
                new_fishies[6] = new_fishies.get(6, 0) + fishies.get(0, 0)
                new_fishies[8] = fishies.get(0, 0)

        fishies = new_fishies

    return sum(fishies.values())


def test_simulate_fish_cycles():
    assert counter_based_fish_cycle_simulator('1', 3) == 2
    assert counter_based_fish_cycle_simulator('3,4,3,1,2', 80) == 5934
    assert counter_based_fish_cycle_simulator('3,4,3,1,2', 256) == 26984457539


if __name__ == '__main__':
    print(counter_based_fish_cycle_simulator(open('input/06').read().strip(), 80))
    print(counter_based_fish_cycle_simulator(open('input/06').read().strip(), 256))