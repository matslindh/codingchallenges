import math


def evaluate_nanos(f):
    bots = []
    best = None
    intersects = []

    for line in f.readlines():
        pos, r = line.strip().split(', ')
        r = int(r.split('=')[1])
        pos = [int(x) for x in pos.split('=')[1][1:-1].split(',')]

        bots.append((pos, r))
        intersects.append([])

        if not best or r > best[1]:
            best = (pos, r)

    c = 0

    for bot in bots:
        d = abs(bot[0][0] - best[0][0]) + abs(bot[0][1] - best[0][1]) + abs(bot[0][2] - best[0][2])

        if d <= best[1]:
            c += 1

    for i in range(0, len(bots)):
        for j in range(i + 1, len(bots)):
            d = abs(bots[i][0][0] - bots[j][0][0]) + abs(bots[i][0][1] - bots[j][0][1]) + abs(bots[i][0][2] - bots[j][0][2])
            reach = bots[i][1] + bots[j][1]

            if d < reach:
                intersects[i].append(j)
                intersects[j].append(i)

    lens = [len(intersect) for intersect in intersects]
    best_intersect_count = max(lens)

    best_idx = lens.index(best_intersect_count)

    while best_idx >= 0:
        print("best", best_idx)
        reaches = []
        reaches_idx = []

        for idx in intersects[best_idx]:
            if idx == best_idx:
                continue

            d = abs(bots[idx][0][0] - bots[best_idx][0][0]) + \
                abs(bots[idx][0][1] - bots[best_idx][0][1]) + \
                abs(bots[idx][0][2] - bots[best_idx][0][2])

            reach = bots[idx][1] + bots[best_idx][1]

            if d < reach:
                reaches.append(reach - d)
                reaches_idx.append(idx)

        m = min(reaches)
        v = reaches_idx[reaches.index(m)]
        print(v)
        print(reaches)
        print(reaches_idx)
        m_diff = math.ceil(m / 2)

        mid = (
            (bots[v][0][0] + bots[best_idx][0][0]) // 2,
            (bots[v][0][1] + bots[best_idx][0][1]) // 2,
            (bots[v][0][2] + bots[best_idx][0][2]) // 2,
        )

        area = {}

        print(v, "intersects is", bots[v], "source is", bots[best_idx])
        print("mid is", mid)
        print("min reach", m)

        print("x diff", abs(bots[v][0][0] - bots[best_idx][0][0]))
        print("y diff", abs(bots[v][0][1] - bots[best_idx][0][1]))
        print("z diff", abs(bots[v][0][2] - bots[best_idx][0][2]))

        for z in range(mid[2] - m_diff, mid[2] + m_diff):
            if z not in area:
                area[z] = {}

            for y in range(mid[1] - m_diff, mid[1] + m_diff):
                if y not in area[z]:
                    area[z][y] = {}

                for x in range(mid[0] - m_diff, mid[0] + m_diff):
                    area[z][y][x] = 0

                    for bot_idx in intersects[best_idx]:
                        n = bots[bot_idx]

                        d = abs(x - n[0][0]) + \
                            abs(y - n[0][1]) + \
                            abs(z - n[0][2])

                        if d <= n[1]:
                            area[z][y][x] += 1

            print(area)
        try:
            best_idx = lens.index(best_intersect_count, best_idx + 1)
        except ValueError:
            break

    print("best number in reach of", max(lens))
    print(lens.count(best_intersect_count))
    return c


def test_evaluate_nanos():
    assert evaluate_nanos(open('input/23.test'))[0] == 7


def test_optimal_pos():
    assert evaluate_nanos(open('input/23b.test'))[1] == (12, 12, 12)


if __name__ == '__main__':
    print(evaluate_nanos(open('input/23b.test')))