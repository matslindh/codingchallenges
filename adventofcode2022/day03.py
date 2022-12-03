import string


def get_priority_for_letter(letter):
    if letter in string.ascii_lowercase:
        return string.ascii_lowercase.find(letter) + 1

    return string.ascii_uppercase.find(letter) + 27


def calculate_priority(path):
    rucksacks = open(path).read().splitlines()
    commons = []

    for sack in rucksacks:
        split_point = len(sack) // 2
        compartment_1 = sack[:split_point]
        compartment_2 = sack[split_point:]

        commons.append((set(compartment_1) & set(compartment_2)).pop())

    priorities = list(map(get_priority_for_letter, commons))
    return sum(priorities)


def calculate_priority_groups(path):
    rucksacks = open(path).read().splitlines()
    commons = []

    for idx in range(0, len(rucksacks), 3):
        commons.append((set(rucksacks[idx]) & set(rucksacks[idx+1]) & set(rucksacks[idx+2])).pop())

    return sum(map(get_priority_for_letter, commons))


def test_calculate_priority():
    assert calculate_priority('input/03.test') == 157


def test_calculate_priority_groups():
    assert calculate_priority_groups('input/03.test') == 70


def test_get_priority_for_letter():
    assert get_priority_for_letter('a') == 1
    assert get_priority_for_letter('z') == 26
    assert get_priority_for_letter('A') == 27
    assert get_priority_for_letter('Z') == 52


if __name__ == '__main__':
    print(calculate_priority('input/03'))
    print(calculate_priority_groups('input/03'))
