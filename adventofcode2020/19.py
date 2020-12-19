import re

from lark import (
    Lark,
)

from lark.exceptions import (
    UnexpectedCharacters,
    UnexpectedEOF,
)


def parse_file(f):
    parser_text = []
    inp = []
    mode = 'parser'

    for line in [x.strip() for x in open(f)]:
        if mode == 'parser':
            if not line:
                mode = 'input'
                continue

            parser_text.append(re.sub(r'([0-9]+)', r'rule_\1', line).replace('rule_0:', 'rule:'))
        else:
            inp.append(line)

    return {
        'parser': parser_text,
        'input': inp,
    }


def count_valid_from_parser(data, replace=False):
    if replace:
        for idx, line in enumerate(data['parser']):
            if line == 'rule_8: rule_42':
                data['parser'][idx] = 'rule_8: rule_42 | rule_42 rule_8'
            elif line == 'rule_11: rule_42 rule_31':
                data['parser'][idx] = 'rule_11: rule_42 rule_31 | rule_42 rule_11 rule_31'

    parser = Lark("\n".join(data['parser']) + """
    
        %import common.WS
        %ignore WS  
    """, start='rule')

    c = 0

    for line in data['input']:
        try:
            parser.parse(line)
            c += 1
        except UnexpectedCharacters:
            continue
        except UnexpectedEOF:
            continue

    return c


def test_count_valid_from_parser():
    data = parse_file('input/19.test')
    assert count_valid_from_parser(data) == 2


def test_count_valid_with_replacement():
    data = parse_file('input/19-2.test')
    assert count_valid_from_parser(data) == 3
    assert count_valid_from_parser(data, replace=True) == 12


if __name__ == '__main__':
    data = parse_file('input/19')
    print(count_valid_from_parser(data))
    print(count_valid_from_parser(data, replace=True))
