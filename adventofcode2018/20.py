class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.N = None
        self.W = None
        self.E = None
        self.S = None
        self.visited = False
        self.distance = None

    def __str__(self):
        return str({'n': (self.x, self.y), 'W': (self.W.x, self.W.y) if self.W else None, 'E': (self.E.x, self.E.y) if self.E else None, 'N': (self.N.x, self.N.y) if self.N else None, 'S': (self.S.x, self.S.y) if self.S else None})


def k(n):
    return str(n.x) + ',' + str(n.y)


def build_graph(s):
    s = list(s[1:-1])

    nodes_by_coordinate = {}

    def process_node(node, s):
        print(" down ")
        i = 0
        calling_node = node
        nodes = {k(node): node}
        exit_nodes = {}

        while i < len(s):
            c = s[i]

            if c == '(':
                process = dict(nodes)
                nodes = {}

                for _, n in process.items():
                    skip, exit_nodes = process_node(n, s[i+1:])

                    for _, n in exit_nodes.items():
                        nodes[k(n)] = n

                i += skip
                print(len(nodes))
                #print("returned, continuing processing of ", s[i+1:])
                #print([str(n) for n in exit_nodes])
            elif c == '|':
                #print("this time we got to", nodes)
                exit_nodes.update(nodes)
                nodes = {k(calling_node): calling_node}
            elif c == ')':
                exit_nodes.update(nodes)
                return i + 1, exit_nodes
            else:
                new_nodes = {}

                for _, n in nodes.items():
                    #print("working with", (n.x, n.y))
                    x = n.x
                    y = n.y

                    if c == 'W':
                        x -= 1
                    elif c == 'E':
                        x += 1
                    elif c == 'N':
                        y += 1
                    elif c == 'S':
                        y -= 1

                    coord = str(x) + ',' + str(y)

                    if coord not in nodes_by_coordinate:
                        nodes_by_coordinate[coord] = Node(x, y)

                    next_node = nodes_by_coordinate[coord]

                    if c == 'W':
                        n.W = next_node
                        next_node.E = n
                    elif c == 'E':
                        n.E = next_node
                        next_node.W = n
                    elif c == 'N':
                        n.N = next_node
                        next_node.S = n
                    elif c == 'S':
                        n.S = next_node
                        next_node.N = n

                    new_nodes[k(n)] = next_node

                nodes = new_nodes

            i += 1

        return

    n_init = Node(0, 0)
    nodes_by_coordinate['0,0'] = n_init
    process_node(n_init, s)

    return n_init


def longest_path(s):
    queue = [(build_graph(s), 0, None)]
    last_distance = 0
    m = {}
    over_1000 = 0

    while queue:
        n, distance, f = queue.pop(0)

        if distance >= 1000:
            over_1000 += 1

        if n.y not in m:
            m[n.y] = {}

        m[n.y][n.x] = n
        #print(distance, (n.x, n.y), (f.x, f.y) if f else None, n)
        last_distance = distance
        n.visited = True

        if n.W and not n.W.visited:
            queue.append((n.W, distance+1, n))

        if n.E and not n.E.visited:
            queue.append((n.E, distance+1, n))

        if n.N and not n.N.visited:
            queue.append((n.N, distance+1, n))

        if n.S and not n.S.visited:
            queue.append((n.S, distance+1, n))

    #print_map(m)
    return last_distance, over_1000


def print_map(m):
    for y in range(-10, 10):
        for x in range(-10, 10):
            if y in m and x in m[y]:
                c = '.'

                if m[y][x].W and m[y][x].E and m[y][x].N and m[y][x].S:
                    c = 'x'
                elif m[y][x].W and m[y][x].E:
                    c = '-'
                elif m[y][x].N and m[y][x].S:
                    c = '|'
                elif m[y][x].N and m[y][x].E:
                    c = '/'
                elif m[y][x].N and m[y][x].W:
                    c = '\\'

                print(c, end='')
            else:
                print('#', end='')

        print()


def test_longest_path():
    assert longest_path('^WNE$') == 3
    assert longest_path('^WN(E|WW)NEE$') == 7
    assert longest_path('^ENWWW(NEEE|SSE(EE|N))$') == 10
    assert longest_path('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$') == 18


if __name__ == '__main__':
    print(longest_path(open('input/20').read().strip()))