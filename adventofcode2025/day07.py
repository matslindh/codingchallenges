from common import as_board


def tachyon_splitter(path):
    lines = as_board(path)
    beams = {'S', '|'}
    splits = {'^'}
    line_len = len(lines[0])
    split_count = 0

    for line_idx, line in enumerate(lines[:-1]):
        for c_idx, c in enumerate(line):
            if c in beams:
                if lines[line_idx + 1][c_idx] in splits:
                    split_count += 1

                    if c_idx > 0:
                        lines[line_idx + 1][c_idx - 1] = '|'

                    if c_idx < line_len - 1:
                        lines[line_idx + 1][c_idx + 1] = '|'
                else:
                    lines[line_idx + 1][c_idx] = '|'

    return split_count, 0


def test_tachyon_splitter():
    assert tachyon_splitter('input/07.test') == (21, 40)


if __name__ == '__main__':
    print(tachyon_splitter('input/07'))
