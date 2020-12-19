from collections import defaultdict


def rotate(l, n):
    n = n % len(l)
    return l[n:] + l[:n]


def charspinnerizer(line):
    contestants = []
    iteration = 0

    rule, slide, *rest = line.split(' ')

    for contestant in rest:
        contestants.append(contestant.strip('[').strip(']').strip(',').strip())

    rule = int(rule)
    slide = int(slide)

    def rule_1():
        contestants.pop(0)

    def rule_2():
        contestants.pop(iteration % len(contestants))

    def rule_3():
        if len(contestants) == 2:
            contestants.pop(0)
            return

        pre = len(contestants) % 2 == 0
        contestants.pop(len(contestants) // 2)

        if pre:
            contestants.pop(len(contestants) // 2)

    def rule_4():
        contestants.pop()

    callbacks = {
        1: rule_1,
        2: rule_2,
        3: rule_3,
        4: rule_4,
    }

    while len(contestants) > 1:
        if iteration >= len(contestants):
            iteration = 0

        contestants = rotate(contestants, -slide)
        callbacks[rule]()
        iteration += 1

    return contestants[0]


def test_charspinnerizer():
    assert charspinnerizer('1 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]') == 'Olaf'
    assert charspinnerizer('2 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]') == 'Jenny'
    assert charspinnerizer('3 3 [Jenny, Alvin, Greger, Petra, Olaug]') == 'Petra'
    assert charspinnerizer('4 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]') == 'Alvin'


if __name__ == '__main__':
    winners = defaultdict(int)

    for line in [x.strip() for x in open('input/19')]:
        winners[charspinnerizer(line)] += 1

    print(sorted(winners.items(), key=lambda x: x[1])[-1])
