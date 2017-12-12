def build_graph(f):
    nodes = {}

    for line in open(f).readlines():
        _id, conn = [x.strip() for x in line.split('<->')]
        nodes[int(_id)] = {
            'id': _id,
            'links': [int(x.strip()) for x in conn.split(',')],
            'visited': False,
        }

    return nodes


def find_connected_nodes(f, idx):
    nodes = build_graph(f)
    queue = [nodes[idx]]

    while queue:
        n = queue.pop(0)

        if n['visited']:
            continue

        n['visited'] = True

        for l in n['links']:
            l_n = nodes[l]

            if not l_n['visited']:
                queue.append(l_n)

    c = 0

    for idx in nodes:
        if nodes[idx]['visited']:
            c += 1

    return c


def find_group_count(f, idx):
    nodes = build_graph(f)
    queue = [nodes[idx]]
    g_c = 0
    n_count = len(nodes)
    n_idx = 0

    while True:
        while queue:
            n = queue.pop(0)

            if n['visited']:
                continue

            n['visited'] = True

            for l in n['links']:
                l_n = nodes[l]

                if not l_n['visited']:
                    queue.append(l_n)

        g_c += 1

        while n_idx < n_count and nodes[n_idx]['visited']:
            n_idx += 1

        if n_idx == n_count:
            return g_c

        queue = [nodes[n_idx]]


def test_find_connected_nodes():
    assert 6 == find_connected_nodes('input/dec12_test', 0)


def test_find_group_count():
    assert 2 == find_group_count('input/dec12', 0)


if __name__ == "__main__":
    print(find_connected_nodes('input/dec12', 0))
    print(find_group_count('input/dec12', 0))
