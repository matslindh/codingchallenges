from lark import (
    Lark,
    Transformer,
    v_args,
)

@v_args(inline=True)
class Calculator(Transformer):
    def add(self, left, right):
        return int(left) + int(right)

    def mul(self, left, right):
        return int(left) * int(right)

    def sum(self, val):
        return val

    def number(self, val):
        return val


parser_v1 = Lark("""
    sum: item
       | sum "+" item        -> add
       | sum "*" item  -> mul

    ?item: NUMBER               
         | "(" sum ")"          -> number

    %import common.NUMBER
    %import common.WS
    %ignore WS  
""", start='sum', parser='lalr', transformer=Calculator())

parser_v2 = Lark("""
    ?sum: addlifier
        | sum "*" addlifier          -> mul
       
    ?addlifier: item
              | addlifier "+" item   -> add

    ?item: NUMBER               
         | "(" sum ")"               -> number

    %import common.NUMBER
    %import common.WS
    %ignore WS  
""", start='sum', parser='lalr', transformer=Calculator())


def calculator_parser(expr, parser=parser_v1):
    return parser.parse(expr)


def test_calculator():
    assert calculator_parser('1 + 2 * 3 + 4 * 5 + 6') == 71
    assert calculator_parser('1 + (2 * 3)') == 7
    assert calculator_parser('1 + 2 * 3') == 9

    assert calculator_parser('1 + 2 * 3 + 4 * 5 + 6', parser=parser_v2) == 231
    assert calculator_parser('1 + 2 * 3', parser=parser_v2) == 9


if __name__ == '__main__':
    c = 0
    c2 = 0

    for line in [x.strip() for x in open('input/18')]:
        c += calculator_parser(line)
        c2 += calculator_parser(line, parser=parser_v2)

    print(c, c2)
