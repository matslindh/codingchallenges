import re
from cachetools import cached


def bagger(look_for, file_path):
    rules, inverse = make_nodes(file_path)

    unique_colors = set()
    stack = [look_for]

    while stack:
        current_color = stack.pop(0)

        for lookup_color in inverse[current_color]:
            if lookup_color in unique_colors:
                continue

            unique_colors.add(lookup_color)
            stack.append(lookup_color)

    @cached(cache={})
    def child_bag_count(color):
        if not rules[color]:
            return 1

        count = 1

        for inner_color, inner_count in rules[color].items():
            count += inner_count * child_bag_count(inner_color)

        return count

    # -1 since we don't want to count the golden bag itself
    return len(unique_colors), child_bag_count(look_for) - 1


def make_nodes(file_path):
    rules = {}
    inverse = {}

    for rule in [x.strip() for x in open(file_path).readlines()]:
        m = re.match('^([a-z ]+) bags contain (.*)', rule)
        my_color, other = m.groups()
        rules[my_color] = {}

        if my_color not in inverse:
            inverse[my_color] = []

        for count, color in re.findall('([0-9]+) ([a-z ]+?) bag', other):
            if color not in inverse:
                inverse[color] = []

            rules[my_color][color] = int(count)
            inverse[color].append(my_color)

    return rules, inverse


def test_bagger():
    assert (4, 32) == bagger('shiny gold', 'input/07.test')


if __name__ == '__main__':
    print(bagger('shiny gold', 'input/07'))
