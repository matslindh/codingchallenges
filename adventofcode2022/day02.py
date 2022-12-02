def calculate_score_for_round(path):
    games = open(path).read().splitlines()
    mapping = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    scores = {'A': 1, 'B': 2, 'C': 3}
    score = 0

    for game in games:
        elf, me = game.split(' ')
        me = mapping[me]
        game_score = 0

        if elf == me:
            game_score = 3
        elif me == 'A' and elf == 'C':
            game_score = 6
        elif me == 'B' and elf == 'A':
            game_score = 6
        elif me == 'C' and elf == 'B':
            game_score = 6

        score += game_score + scores[me]

    return score


def calculate_score_for_round_secret(path):
    games = open(path).read().splitlines()
    scores = {'A': 1, 'B': 2, 'C': 3}
    wins = {'A': 'B', 'B': 'C', 'C': 'A'}
    loses = {'A': 'C', 'B': 'A', 'C': 'B'}
    result_scores = {'X': 0, 'Y': 3, 'Z': 6}
    score = 0

    for game in games:
        elf, result = game.split(' ')

        if result == 'Y':
            game_score = scores[elf]
        elif result == 'Z':
            game_score = scores[wins[elf]]
        else:
            game_score = scores[loses[elf]]

        score += game_score + result_scores[result]

    return score


def test_calculate_score_for_round():
    assert calculate_score_for_round('input/02.test') == 15


def test_calculate_score_for_round_secret():
    assert calculate_score_for_round_secret('input/02.test') == 12


if __name__ == '__main__':
    print(calculate_score_for_round('input/02'))
    print(calculate_score_for_round_secret('input/02'))
