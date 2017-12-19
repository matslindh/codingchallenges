def explore(lines):
    y = 0
    x = lines[0].index('|')
    dx = 0
    dy = 1
    answer = ''
    steps = 0

    while True:
        x += dx
        y += dy

        if lines[y][x] == '+':
            if x < (len(lines[y]) - 1) and lines[y][x+1].strip() and dx != -1:
                dx = 1
                dy = 0

            elif y < (len(lines) - 1) and x < len(lines[y+1]) and lines[y+1][x].strip() and dy != -1:
                dx = 0
                dy = 1

            elif y > 0 and x < len(lines[y-1]) and lines[y-1][x].strip() and dy != 1:
                dx = 0
                dy = -1

            elif x > 0 and lines[y][x-1].strip() and dx != 1:
                dx = -1
                dy = 0
        elif lines[y][x] == ' ':
            break
        elif lines[y][x] not in ('-', '|'):
            answer += lines[y][x]

        steps += 1

    return answer, steps + 1


def test_explore():
    assert ('ABCDEF', 38) == explore(open("input/dec19_test").readlines())


if __name__ == "__main__":
    print(explore(open("input/dec19").readlines()))