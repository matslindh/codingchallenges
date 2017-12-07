import re
import collections


def build_tree(lines):
    nodes = {}

    for line in lines:
        line = line.strip()

        obj = re.search(r'(?P<node>[a-z]+) \((?P<weight>[0-9]+)\)(?P<links> -> .*)?', line).groupdict()

        nodes[obj['node']] = {
            'name': obj['node'],
            'weight': int(obj['weight']),
            'total_weight': 0,
            'links': [],
            'parent': None,
            'linksDescription': obj['links'],
        }

    for nodek in nodes:
        node = nodes[nodek]

        if node['linksDescription']:
            ids = node['linksDescription'][4:].split(', ')

            for _id in ids:
                node['links'].append(nodes[_id])
                nodes[_id]['parent'] = node

    return nodes


def find_root_node(nodes):
    for nodek in nodes:
        if not nodes[nodek]['parent']:
            return nodes[nodek]['name']


def find_wrong_weight(nodes):
    root = find_root_node(nodes)
    wrong_in = None

    def weigh_nodes(node):
        nonlocal wrong_in

        if not node['total_weight'] and node['links']:
            total_weight = node['weight']
            weight = None
            wrong_level = False

            for link in node['links']:
                this_weight = weigh_nodes(link)

                if not weight:
                    weight = this_weight
                elif weight != this_weight:
                    wrong_level = True

                total_weight += this_weight

            if wrong_level and not wrong_in:
                wrong_in = [(n['total_weight'], n['weight'], n['name']) for n in node['links']]

            node['total_weight'] = total_weight
        elif not node['links']:
            node['total_weight'] = node['weight']

        return node['total_weight']

    weigh_nodes(nodes[root])

    c = collections.Counter([w[0] for w in wrong_in])
    wrong = 0
    correct = 0

    for val in c:
        if c[val] == 1:
            wrong = val
        else:
            correct = val

    for node in wrong_in:
        if node[0] == wrong:
            diff = wrong - correct
            return node[1] - diff


def test_find_root_node():
    assert 'tknk' == find_root_node(build_tree(open('input/dec07_test').readlines()))


def test_find_wrong_weight():
    assert 60 == find_wrong_weight(build_tree(open('input/dec07_test').readlines()))


if __name__ == "__main__":
    print(find_root_node(build_tree(open('input/dec07').readlines())))
    print(find_wrong_weight(build_tree(open('input/dec07').readlines())))
