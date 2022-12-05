from pytest import fixture


def get_movement_instructions(lines):
    in_instructions = False
    instructions = []

    for line in lines:
        if not line.strip():
            in_instructions = True
            continue

        if not in_instructions:
            continue

        _, units, _, from_, _, to = line.split(' ')
        instructions.append((int(units), int(from_), int(to)))

    return instructions


def get_stacks(lines):
    stack_lines = []
    stacks = []

    for line in lines:
        if not line.strip():
            stack_lines.pop(0)
            break

        stack_lines.insert(0, line)

    step_size = 4

    for line in stack_lines:
        for idx in range(1, len(line), step_size):
            if line[idx] == ' ':
                continue

            pos = (idx - 1) // step_size

            while len(stacks) <= pos:
                stacks.append([])

            stacks[pos].append(line[idx])

    return stacks


def move_stacks_from_file(path):
    lines = open(path).read().splitlines()
    stacks = get_stacks(lines)
    instructions = get_movement_instructions(lines)

    for units, from_, to in instructions:
        for _ in range(units):
            stacks[to - 1].append(stacks[from_ - 1].pop())

    return ''.join([stack[-1] for stack in stacks])


def make_cratemover_9001_with_cupholder_work(path):
    lines = open(path).read().splitlines()
    stacks = get_stacks(lines)
    instructions = get_movement_instructions(lines)

    for units, from_, to in instructions:
        stacks[to - 1].extend(stacks[from_ - 1][-units:])
        stacks[from_ - 1] = stacks[from_ - 1][:-units]

    return ''.join([stack[-1] for stack in stacks])

@fixture
def test_lines():
    return open('input/05.test').read().splitlines()


def test_get_stacks(test_lines):
    assert get_stacks(test_lines) == [['Z', 'N'], ['M', 'C', 'D'], ['P']]


def test_get_movement_instructions(test_lines):
    assert get_movement_instructions(test_lines) == [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]


def test_move_stacks_from_file():
    assert move_stacks_from_file('input/05.test') == 'CMZ'


def test_cratemover_9001_from_file():
    assert make_cratemover_9001_with_cupholder_work('input/05.test') == 'MCD'


if __name__ == '__main__':
    print(move_stacks_from_file('input/05'))
    print(make_cratemover_9001_with_cupholder_work('input/05'))
