def landscaper(f, generations):
    seen_states = {}
    states = []
    state = f.readline().strip().split(' ')[-1]
    f.readline()
    rules = {}
    idx = 0
    prev_sum = None

    for rule in f.readlines():
        keys, _, res = rule.strip().split(' ')

        if res == '#':
            rules[keys] = True

    for i in range(0, generations):
        first_hash = state.index('#')

        if first_hash < 5:
            adds = 5 - first_hash
            state = '.' * adds + state
            idx -= adds

        last_hash = state.rindex('#')

        if last_hash > (len(state) - 5):
            state += '.' * (6 - abs(last_hash - len(state)))

        output = state[:2]

        for x in range(2, len(state) - 2):
            output += '#' if state[x-2:x+3] in rules else '.'

        output += state[len(state) - 2:]
        state = output
        k = state.strip('.')

        if k in seen_states:
            current = sum_state(state, idx)

            if prev_sum:
                diff = current - prev_sum

                return current + diff * (generations - seen_states[k][0] - 2)

            prev_sum = current

        seen_states[k] = (i, idx)
        states.append(state)

    return sum_state(state, idx)


def sum_state(state, idx):
    s = 0

    for i in range(0, len(state)):
        add = (i + idx) if state[i] == '#' else 0
        s += add

    return s


def test_landscaper():
    assert landscaper(open('input/12.test'), 20) == 325


if __name__ == '__main__':
    print(landscaper(open('input/12'), 20))
    print(landscaper(open('input/12'), 128))
    print(landscaper(open('input/12'), 50_000_000_000))
