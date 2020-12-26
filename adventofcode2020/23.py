from collections import deque

@profile
def play(cups, iterations=100):
    m = max(cups)
    dq = deque(cups)
    indices = {}

    for cidx, c in enumerate(cups):
        indices[c] = cidx

    while iterations:
        current = original_current = dq.popleft()
        extracted = (dq.popleft(), dq.popleft(), dq.popleft())

        while True:
            current -= 1
            
            if current < 1:
                current = m

            if current not in extracted:
                break

        # four has disappeared in front
        dest_idx = indices[c] - 4
        dq.insert(dest_idx+1, extracted[2])
        dq.insert(dest_idx+1, extracted[1])
        dq.insert(dest_idx+1, extracted[0])
        dq.append(original_current)
        iterations -= 1

        if iterations % 1000 == 0:
            return list(dq)
            print(iterations)

    return list(dq)


def extract(cups, idx):
    end = (idx + 3) % len(cups)

    if end < idx:
        if end == 4:
            to_insert = cups[0:4]
            del cups[0:4]
        else:
            to_insert = cups[idx:] + cups[0:end]
            del cups[idx:]
            del cups[0:end]
    else:
        to_insert = cups[idx:idx+3]
        del cups[idx:idx+3]

    return to_insert


def order_after_one(cups):
    idx = cups.index(1)
    return cups[idx+1:] + cups[:idx]


def test_extract():
    l = [1, 2, 3, 4, 5, 6]
    assert extract(l, 0) == [1, 2, 3]
    assert l == [4, 5, 6]

    l = [1, 2, 3, 4, 5, 6]
    assert extract(l, 5) == [6, 1, 2]
    assert l == [3, 4, 5]

    l = [1, 2, 3, 4, 5, 6]
    assert extract(l, 4) == [5, 6, 1]
    assert l == [2, 3, 4]


def test_order_after_one():
    assert order_after_one([int(x) for x in '328915467']) == [int(x) for x in '54673289']


def test_play_and_order():
    cups = [int(x) for x in '389125467']    
    assert order_after_one(play(cups, 10)) == [int(x) for x in '92658374']

    cups = [int(x) for x in '389125467']
    assert order_after_one(play(cups)) == [int(x) for x in '67384529']


"""def test_play_v2():
    cups = [int(x) for x in '389125467']

    for i in range(10, 1000001):
        cups.append(i)

    play(cups, 1000000)
    assert False"""


if __name__ == '__main__':
    print(order_after_one(play([int(x) for x in '523764819'])))

    cups = [int(x) for x in '523764819']
    cups.extend(list(range(10, 1000001)))

    result = play(cups, 1000000)
    r_idx = result.index(1)
    print(result[r_idx+1], result[r_idx+2], result[r_idx+1] * result[r_idx+2])

"""
    cups = [int(x) for x in '389125467']
    cups.extend(list(range(10, 1000001)))

    result = play(cups, 1000000)
    r_idx = result.index(1)
    print(result[r_idx+1], result[r_idx+2], result[r_idx+1] * result[r_idx+2]) """

