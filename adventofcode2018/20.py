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


def build_graph(s):
    s = list(s[1:-1])

    nodes_by_coordinate = {}

    def process_node(node, x, y, s):
        print("processing ", x, y, s)
        i = 0
        calling = [x, y, node]

        while i < len(s):
            c = s[i]
            print("at", x, y, c)

            if c == '(':
                i += process_node(node, x, y, s[i+1:])
                print("got back")
            elif c == '|':
                x, y, node = calling
            elif c == ')':
                return i + 1
            else:
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

                dest_node = nodes_by_coordinate[coord]
                # print(coord, node, dest_node)

                if c == 'W':
                    node.W = dest_node
                    dest_node.E = node
                elif c == 'E':
                    node.E = dest_node
                    dest_node.W = node
                elif c == 'N':
                    node.N = dest_node
                    dest_node.S = node
                elif c == 'S':
                    node.S = dest_node
                    dest_node.N = node

                node = dest_node

            i += 1

        return i

    n = Node(0, 0)
    nodes_by_coordinate['0,0'] = n
    process_node(n, 0, 0, s)

    return n


def longest_path(s):
    queue = [(build_graph(s), 0)]
    last_distance = 0

    while queue:
        n, distance = queue.pop(0)
        print(distance, n)
        last_distance = distance
        n.visited = True

        if n.W and not n.W.visited:
            queue.append((n.W, distance+1))

        if n.E and not n.E.visited:
            queue.append((n.E, distance+1))

        if n.N and not n.N.visited:
            queue.append((n.N, distance+1))

        if n.S and not n.S.visited:
            queue.append((n.S, distance+1))

    return last_distance


def test_longest_path():
    assert longest_path('^WNE$') == 3
    assert longest_path('^WN(E|WW)NEE$') == 8
    assert longest_path('^ENWWW(NEEE|SSE(EE|N))$') == 10
    assert longest_path('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$') == 18