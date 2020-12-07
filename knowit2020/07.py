# https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def sellable_trees(lines):
    c = 0

    for trunk in find(lines[len(lines) - 1], '#'):
        c += is_tree_sellable(lines, trunk)

    return c


def is_tree_sellable(lines, trunk_idx):
    h = len(lines) - 1

    while h > -1 and trunk_idx < len(lines[h]) and lines[h][trunk_idx] == '#':
        # include trunk_idx since that makes .strip work without problems
        r_end = lines[h].find('  ', trunk_idx)
        l_end = lines[h].rfind('  ', 0, trunk_idx)

        r = lines[h][trunk_idx:r_end if r_end > -1 else len(lines[h])].strip()
        l = lines[h][max(0, l_end):trunk_idx+1].strip()[::-1]

        if l != r:
            return False

        h -= 1

    if (trunk_idx < len(lines[h]) and lines[h][trunk_idx-1] == '#') or \
            (trunk_idx < (len(lines[h]) - 1) and lines[h][trunk_idx+1] == '#'):
        return False

    return True


def test_sellable_trees():
    assert 2 == sellable_trees(open('input/07.test').readlines())


if __name__ == '__main__':
    print(sellable_trees(open('input/07').readlines()))
