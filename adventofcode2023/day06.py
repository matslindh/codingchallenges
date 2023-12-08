import re

def parse_race(lines):
    return tuple(
        zip(
            map(int, re.findall("\d+", lines[0])),
            map(int, re.findall("\d+", lines[1])),
        )
    )


def parse_race_keming(lines):
    time = lines[0].replace(" ", "")
    distance = lines[1].replace(" ", "")
    return tuple(
        zip(
            map(int, re.findall("\d+", time)),
            map(int, re.findall("\d+", distance)),
        )
    )[0]

def winners(race):
    time, record = race
    wins = []

    for charge in range(1, time):
        score = charge * (time - charge)

        if score > record:
            wins.append(charge)

    return wins


def multiply_winning_options(races):
    m = 1

    for race in races:
        m *= len(winners(race))

    return m



def test_parse_race():
    assert parse_race(open("input/06.test").read().splitlines()) == (
        (7, 9), (15, 40), (30, 200)
    )


def test_parse_race_keming():
    assert parse_race_keming(open("input/06.test").read().splitlines()) == (71530, 940200)


def test_winners():
    assert winners((7, 9)) == [2, 3, 4, 5]


def test_multiply_winning_options():
    assert multiply_winning_options([(7, 9), (15, 40), (30, 200)]) == 288


if __name__ == "__main__":
    print(multiply_winning_options(parse_race(open("input/06").read().splitlines())))
    print(multiply_winning_options([parse_race_keming(open("input/06").read().splitlines())]))