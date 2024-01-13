from utils import rs


def parse_lines(lines):
    platform = dict()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                continue

            platform[y, x] = c

    return platform


def slide_platform(platform, width, height):
    new_platform = {}

    for x in range(width):
        current_pos = 0

        for y in range(height):
            coord = y, x

            if coord not in platform:
                continue

            if platform[coord] == '#':
                new_platform[coord] = '#'
                current_pos = y + 1

            if platform[coord] == 'O':
                new_platform[current_pos, x] = 'O'
                current_pos += 1

    return new_platform


def slide_and_rotate(platform, width, height, count=1000000000):
    seen_configuration = {}
    idx = 0

    while idx < count:
        for slide in range(4):
            platform = slide_platform(platform, width, height)
            platform = rotate_platform(platform, width, height)

        k = hashable_platform(platform)

        if k in seen_configuration:
            interval_size = idx - seen_configuration[k]
            repeats = (count - seen_configuration[k]) // interval_size
            print(idx, seen_configuration[k], interval_size)
            idx = repeats * interval_size + seen_configuration[k]
            print(idx)

        seen_configuration[k] = idx
        idx += 1

    return platform



def rotate_platform(platform, width, height):
    new_platform = {}

    for y, x in platform.keys():
        new_platform[x, height - y - 1] = platform[y, x]

    return new_platform


def hashable_platform(platform):
    return tuple((y, x, c) for (y, x), c in platform.items())


def score_slide_it(lines):
    width = len(lines[0])
    height = len(lines)

    platform = slide_platform(parse_lines(lines), width=width, height=height)
    return score_platform(platform, width, height)


def score_slide_and_rotate(lines):
    width = len(lines[0])
    height = len(lines)

    platform = slide_and_rotate(parse_lines(lines), width=width, height=height)
    return score_platform(platform, width, height)

def score_platform(platform, width, height):
    score = 0

    for y in range(height):
        for x in range(width):
            coord = y, x

            if coord not in platform:
                continue

            if platform[coord] == 'O':
                score += height - y

    return score


def test_slide_and_rotate():
    lines = rs("14.test")
    width = len(lines[0])
    height = len(lines)

    platform = parse_lines(lines)

    assert score_platform(slide_and_rotate(platform, width, height), width, height) == 64


def test_slide_it():
    assert score_slide_it(rs("14.test")) == 136


def test_rotate_platform():
    lines = rs("14.test")
    width = len(lines[0])
    height = len(lines)

    platform = parse_lines(lines)

    platform_1 = rotate_platform(platform, width, height)
    platform_2 = rotate_platform(platform_1, width, height)
    platform_3 = rotate_platform(platform_2, width, height)
    platform_4 = rotate_platform(platform_3, width, height)

    # neste: lage noe som er hashable sånn at vi kan slenge hele brettet i en state og hvilken vei vi skal slide, slik av oppdager perioden

    assert platform_1 != platform_2
    assert platform_2 != platform_3
    assert platform_3 != platform_4
    assert platform_4 == platform


if __name__ == "__main__":
    print(score_slide_it(rs("14")))
    print(score_slide_and_rotate(rs("14")))