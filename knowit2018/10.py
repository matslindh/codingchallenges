from math import floor


def execute(ops):
    stack = []
    skip_until_newline = False

    for op in ops:
        if skip_until_newline:
            if op == "\n":
                skip_until_newline = False

            continue

        if op == ' ':
            stack.append(31)
        elif op == '|':
            stack.append(3)
        elif op == ':':
            stack = [sum(stack)]
        elif op == '\'':
            stack.append(stack.pop() + stack.pop())
        elif op == '.':
            a = stack.pop()
            b = stack.pop()
            stack.append(a - b)
            stack.append(b - a)
        elif op == '_':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
            stack.append(a)
        elif op == '/':
            stack.pop()
        elif op == 'i':
            stack.append(stack[-1])
        elif op == '\\':
            stack[-1] += 1
        elif op == '*':
            stack.append(int(floor(stack.pop() / stack.pop())))
        elif op == ']':
            v = stack.pop()

            if v % 2 == 0:
                stack.append(1)
        elif op == '[':
            v = stack.pop()

            if v % 2 == 1:
                stack.append(v)
        elif op == '~':
            stack.append(max(stack.pop(), stack.pop(), stack.pop()))
        elif op == 'K':
            skip_until_newline = True

    return max(stack)


def test_execute():
    assert execute('|||:') == 9


if __name__ == '__main__':
    print(execute(open('input/10.spp').read()))