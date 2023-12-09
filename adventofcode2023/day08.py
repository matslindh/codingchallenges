
def parse_lines(lines):
    nodes = {}

    for line in lines[2:]:
        source, entries = line.split(" = ")
        left, right = entries[1:-1].split(", ")

        nodes[source] = (left, right)

    return {
        "instructions": lines[0],
        "nodes": nodes,
    }

def navigate(network):
    moves = 0
    node = 'AAA'
    instr_num = len(network['instructions'])

    while node != 'ZZZ':
        instr = network['instructions'][moves % instr_num]

        node = network['nodes'][node][0 if instr == 'L' else 1]
        moves += 1

    return moves


def navigate_parallel(network):
    moves = 0
    nodes = {
        node: {
            "moves": 0,
            "current": node,
            "finishes_at": set(),
        }
        for node in network['nodes'].keys() if node[-1] == 'A'
    }

    instr_num = len(network['instructions'])

    while True:
        instr = network['instructions'][moves % instr_num]

        for node, node_data in nodes.items():
            node_data['current'] = network["nodes"][node_data['current']][0 if instr == 'L' else 1]
            node_data['moves'] += 1

            if node_data['current'][-1] == 'Z':
                node_data['finishes_at'].add(moves)

        moves += 1

        if moves > 50000:
            break

    pass


def test_navigate_parallel():
    assert navigate_parallel(parse_lines(open("input/08.test3").read().splitlines())) == 6


def test_navigate():
    assert navigate(parse_lines(open("input/08.test").read().splitlines())) == 2
    assert navigate(parse_lines(open("input/08.test2").read().splitlines())) == 6, "Failed looping instruction set"


def test_parse_lines():
    assert parse_lines(open("input/08.test").read().splitlines()) == {"instructions": "RL", "nodes": {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }}


if __name__ == "__main__":
    print(navigate_parallel(parse_lines(open("input/08").read().splitlines())))
    print(navigate(parse_lines(open("input/08").read().splitlines())))