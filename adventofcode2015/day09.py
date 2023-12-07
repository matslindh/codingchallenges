from collections import defaultdict


end_dists = []


def distances(lines):
    dists = defaultdict(dict)

    for line in lines:
        city1, _, city2, _, distance = line.split()
        dists[city1][city2] = int(distance)
        dists[city2][city1] = int(distance)

    return dists


def recurse(current, distance, visited: set):
    visited.add(current)

    if len(visited) == len(dists):
        end_dists.append(distance)

    for dest, dist in dists[current].items():
        if dest in visited:
            continue

        recurse(dest, distance + dist, visited=visited)

    visited.remove(current)

dists = distances(open("input/09").read().splitlines())

for start in dists.keys():
    recurse(start, 0, set())

print(min(end_dists), max(end_dists))