def steps_until_repeat(configuration):
    seen = {}
    steps = 0
    conflen = len(configuration)
    started_at = None

    while True:
        k = '-'.join([str(x) for x in configuration])

        if k in seen:
            started_at = seen[k]
            break

        seen[k] = steps

        best = 0
        best_idx = 0

        for i in range(0, conflen):
            if configuration[i] > best:
                best_idx = i
                best = configuration[i]

        to_divide = configuration[best_idx]
        configuration[best_idx] = 0

        while to_divide:
            best_idx = (best_idx + 1) % conflen
            configuration[best_idx] += 1
            to_divide -= 1

        steps += 1

    return steps, steps - started_at


def test_steps_until_repeat():
    assert 5, 4 == steps_until_repeat([0, 2, 7, 0])


if __name__ == "__main__":
    data = [int(x.strip()) for x in open("input/dec06").read().split("\t")]
    print(steps_until_repeat(data))
