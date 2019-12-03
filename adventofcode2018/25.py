def constellate(f):
    stars = []
    constellations = []

    for f in f.readlines():
        stars.append({'pos': [int(x) for x in f.strip().split(',')], 'constellation': None})

    for i in range(0, len(stars) - 1):
        if stars[i]['constellation'] is None:
            stars[i]['constellation'] = [i]
            constellations.append(stars[i]['constellation'])

        for j in range(i + 1, len(stars)):
            d = 0

            for el in range(0, 4):
                d += abs(stars[i]['pos'][el] - stars[j]['pos'][el])

            if d <= 3:
                # print(i, j, d)
                # print(stars[j]['constellation'])
                if stars[j]['constellation']:
                    # print("j has constellation")
                    if stars[i]['constellation'] == stars[j]['constellation']:
                        continue

                    # print(i, stars[i]['constellation'])
                    # print(j, stars[j]['constellation'])

                    stars[i]['constellation'] += stars[j]['constellation']

                    while stars[j]['constellation']:
                        x = stars[j]['constellation'].pop()
                        # print("popped", x, stars[j]['constellation'])

                        if x == j:
                            continue

                        stars[x]['constellation'] = stars[i]['constellation']

                    stars[j]['constellation'] = stars[i]['constellation']
                else:
                    stars[i]['constellation'].append(j)
                    stars[j]['constellation'] = stars[i]['constellation']

    # print(constellations)
    return list(filter(lambda x: bool(x), constellations))


def test_constellate():
    assert len(constellate(open('input/25.test'))) == 2
    assert len(constellate(open('input/25-1.test'))) == 4
    assert len(constellate(open('input/25-2.test'))) == 3
    assert len(constellate(open('input/25-3.test'))) == 8


# 447 too high
if __name__ == '__main__':
    out = constellate(open('input/25'))
    print(len(out))
    entries = set()

    for constellation in out:
        entries.update(set(constellation))

    for i in range(0, 1000):
        if i not in entries:
            print(i)

