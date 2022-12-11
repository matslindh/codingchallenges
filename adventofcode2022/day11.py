def monkey_parser(s):
    lines = s.splitlines()

    holding = list(map(int, lines[1][18:].split(', ')))
    operation = lines[2][19:]
    divisible_by = int(lines[3][21:])
    true_to = int(lines[4][29:])
    false_to = int(lines[5][30:])

    return {
        'holding': holding,
        'operation': operation,
        'divisible_by': divisible_by,
        'true_to': true_to,
        'false_to': false_to,
        'inspection_count': 0,
    }


def operation_evaluator(old, expr, divider):
    v1, op, v2 = expr.split()

    v1 = int(v1) if v1 != 'old' else old
    v2 = int(v2) if v2 != 'old' else old

    if op == '*':
        return (v1 * v2) % divider
    elif op == '+':
        return v1 + v2
    else:
        raise ValueError('Invalid operator')


def monkey_business_level(path, rounds=20, div_by=3):
    monkeys = []
    factors = 1

    with open(path) as f:
        for monkey_string in f.read().split("\n\n"):
            monkeys.append(monkey_parser(monkey_string))
            factors *= monkeys[-1]['divisible_by']

    for round_idx in range(rounds):
        for monkey in monkeys:
            monkey['inspection_count'] += len(monkey['holding'])

            for item in monkey['holding']:
                new_item = operation_evaluator(item, monkey['operation'], factors)

                if div_by > 1:
                    new_item //= div_by

                if new_item % monkey['divisible_by'] == 0:
                    monkeys[monkey['true_to']]['holding'].append(new_item)
                else:
                    monkeys[monkey['false_to']]['holding'].append(new_item)

            monkey['holding'] = []

        pass

    inspection_monkeys = sorted(monkeys, key=lambda m: m['inspection_count'], reverse=True)
    return inspection_monkeys[0]['inspection_count'] * inspection_monkeys[1]['inspection_count']


def test_monkey_business_level():
    assert monkey_business_level('input/11.test') == 10605


def test_monkey_business_level_its_real_now():
    assert monkey_business_level('input/11.test', rounds=10000, div_by=1) == 2713310158


def test_monkey_parser():
    assert monkey_parser("""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3""") == {
        'holding': [79, 98],
        'operation': 'old * 19',
        'divisible_by': 23,
        'true_to': 2,
        'false_to': 3,
        'inspection_count': 0,
    }


def test_operation_evaluator():
    assert operation_evaluator(79, 'old * 19') == 1501
    assert operation_evaluator(79, 'old + old') == 158


if __name__ == '__main__':
    print(monkey_business_level('input/11'))
    print(monkey_business_level('input/11', rounds=10000, div_by=1))