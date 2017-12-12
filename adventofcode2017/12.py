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


def find_counts(f, idx):
    nodes = build_graph(f)
    queue = [nodes[idx]]
    g_c = 0
    n_count = len(nodes)
    n_idx = 0
    first_count = 0

    while True:
        while queue:
            n = queue.pop(0)

            if n['visited']:
                continue

            if g_c == 0:
                first_count += 1

            n['visited'] = True

            for l in n['links']:
                l_n = nodes[l]

                if not l_n['visited']:
                    queue.append(l_n)

        g_c += 1

        while n_idx < n_count and nodes[n_idx]['visited']:
            n_idx += 1

        if n_idx == n_count:
            break

        queue = [nodes[n_idx]]

    return first_count, g_c


def test_find_counts():
    assert (6, 2) == find_counts('input/dec12_test', 0)


if __name__ == "__main__":
    print(find_counts('input/dec12', 0))
