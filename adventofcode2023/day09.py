from itertools import pairwise


def parse_lines(lines):
    return tuple(
        tuple(map(int, line.split(' '))) for line in lines
    )


def diff_reducer(numbers):
    return tuple(
        b - a
        for a, b in pairwise(numbers)
    )


def predict_next_number(history):
    diffs = [history]
    current = history

    while len(set(current)) != 1:
        current = diff_reducer(current)
        diffs.append(current)

    predicted = 0

    for measurement in diffs[::-1]:
        predicted += measurement[-1]

    return predicted


def predict_zeroth_number(history):
    diffs = [history]
    current = history

    while len(set(current)) != 1:
        current = diff_reducer(current)
        diffs.append(current)

    predicted = 0

    for measurement in diffs[::-1]:
        predicted = measurement[0] - predicted

    return predicted


def test_predict_next_number():
    assert predict_next_number((0, 3, 6, 9, 12, 15)) == 18
    assert predict_next_number((1, 3, 6, 10, 15, 21)) == 28
    assert predict_next_number((10, 13, 16, 21, 30, 45)) == 68


def test_predict_zeroth_number():
    assert predict_zeroth_number((0, 3, 6, 9, 12, 15)) == -3
    assert predict_zeroth_number((1, 3, 6, 10, 15, 21)) == 0
    assert predict_zeroth_number((10, 13, 16, 21, 30, 45)) == 5


def test_parse_lines():
    assert parse_lines(open("input/09.test")) == (
        (0, 3, 6, 9, 12, 15),
        (1, 3, 6, 10, 15, 21),
        (10, 13, 16, 21, 30, 45),
    )


if __name__ == "__main__":
    histories = parse_lines(open("input/09").read().splitlines())

    print(sum(
        predict_next_number(history)
        for history in histories
    ))

    print(sum(
        predict_zeroth_number(history)
        for history in histories
    ))