from collections import defaultdict
from functools import cmp_to_key


def read_rules(path):
    rules = defaultdict(list)
    updates = []

    lines = open(path).read().splitlines()
    in_rules = True

    for line in lines:
        if not line:
            in_rules = False
            continue

        if in_rules:
            page, before = tuple(map(int, line.split('|')))
            rules[page].append(before)
        else:
            updates.append(tuple(map(int, line.split(','))))

    return rules, updates


def is_order_valid_for_update(rules, update):
    already_processed = set()
    valid = True

    for update_page in update:
        for page_before in rules.get(update_page, tuple()):
            if page_before in already_processed:
                valid = False
                break

        if not valid:
            break

        already_processed.add(update_page)

    return valid

def determine_if_updates_are_in_correct_order(rules, updates):
    summed_middle_pages = 0
    summed_corrected_pages = 0

    def rules_sorter(a, b):
        if b in rules.get(a, tuple()):
            return -1

        if a in rules.get(b, tuple()):
            return 1

        return 0

    for update in updates:
        valid = is_order_valid_for_update(rules, update)

        if valid:
            summed_middle_pages += update[len(update) // 2]
        else:
            ordered = sorted(update, key=cmp_to_key(rules_sorter))
            summed_corrected_pages += ordered[len(ordered) // 2]

    return summed_middle_pages, summed_corrected_pages


def test_determine_if_updates_are_in_correct_order():
    rules, updates = read_rules('input/05.test')

    assert determine_if_updates_are_in_correct_order(rules=rules, updates=updates) == (143, 123)


if __name__ == '__main__':
    parsed_rules, updates = read_rules('input/05')
    print(determine_if_updates_are_in_correct_order(rules=parsed_rules, updates=updates))