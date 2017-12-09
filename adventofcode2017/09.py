def score_group(input):
    in_ignore = False
    in_garbage = False
    level = 0
    score = 0
    garb_count = 0

    for c in input:
        if in_ignore:
            in_ignore = False
            continue

        if in_garbage:
            if c == '!':
                in_ignore = True
                continue

            if c == '>':
                in_garbage = False
                continue

            garb_count += 1
            continue

        if c == '<':
            in_garbage = True
            continue

        if c == '{':
            level += 1
            continue

        if c == '}':
            score += level
            level -= 1
            continue

    return score, garb_count


def test_score_group():
    assert 1, 0 == score_group('{}')
    assert 6, 0 == score_group('{{{}}}')
    assert 5, 0 == score_group('{{},{}}')
    assert 16, 0 == score_group('{{{},{},{{}}}}')
    assert 1, 4 == score_group('{<a>,<a>,<a>,<a>}')
    assert 9, 8 == score_group('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    assert 9, 0 == score_group('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    assert 3, 6 == score_group('{{<a!>},{<a!>},{<a!>},{<ab>}}')


if __name__ == "__main__":
    print(score_group(open('input/dec09').read()))