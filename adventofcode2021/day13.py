from collections import defaultdict


def code_cracker_4000(lines, max_instructions=1):
    paper = set()
    instructions = []
    in_instructions = False

    for line in lines:
        if not line:
            in_instructions = True
            continue

        if not in_instructions:
            x, y = map(int, line.split(','))
            paper.add((x, y))
        else:
            instructions.append(line)

    for idx, instruction in enumerate(instructions):
        if idx >= max_instructions:
            break

        direction_str, along = instruction.split('=')
        direction = direction_str[-1]
        along = int(along)

        if direction == 'x':
            paper = flip_set_x(paper, along)
        elif direction == 'y':
            paper = flip_set_y(paper, along)
        else:
            print(f"INVALID DIRECTION {direction}")

    return paper


def flip_set_y(paper, along):
    new_paper = set()

    for x, y in paper:
        if y > along:
            new_paper.add((x, along - abs(along - y)))
        elif y < along:
            new_paper.add((x, y))

    return new_paper


def flip_set_x(paper, along):
    new_paper = set()

    for x, y in paper:
        if x > along:
            new_paper.add((along - abs(along - x), y))
        elif x < along:
            new_paper.add((x, y))

    return new_paper


def print_paper(coords):
    width = max([x for x, y in coords])
    height = max([y for x, y in coords])

    for y in range(height + 1):
        for x in range(width + 1):
            print('X' if (x, y) in coords else ' ', end='')

        print('')


def test_code_cracker_4000():
    assert len(code_cracker_4000(open('input/13.test').read().splitlines())) == 17


if __name__ == '__main__':
    print(len(code_cracker_4000(open('input/13').read().splitlines())))
    paper = code_cracker_4000(open('input/13').read().splitlines(), max_instructions=99999)
    print_paper(paper)
