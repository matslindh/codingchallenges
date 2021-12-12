from string import ascii_lowercase


def count_distinct_paths(connections, max_small_visits=1):
    nodes = {}

    def initialize_node(name):
        small = name[0] in ascii_lowercase

        nodes[name] = {
            'name': name,
            'connected_to': set(),
            'visited': 0,
            'small': small
        }

    for connection in connections:
        source, destination = connection.split('-')

        if source not in nodes:
            initialize_node(source)

        if destination not in nodes:
            initialize_node(destination)

        nodes[source]['connected_to'].add(destination)
        nodes[destination]['connected_to'].add(source)

    paths = set()

    def explore(path, current, allow_double=None):
        node = nodes[current]

        if current == 'end':
            paths.add(','.join(path))
            return

        path.append(current)

        if node['small']:
            node['visited'] += 1

        # recurse
        for child in node['connected_to']:
            if child == 'start':
                continue

            if (nodes[child]['visited'] and child != allow_double) or nodes[child]['visited'] > 1:
                continue

            explore(path, child, allow_double=allow_double)

        if node['small']:
            node['visited'] -= 1

        path.pop()

    if max_small_visits > 1:
        for lowercase_node in filter(lambda x: nodes[x]['small'], nodes):
            explore([], 'start', allow_double=lowercase_node)
    else:
        explore([], 'start')

    return len(paths)


def test_count_distinct_paths():
    assert count_distinct_paths(open('input/12.test').read().splitlines()) == 10
    assert count_distinct_paths(open('input/12.test2').read().splitlines()) == 19
    assert count_distinct_paths(open('input/12.test3').read().splitlines()) == 226


def test_count_distinct_paths_allow_doubles():
    assert count_distinct_paths(open('input/12.test').read().splitlines(), max_small_visits=2) == 36
    assert count_distinct_paths(open('input/12.test2').read().splitlines(), max_small_visits=2) == 103
    assert count_distinct_paths(open('input/12.test3').read().splitlines(), max_small_visits=2) == 3509


if __name__ == '__main__':
    print(count_distinct_paths(open('input/12').read().splitlines()))
    print(count_distinct_paths(open('input/12').read().splitlines(), max_small_visits=2))


"""
start [visited: 1]
    -> A ['start']
        -> start -> visited, skip
        -> c ['start', 'A'] [visited: 1]
            -> 'A' ['start', 'A', 'c']
                -> start -> visited, skip
                -> c -> visited, skip
                -> b -> ....
                -> end -> ['start', 'A', 'c', 'A'] => DONE, add to paths
                [pop(a)]
           [visited: 0, pop(c)] 
        -> b ['start', 'A'] [visited: 1]
            -> d ['start', 'A', 'b'] [visited: 1]
                stopper..
            -> start -> visited, skip
            -> end -> ['start', 'A', 'b'] => Done, add to paths
            [visited: 0, pop(b)]
        -> end -> ['start', 'A'] => Done, add to paths
    -> b ['start'] [visited: 1]
        -> d ['start', 'b'] [visited: 1]
            stopper..
        -> start -> visited, skip
        -> end -> ['start', 'b'] => Done, add to paths

"""