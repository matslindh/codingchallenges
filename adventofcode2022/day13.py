from functools import cmp_to_key


def parse_message(s, idx=1):
    node = []
    current = ''

    while idx < len(s) - 1:
        if s[idx] == '[':
            v, idx = parse_message(s, idx + 1)
            node.append(v)
            continue

        if s[idx] == ']':
            if current:
                node.append(int(current))

            return node, idx + 1

        if s[idx] == ',':
            if current:
                node.append(int(current))
                current = ''

            idx += 1
            continue

        current += s[idx]
        idx += 1

    if current:
        node.append(int(current))

    return node, idx


def are_messages_in_right_order(left, right):
    for idx in range(min(len(left), len(right))):
        l = left[idx]
        r = right[idx]

        if isinstance(l, list) and not isinstance(r, list):
            res = are_messages_in_right_order(l, [r])
        elif not isinstance(l, list) and isinstance(r, list):
            res = are_messages_in_right_order([l], r)
        elif isinstance(l, list) and isinstance(r, list):
            res = are_messages_in_right_order(l, r)
        else:
            if l < r:
                res = -1
            elif l > r:
                res = 1
            else:
                res = 0

        if res != 0:
            return res

    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


def sum_right_order_indexes(path):
    pair_sum = 0

    for idx, pair in enumerate(open(path).read().split("\n\n"), start=1):
        left, right = pair.split("\n")

        if are_messages_in_right_order(parse_message(left)[0], parse_message(right)[0]) == -1:
            pair_sum += idx

    return pair_sum


def decoder_key(path):
    messages = []

    for line in open(path).read().splitlines():
        if not line:
            continue

        messages.append(parse_message(line)[0])

    messages.append([[2]])
    messages.append([[6]])

    messages_sorted = sorted(messages, key=cmp_to_key(are_messages_in_right_order))

    return (messages_sorted.index([[2]]) + 1) * (messages_sorted.index([[6]]) + 1)


def test_parse_message():
    assert parse_message('[1,1,3,1,1]')[0] == [1, 1, 3, 1, 1]
    assert parse_message('[[1],[2,3,4]]')[0] == [[1], [2, 3, 4]]
    assert parse_message('[[[]]]')[0] == [[[]]]


def test_are_messages_in_right_order():
    assert are_messages_in_right_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == -1
    assert are_messages_in_right_order([[1], [2, 3, 4]], [[1], 4]) == -1
    assert are_messages_in_right_order([9], [[8, 7, 6]]) == 1


def test_sum_right_order_indexes():
    assert sum_right_order_indexes('input/13.test') == 13


def test_decoder_key():
    assert decoder_key('input/13.test') == 140


if __name__ == '__main__':
    print(sum_right_order_indexes('input/13'))
    print(decoder_key('input/13'))


