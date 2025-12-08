from common import as_board


class Node:
    def __init__(self):
        self.children = []


def tachyon_splitter(path):
    lines = as_board(path)
    beams = {'S', '|'}
    splits = {'^'}
    line_len = len(lines[0])
    split_count = 0

    for line_idx in range(len(lines)):
        for c_idx in range(len(lines[0])):
            if lines[line_idx][c_idx] == '.':
                lines[line_idx][c_idx] = 0

    lines[0][lines[0].index('S')] = 1

    for line_idx, line in enumerate(lines[:-1]):
        for c_idx, c in enumerate(line):
            current = lines[line_idx][c_idx]

            if type(c) is int and c > 0:
                if lines[line_idx + 1][c_idx] in splits:
                    split_count += 1

                    if c_idx > 0:
                        lines[line_idx + 1][c_idx - 1] += current

                    if c_idx < line_len - 1:
                        lines[line_idx + 1][c_idx + 1] += current
                else:
                    lines[line_idx + 1][c_idx] += current

    return split_count, sum(lines[-1])  # there are no splits on last line, so every value is an int


def test_tachyon_splitter():
    assert tachyon_splitter('input/07.test') == (21, 40)


if __name__ == '__main__':
    print(tachyon_splitter('input/07'))
