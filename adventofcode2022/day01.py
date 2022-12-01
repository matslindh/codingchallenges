def get_maximum_calories(path):
    lines = open(path).read().splitlines()
    calories = []
    current = 0

    for line in lines:
        if not line:
            calories.append(current)
            current = 0
            continue

        current += int(line)

    calories.append(current)
    calories = sorted(calories, reverse=True)
    return max(calories), sum(calories[:3])


def test_maximum_calories():
    assert get_maximum_calories('input/01.test') == (24000, 45000)


if __name__ == '__main__':
    print(get_maximum_calories('input/01'))
