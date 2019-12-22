def tree_heights(f):
    lines = open(f).readlines()
    
    last = len(lines) - 1
    heights = []

    for idx, c in enumerate(lines[last]):
        if c == '#':
            y = last
            ch = lines[y][idx]
            
            while ch == '#' and y >= 0:
                y -= 1
                ch = lines[y][idx]
                
            heights.append(last - y)

    return list(map(lambda x: round(x * 0.2, 1), heights))


def tree_values(inp):
    return sum(tree_heights(inp)) * 200


def test_tree_heights():
    assert [4, 2.4, 4.2] == tree_heights('input/forest.test.txt')


def test_tree_values():
    assert 2120 == round(tree_values('input/forest.test.txt'))


if __name__ == '__main__':
    print(tree_values('input/forest.txt'))
