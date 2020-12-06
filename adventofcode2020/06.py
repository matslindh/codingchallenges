def count_unique_answers(l):
    a = set()

    for answer in l:
        a.update(answer)

    return len(a)


def count_all_had_answered(l):
    a = set(l[0])

    for answer in l[1:]:
        a &= set(answer)

    return len(a)


def sum_answers(f, counter=count_unique_answers):
    lines = [x.strip() for x in open(f).readlines()]
    current_set = []
    amount = 0

    for line in lines:
        if not line:
            amount += counter(current_set)
            current_set = []
        else:
            current_set.append(line)

    if current_set:
        amount += counter(current_set)

    return amount


def test_count_unique_answers():
    assert 3 == count_unique_answers(['abc'])
    assert 3 == count_unique_answers(['a', 'b', 'c'])
    assert 3 == count_unique_answers(['ab', 'ac'])


def test_count_all_had_answered():
    assert 3 == count_all_had_answered(['abc'])
    assert 0 == count_all_had_answered(['a', 'b', 'c'])
    assert 1 == count_all_had_answered(['ab', 'ac'])


def test_sum_answers():
    assert 11 == sum_answers('input/06.test', counter=count_unique_answers)


def test_sum_answers_count_all():
    assert 6 == sum_answers('input/06.test', counter=count_all_had_answered)


if __name__ == '__main__':
    print(sum_answers('input/06', counter=count_unique_answers))
    print(sum_answers('input/06', counter=count_all_had_answered))