from functools import reduce
from operator import mul

def parse_line(line: str):
    game_line, rounds_line = line.split(": ")
    game_id = int(game_line.split()[1])
    rounds = []

    for round_line in rounds_line.split('; '):
        round_values = {}

        for stone_line in round_line.split(', '):   # 1 red, 2 green => ['1 red', '2 green']
            count_str, color = stone_line.split()
            round_values[color] = int(count_str)

        rounds.append(round_values)

    return {
        'id': game_id,
        'rounds': rounds,
    }


def does_rounds_satisfy_minimum_criteria(rounds, criteria):
    for round_ in rounds:
        for round_color, round_count in round_.items():
            if criteria.get(round_color, 0) < round_count:
                return False

    return True


def sum_games_that_pass(criteria, lines):
    summed_game_ids = 0

    for line in lines:
        game = parse_line(line)

        if does_rounds_satisfy_minimum_criteria(rounds=game['rounds'], criteria=criteria):
            summed_game_ids += game['id']

    return summed_game_ids


def cube_power(cubes):
    values = list(cubes.values())
    values.insert(0, 1)

    return reduce(mul, values)


def sum_cube_power_of_games(lines):
    allstin_powers = 0

    for line in lines:
        game = parse_line(line)
        cubes = minimum_required_number_of_cubes(game['rounds'])

        allstin_powers += cube_power(cubes)

    return allstin_powers


def minimum_required_number_of_cubes(rounds):
    minimum_required = {}

    for round_ in rounds:
        for color, count in round_.items():
            minimum_required[color] = max(minimum_required.get(color, -1), count)

    return minimum_required


def test_minimum_required_number_of_cubes():
    assert minimum_required_number_of_cubes([
            {'blue': 3, 'red': 4},
            {'red': 1, 'green': 2, 'blue': 6},
            {'green': 2}
        ]) == {
            'red': 4,
            'green': 2,
            'blue': 6,
        }


def test_sum_cube_power_of_games():
    assert sum_cube_power_of_games(open("input/02.test").read().splitlines()) == 2286


def test_cube_power():
    assert cube_power({'red': 4, 'green':2 , 'blue': 6}) == 48


def test_sum_games_that_pass():
    assert sum_games_that_pass({'red': 12, 'green': 13, 'blue': 14}, open("input/02.test").read().splitlines()) == 8


def test_parse_line():
    assert parse_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {
        'id': 1,
        'rounds': [
            {'blue': 3, 'red': 4},
            {'red': 1, 'green': 2, 'blue': 6},
            {'green': 2}
        ]
    }

def test_does_rounds_satisfy_minimum_criteria():
    assert does_rounds_satisfy_minimum_criteria(
        rounds=[
            {'blue': 3, 'red': 4},
            {'red': 1, 'green': 2, 'blue': 6},
            {'green': 2}
        ],
        criteria={'red': 12, 'green': 13, 'blue': 14}
    )

    assert not does_rounds_satisfy_minimum_criteria(
        rounds=[
            {'blue': 3, 'red': 4},
            {'red': 1, 'green': 2, 'blue': 6},
            {'green': 2}
        ],
        criteria={'red': 3, 'green': 13, 'blue': 14}
    )


if __name__ == '__main__':
    print(sum_games_that_pass(
        {'red': 12, 'green': 13, 'blue': 14},
        open("input/02").read().splitlines()
    ))

    print(sum_cube_power_of_games(
        open("input/02").read().splitlines()
    ))