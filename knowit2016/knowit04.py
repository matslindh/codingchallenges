import sys

sequences = []


def is_magic_number(i):
    s = str(i)

    if '7' in s or i % 7 == 0:
        return True

    return False


def get_next_sequence(idx=0):
    if len(sequences) < (idx + 1):
        sequences.append(0)

    sequences[idx] += 1

    if is_magic_number(sequences[idx]):
        return get_next_sequence(idx+1)

    return sequences[idx]


for i in range(1, 1338):
    a = i

    if is_magic_number(i):
        a = get_next_sequence()

    """
        sys.stdout.write('(' + str(a) + ') ')
    else:
        sys.stdout.write(str(a) + ' ')
    """

    print(str(i) + ': ' + str(a))



