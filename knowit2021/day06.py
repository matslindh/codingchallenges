def boxstacker_3000(instructions):
    field = ['X' * 20]

    def add_row():
        field.insert(0, '.' * 20)

    toppled = 0

    for instruction in instructions:
        left_idx, length = map(int, instruction.split(','))
        right_idx = left_idx + length
        mid = (left_idx + length / 2.0)

        for ridx, row in enumerate(field):
            left = row.find('X', left_idx, right_idx)
            right = row.rfind('X', left_idx, right_idx)

            if left != -1 or right != -1:
                if length > 1 and (left >= mid or (right + 1) <= mid):
                    toppled += 1
                    break

                if ridx == 0:
                    add_row()
                    ridx += 1

                field[ridx-1] = field[ridx-1][:left_idx] + 'X' * length + field[ridx-1][right_idx:]
                break

    print("\n" + "\n".join(field) + "\n\n")
    return toppled


def test_boxstacker_3000():
    test_data = """0,6
0,1
4,3
"""

    assert boxstacker_3000(test_data.splitlines()) == 0
    assert boxstacker_3000((test_data + '2,4').splitlines()) == 1
    assert boxstacker_3000((test_data + '0,5').splitlines()) == 0
    assert boxstacker_3000((test_data + '0,1').splitlines()) == 0
    assert boxstacker_3000((test_data + '6,2').splitlines()) == 1
    assert boxstacker_3000((test_data + '0,2').splitlines()) == 1
    assert boxstacker_3000((test_data + "0,1\n0,1").splitlines()) == 0
    assert boxstacker_3000((test_data + "0,1\n0,1\n1,1").splitlines()) == 0


if __name__ == '__main__':
    print(boxstacker_3000(open('input/06').read().splitlines()))
