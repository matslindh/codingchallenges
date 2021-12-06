def better_tree_parser(tree_description):
    depth = 0
    max_depth = 0
    name = ''
    names = []

    for char in tree_description:
        if char == '(':
            names.append(name)
            depth += 1 if name != 'Grinch' else 0
            name = ''
            max_depth = max(max_depth, depth)
        elif char == ')':
            name = names.pop()
            depth -= 1 if name != 'Grinch' else 0
        elif char == ' ':
            name = ''
        else:
            name += char

    return max_depth


def test_better_tree_parser():
    assert better_tree_parser('Aurora(Toralv(Grinch(Kari Robinalv) Alvborg) Grinch(Alva(Alve-Berit Anna) Grete(Ola Hans)))') == 2
    assert better_tree_parser('Aurora(Kari(Hans Kari) Hans(Hans Kari))') == 2


if __name__ == '__main__':
    print(better_tree_parser(open('input/05').read()))
