from math import floor


def score_syntax_errors(program_lines):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    s = 0
    scores_auto = []

    for line in program_lines:
        corrupted, stack = corrupted_character(line)

        if corrupted:
            s += points[corrupted]
        else:
            scores_auto.append(score_autocomplete(stack))

    return s, sorted(scores_auto)[floor(len(scores_auto)/2)]


def corrupted_character(inp):
    stack = []
    lookup = {'(': ')', '[': ']', '{': '}', '<': '>'}
    lookup_close = {v: k for k, v in lookup.items()}

    def stack_converter(st):
        return [lookup[element] for element in st[::-1]]

    for char in inp:
        if char in lookup:
            stack.append(char)
        elif char in lookup_close:
            expected = stack.pop()

            if expected != lookup_close[char]:
                return char, stack_converter(stack)
        else:
            print(f"INVALID {char}")

    return None, stack_converter(stack)


def score_autocomplete(stack):
    points_autocomplete = {')': 1, ']': 2, '}': 3, '>': 4}
    s_auto = 0

    for char in stack:
        s_auto *= 5
        s_auto += points_autocomplete[char]

    return s_auto


def test_corrupted_character():
    assert corrupted_character('{([(<{}[<>[]}>{[]{[(<()>')[0] == '}'
    assert corrupted_character('[[<[([]))<([[{}[[()]]]')[0] == ')'
    assert corrupted_character('[{[{({}]{}}([{[{{{}}([]')[0] == ']'
    assert corrupted_character('[<(<(<(<{}))><([]([]()')[0] == ')'
    assert corrupted_character('<{([([[(<>()){}]>(<<{{')[0] == '>'


def test_score_syntax_errors():
    assert score_syntax_errors(open('input/10.test').read().splitlines()) == (26397, 288957)


def test_corrupted_character_stack():
    assert corrupted_character('[({(<(())[]>[[{[]{<()<>>')[1] == ['}', '}', ']', ']', ')', '}', ')', ']']


def test_scoring_autocomplete():
    assert score_autocomplete('}}]])})]') == 288957
    assert score_autocomplete(')}>]})') == 5566
    assert score_autocomplete('}}>}>))))') == 1480781


if __name__ == '__main__':
    print(score_syntax_errors(open('input/10').read().splitlines()))
