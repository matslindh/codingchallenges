import json
from typing import List


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def __str__(self):
        return self.val + ', next: ' + id(self.next)


class FastList:
    def __init__(self, seq):
        self.node_map = {}

        prev = None
        n = None

        for s in seq:
            n = Node(s)
            self.node_map[s] = n

            if prev:
                prev.next = n
            else:
                self.root = n

            prev = n

        if n:
            n.next = self.root

    def node_from_val(self, val) -> Node:
        return self.node_map[val]

    def rotate(self) -> Node:
        current = self.root
        self.root = self.root.next
        return current

    def extract(self, current, next_count=3) -> List[Node]:
        nodes = []
        node = current

        for i in range(0, next_count):
            nodes.append(node.next)
            node = node.next

        current.next = node.next

        if self.root in nodes:
            self.root = current.next

        return nodes

    def insert(self, n: Node, nodes: List[Node]):
        old_next = n.next
        n.next = nodes[0]
        nodes[-1].next = old_next

    def print_seq(self):
        root = self.root
        n = self.root

        while n.next != root:
            print(n.val, end=' ')
            n = n.next


def play(cups, iterations=100):
    m = max(cups)
    fl = FastList(cups)
    
    while iterations:
        current = fl.rotate()
        extracted = fl.extract(current)
        extracted_labels = [n.val for n in extracted]
        current_label = current.val
        destination_node = None

        while True:
            current_label -= 1
            
            if current_label < 1:
                current_label = m

            if current_label in extracted_labels:
                continue

            destination_node = fl.node_from_val(current_label)
            break

        fl.insert(destination_node, extracted)
        iterations -= 1

        if iterations % 50000 == 0:
            print(iterations)

    return fl.node_from_val(1)


def order_after_one(n_in):
    vals = []
    n = n_in

    while n.next != n_in:
        vals.append(n.val)
        n = n.next

    vals.append(n.val)

    return vals[1:]


def test_play_and_order():
    cups = [int(x) for x in '389125467']    
    assert order_after_one(play(cups, 10)) == [int(x) for x in '92658374']

    cups = [int(x) for x in '389125467']
    assert order_after_one(play(cups)) == [int(x) for x in '67384529']


"""def test_play_v2():
    cups = [int(x) for x in '389125467']

    for i in range(10, 1000001):
        cups.append(i)

    play(cups, 1000000)
    assert False"""


if __name__ == '__main__':
    print(order_after_one(play([int(x) for x in '523764819'])))

    cups = [int(x) for x in '523764819']
    cups.extend(list(range(10, 1000001)))

    cups_test = [int(x) for x in '389125467']
    cups_test.extend(list(range(10, 1000001)))

    result = play(cups_test, 10000000)
    print(result.next.val, result.next.next.val, result.next.val * result.next.next.val)

    result = play(cups, 10000000)
    print(result.next.val, result.next.next.val, result.next.val * result.next.next.val)

"""
    cups = [int(x) for x in '389125467']
    cups.extend(list(range(10, 1000001)))

    result = play(cups, 1000000)
    r_idx = result.index(1)
    print(result[r_idx+1], result[r_idx+2], result[r_idx+1] * result[r_idx+2]) """

