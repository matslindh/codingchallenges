def evaluate_orbits(orbit_lines):
    struct = build_orbit_structure(orbit_lines)
    return count_orbits(struct)


def count_orbit_transfers(orbit_lines):
    orbit_struct = build_orbit_structure(orbit_lines)

    orbit_queue = [(orbit_struct['YOU'], -1)]

    while orbit_queue:
        orbiter, depth = orbit_queue.pop(0)

        if orbiter['name'] == 'SAN':
            return depth - 1

        orbiter['visited'] = True

        for orbitee in orbiter['orbiters']:
            if not orbitee.get('visited'):
                orbit_queue.append((orbitee, depth+1))

        if orbiter.get('parent') and not orbiter['parent'].get('visited'):
            orbit_queue.append((orbiter['parent'], depth+1))

    return None


def count_orbits(orbit_struct):
    orbit_queue = [(orbit_struct['COM'], 0)]
    total = 0

    while orbit_queue:
        orbiter, depth = orbit_queue.pop(0)

        if depth:
            total += depth

        for orbitee in orbiter['orbiters']:
            orbit_queue.append((orbitee, depth+1))

    return total


def build_orbit_structure(lines):
    objects = {}

    for line in lines:
        orbiter, orbitee = line.split(')')

        if orbiter not in objects:
            objects[orbiter] = {
                'name': orbiter,
                'orbiters': [],
                'parent': None,
            }

        if orbitee not in objects:
            objects[orbitee] = {
                'name': orbitee,
                'orbiters': [],
                'parent': objects[orbiter],
            }

        if not objects[orbitee].get('parent'):
            objects[orbitee]['parent'] = objects[orbiter]

        objects[orbiter]['orbiters'].append(objects[orbitee])

    return objects


def test_evalute_orbits():
    assert 42 == evaluate_orbits([o.strip() for o in open('input/06.test').readlines()])


def test_count_orbit_transfers():
    assert 4 == count_orbit_transfers([o.strip() for o in open('input/06b.test').readlines()])


if __name__ == '__main__':
    print(evaluate_orbits([o.strip() for o in open('input/06').readlines()]))
    print(count_orbit_transfers([o.strip() for o in open('input/06').readlines()]))