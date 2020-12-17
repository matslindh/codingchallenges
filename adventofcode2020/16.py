import re
from functools import reduce
from operator import mul


def clickit_or_tickit(f):
    rules = {}
    my_ticket = None
    other_tickets = []
    valid_tickets = []
    mode = 'rules'

    for line in (x.strip() for x in open(f).readlines()):
        if not line:
            if mode == 'rules':
                mode = 'my'
            else:
                mode = 'nearby'

            continue

        if mode == 'rules':
            m = re.match(r'^(.*?): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$', line).groups()
            rules[m[0]] = ((int(m[1]), int(m[2])), (int(m[3]), int(m[4])))
        elif mode == 'my' and line != 'your ticket:':
            my_ticket = tuple(map(int, line.split(',')))
        elif mode == 'nearby' and line != 'nearby tickets:':
            other_tickets.append(tuple(map(int, line.split(','))))

    valid_tickets.append(my_ticket)
    error_rate = 0
    invalid_ticket_fields = []
    valid_ticket_fields = []

    for _ in my_ticket:
        invalid_ticket_fields.append(set())
        valid_ticket_fields.append(set(rules.keys()))

    for tidx, ticket in enumerate(other_tickets):
        has_invalid_fields = False

        for vidx, val in enumerate(ticket):
            is_valid = False

            for name, rule in rules.items():
                if val < rule[0][0] or val > rule[1][1]:
                    continue
                elif rule[0][1] < val < rule[1][0]:
                    continue

                is_valid = True

            if not is_valid:
                has_invalid_fields = True
                error_rate += val

        if not has_invalid_fields:
            valid_tickets.append(ticket)

    for tidx, ticket in enumerate(valid_tickets):
        for vidx, val in enumerate(ticket):
            for name, rule in rules.items():
                if rule[0][0] <= val <= rule[0][1]:
                    continue
                elif rule[1][0] <= val <= rule[1][1]:
                    continue

                invalid_ticket_fields[vidx].add(name)

    for idx, s in enumerate(invalid_ticket_fields):
        valid_ticket_fields[idx] -= s

    changed = True

    while changed:
        changed = False

        for s in valid_ticket_fields:
            if len(s) == 1:
                my_value = next(iter(s))

                for s_i in valid_ticket_fields:
                    if len(s_i) > 1 and my_value in s_i:
                        s_i.remove(my_value)
                        changed = True

    values = []

    for idx, s in enumerate(valid_ticket_fields):
        field_name = next(iter(s))

        if field_name.startswith('departure'):
            values.append(my_ticket[idx])

    return {
        'error_rate': error_rate,
        'my_ticket_values': reduce(mul, values),
    }


def test_clickit_or_tickit():
    assert clickit_or_tickit('input/16.test')['error_rate'] == 71


if __name__ == '__main__':
    print(clickit_or_tickit('input/16'))
