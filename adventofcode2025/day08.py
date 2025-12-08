from common import rs
from operator import mul
from functools import reduce


def make_circuits(path, connections=1000):
    circuits = []
    node_circuit = {}

    nodes = []

    for line in rs(path):
        x, y, z = line.split(',')
        nodes.append((int(x), int(y), int(z)))

    distances = []

    for n1_idx, n1 in enumerate(nodes):
        circuits.append({n1})
        node_circuit[n1] = n1_idx

        for n2 in nodes[n1_idx + 1:]:
            d = (n2[0] - n1[0])**2 + (n2[1] - n1[1])**2 + (n2[2] - n1[2])**2
            distances.append((d, n1, n2))

    last_n1, last_n2 = None, None

    for d, n1, n2 in sorted(distances)[:connections]:
        if node_circuit[n1] == node_circuit[n2]:
            continue

        move_from_circuit = node_circuit[n2]

        for n in circuits[move_from_circuit]:
            node_circuit[n] = node_circuit[n1]
            circuits[node_circuit[n1]].add(n)

        circuits[move_from_circuit] = set()
        last_n1, last_n2 = n1, n2

    return reduce(
        mul,
        (
            len(circuit)
            for circuit in sorted(circuits, key=lambda circuit: len(circuit), reverse=True)[:3]
        )
    ), last_n1[0] * last_n2[0]


def test_make_circuits():
    assert make_circuits('input/08.test', connections=10)[0] == 40
    assert make_circuits('input/08.test', connections=100000)[1] == 25272


if __name__ == '__main__':
    print(make_circuits('input/08'))
    print(make_circuits('input/08', 1000000))
