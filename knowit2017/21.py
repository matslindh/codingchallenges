class Node:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.enemies = []
        self.visited = False

    def enemy(self, node):
        self.enemies.append(node)
        node.enemies.append(self)

    def friend(self, node):
        self.friends.append(node)
        node.friends.append(self)

    def __repr__(self):
        return str((self.name, self.friends, self.enemies))


def count_friends_and_enemies(lines):
    nodes = {
        'me': Node('Me'),
        'Asgeir': Node('Asgeir'),
        'Beate': Node('Beate'),
    }

    nodes['me'].friend(nodes['Asgeir'])
    nodes['me'].enemy(nodes['Beate'])

    for line in lines:
        rule, p1, p2 = line.strip().split(' ')

        if p1 not in nodes:
            nodes[p1] = Node(p1)

        if p2 not in nodes:
            nodes[p2] = Node(p2)

        if rule == 'vennskap':
            nodes[p1].friend(nodes[p2])

        elif rule == 'fiendskap':
            nodes[p1].enemy(nodes[p2])

    queue = [
        (nodes['me'], True)
    ]

    counts = {
        'friends': 0,
        'enemies': 0
    }

    while queue:
        node, friend = queue.pop(0)

        if node.visited:
            continue

        node.visited = True

        if node.name != 'Me':
            counts['friends' if friend else 'enemies'] += 1

        for n in node.friends:
            queue.append((n, friend))

        for n in node.enemies:
            queue.append((n, not friend))

    neutral = 0

    for k in nodes:
        if not nodes[k].visited:
            neutral += 1

    return counts['friends'], counts['enemies'], neutral


def test_count_friends_and_enemies():
    assert (4, 5, 2) == count_friends_and_enemies(open('input/dec21_test').readlines())


if __name__ == "__main__":
    print(count_friends_and_enemies(open("input/dec21").readlines()))