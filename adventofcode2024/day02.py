def verify_scan(entries):
    increases = entries[1] > entries[0]

    for idx in range(1, len(entries)):
        diff = entries[idx] - entries[idx - 1]
        diff_invalid = abs(diff) > 3 or diff == 0

        inc = entries[idx] > entries[idx - 1]
        inc_invalid = inc != increases

        if diff_invalid or inc_invalid:
            return False

    return True

def valid_entry(entries):
    initial_valid = verify_scan(entries)

    for skip in range(len(entries)):
        skipped = entries[:skip] + entries[skip + 1:]
        skipped_valid = verify_scan(skipped)

        if skipped_valid:
            return initial_valid, skipped_valid

    return initial_valid, False


def count_valid_entries(path):
    lines = [tuple(map(int, line.split())) for line in open(path).read().splitlines()]
    valid = 0
    cnt_valid = 0

    for entry in lines:
        valid_without_removal, valid_with_removal = valid_entry(entry)

        valid += valid_without_removal
        cnt_valid += valid_with_removal

    return valid, cnt_valid


def test_is_valid_report():
    assert valid_entry([1, 2, 3]) == (True, True)
    assert valid_entry([1, 3, 2]) == (False, True)
    assert valid_entry([1, 2, 6]) == (False, True)


def test_count_valid_entries():
    assert count_valid_entries("input/02.test") == (2, 4)


if __name__ == '__main__':
    print(count_valid_entries("input/02"))