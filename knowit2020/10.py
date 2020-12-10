def tournament_placer(f):
    scores = {}

    for event in [line.strip().split(',') for line in open(f)]:
        for place, contestant in enumerate(event):
            scores[contestant] = scores.get(contestant, 0) + len(event) - place - 1

    return sorted(scores.items(), key=lambda s: s[1], reverse=True)[0]


def test_tournament_placer():
    assert tournament_placer('input/10.test') == ('ae', 11)


if __name__ == '__main__':
    print(tournament_placer('input/10'))
