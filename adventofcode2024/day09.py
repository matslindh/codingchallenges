def defragger(path):
    disk = list(map(int, open(path).read()))
    front = 0
    write_ptr = 0
    back = len(disk) - 1
    s = 0
    disk_out = []

    while front <= back:
        s += sum_between(write_ptr, write_ptr + disk[front] - 1) * front // 2
        avail = disk[front + 1]
        disk_out.extend(str(front // 2) * disk[front])
        write_ptr += disk[front]

        while avail and back > front:
            move = min(avail, disk[back])
            s += sum_between(write_ptr, write_ptr + move - 1) * back // 2
            disk_out.extend(str(back // 2) * move)

            avail -= move
            disk[back] -= move
            write_ptr += move

            if not disk[back]:
                back -= 2

        front += 2

    return int(s)

def defragger_whole_files(path):
    disk = list(map(int, open(path).read()))

    files = []
    free_space = []
    offset = 0

    for idx in range(0, len(disk), 2):
        files.append({
            'idx': idx // 2,
            'size': disk[idx],
            'offset': offset,
        })

        offset += disk[idx]

        if idx < len(disk) - 1:
            free_space.append({
                'size': disk[idx + 1],
                'offset': offset,
            })

            offset += disk[idx + 1]

    for file in files[::-1]:
        for avail in free_space:
            if file['offset'] < avail['offset']:
                break

            if avail['size'] >= file['size']:
                file['offset'] = avail['offset']
                avail['size'] -= file['size']
                avail['offset'] += file['size']

                break

    """
    prev_end = None
    print('')

    for file in sorted(files, key=lambda x: x['offset']):
        if prev_end and prev_end < file['offset']:
            print("." * (file['offset'] - prev_end), end='')

        print(str(file['idx']) * file['size'], end='')
        prev_end = file['offset'] + file['size']
    """
    s = 0

    for file in files:
        s += sum_between(file['offset'], file['offset'] + file['size'] - 1) * file['idx']

    return s


def sum_between(a_1, a_2):
    d = a_2 - a_1 + 1
    return d * (a_1 * 2 + d - 1) // 2


def test_defragger_simple():
    assert defragger("input/09.test2") == 60


def test_defragger():
    assert defragger("input/09.test") == 1928


def test_defragger_whole_files():
    assert defragger_whole_files("input/09.test") == 2858


if __name__ == '__main__':
    print(defragger("input/09"))
    print(defragger_whole_files("input/09"))