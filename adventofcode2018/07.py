from heapq import heappush, heappop, heapify


def assembly_instructions(f):
    steps = {}
    deps = {}
    seen = {}

    for s in f.readlines():
        parts = s.strip().split()
        finished = parts[1]
        step = parts[7]
        seen[step] = True
        seen[finished] = True

        if step not in steps:
            steps[step] = {
                'deps': [],
            }

        steps[step]['deps'].append(finished)

        if finished not in deps:
            deps[finished] = {
                'leads': [],
            }

        deps[finished]['leads'].append(step)

    start = set((seen.keys()) - set(steps.keys()))
    end = set((seen.keys()) - set(deps.keys())).pop()
    ready = {}

    for obj in start:
        ready[obj] = True

    heap = list(start)
    heapify(heap)
    seen = {}
    s = ''
    from_ = {}

    while heap:
        current = heappop(heap)
        ready[current] = True
        print("current", current)

        if current not in deps:
            continue

        if current in from_:
            print('from ', from_[current])

        s += current

        for n in deps[current]['leads']:
            is_ready = True

            for prev in steps[n]['deps']:
                print("checking ", prev)
                if prev not in ready:
                    print("   NOT READY")
                    is_ready = False

            if is_ready and n not in heap:
                print(" + adding to heap, ", n)
                heappush(heap, n)
                from_[n] = current

    s += end
    return s


def assembly_in_parallel(f, workers):
    steps = {}
    deps = {}
    seen = {}

    for s in f.readlines():
        parts = s.strip().split()
        finished = parts[1]
        step = parts[7]
        seen[step] = True
        seen[finished] = True

        if step not in steps:
            steps[step] = {
                'deps': [],
            }

        steps[step]['deps'].append(finished)

        if finished not in deps:
            deps[finished] = {
                'leads': [],
            }

        deps[finished]['leads'].append(step)

    start = set((seen.keys()) - set(steps.keys()))
    end = set((seen.keys()) - set(deps.keys())).pop()
    ready = {}

    for obj in start:
        ready[obj] = True

    workers_busy_for = [0] * workers
    workers_heap = heapify(workers_busy_for)





def test_assembly_instructions():
    assert assembly_instructions(open('input/07.test')) == 'CABDFE'


def test_assembly_in_parallel():
    assert assembly_in_parallel(open('input/07.test'), 2) == 15


if __name__ == '__main__':
    print(assembly_instructions(open('input/07')))

