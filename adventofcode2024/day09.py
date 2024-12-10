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


def sum_between(a_1, a_2):
    d = a_2 - a_1 + 1
    return d * (a_1 * 2 + d - 1) / 2


def test_defragger_simple():
    assert defragger("input/09.test2") == 60


def test_defragger():
    assert defragger("input/09.test") == 1928


if __name__ == '__main__':
    print(defragger("input/09"))