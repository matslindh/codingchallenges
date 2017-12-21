def expand(rules, iterations):
    drawing = ['.#.', '..#', '###']

    for i in range(0, iterations):
        new_map = []
        
        step = 2 if len(drawing) % 2 == 0 else 3

        for offset_y in range(0, len(drawing), step):
            line = []
            
            for offset_x in range(0, len(drawing), step):
                segment = []

                for y in range(offset_y, offset_y+step):
                    segment.append(drawing[y][offset_x:offset_x+step])

                n = rules[ser(segment)]
                
                if not line:
                    line += n
                else:
                    for idx, row in enumerate(n):
                        line[idx] += row

            new_map += line

        drawing = new_map

    return drawing


def ser(p):
    return '/'.join(p)


def parse_rules(lines):
    expanders = {}

    for line in lines:
        pattern, replacement = line.strip().split(' => ')
        pattern = pattern.split('/')
        replacement = replacement.split('/')

        expanders[ser(pattern)] = replacement
        expanders[ser(flip(pattern))] = replacement
        
        for _ in range(0, 3):
            pattern = rotate(pattern)
            expanders[ser(pattern)] = replacement
            expanders[ser(flip(pattern))] = replacement

    return expanders


def rotate(p):
    output = []
    
    for x in range(len(p[0]) - 1, -1, -1):
        line = ''

        for y in range(0, len(p)):
            line += p[y][x]
            
        output.append(line)

    return output


def flip(p):
    return list(reversed(p))


def count_on(drawing):
    c = 0

    for y in range(0, len(drawing)):
        for x in range(0, len(drawing[y])):
            if drawing[y][x] == '#':
                c += 1   

    return c


def print_drawing(drawing):
    for line in drawing:
        print(line)

    print('')


def test_rotate():
    assert ['#.', '#.'] == rotate(['##', '..'])


def test_flip():
    assert ['#.', '.#'] == flip(['.#', '#.'])

    
def test_count_on():
    assert 2 == count_on(['.#', '.#'])


def test_parse_rules():
    assert {
        '../.#': ['##.', '#..', '...'],
        '#./..': ['##.', '#..', '...'],
        '.#/..': ['##.', '#..', '...'],
        '../#.': ['##.', '#..', '...'],
    } == parse_rules(['../.# => ##./#../...'])

    
def test_problem():
    assert 12 == count_on(expand(parse_rules(open("input/dec21_test").readlines()), 2))

if __name__ == "__main__":
    print(count_on(expand(parse_rules(open("input/dec21").readlines()), 5)))
    print(count_on(expand(parse_rules(open("input/dec21").readlines()), 18)))


