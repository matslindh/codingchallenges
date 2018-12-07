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


def assembly_in_parallel(f, workers, duration=0):
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
    heap = []

    for obj in start:
        heap.append((0, obj))

    heapify(heap)
    s = ''

    workers_heap = [0] * workers
    heapify(workers_heap)

    while heap:
        earliest_start_at, current = heappop(heap)
        ready[current] = True
        # print("current", current)

        if current not in deps:
            continue

        wake_at = heappop(workers_heap)
        # print("wake_at", wake_at, "earliest_start_at", earliest_start_at)
        time = max(wake_at, earliest_start_at)
        heappush(workers_heap, duration + time + ord(current) - 64)
        # print("time is now", time)

        s += current

        for n in deps[current]['leads']:
            is_ready = True

            for prev in steps[n]['deps']:
                # print("checking ", prev)
                if prev not in ready:
                    # print("   NOT READY")
                    is_ready = False

            if is_ready and n not in heap:
                # print(" + adding to heap, ", n)
                heappush(heap, (duration + time + ord(current) - 64, n))

        print(heap)
        print(workers_heap)

    # - 63 since that's when everyone has finished
    return min(workers_heap) + ord(end) - 63


def test_assembly_instructions():
    assert assembly_instructions(open('input/07.test')) == 'CABDFE'


def test_assembly_in_parallel():
    assert assembly_in_parallel(open('input/07.test'), 2) == 15


if __name__ == '__main__':
    print(assembly_instructions(open('input/07')))

    # 554 too low
    print(assembly_in_parallel(open('input/07'), 5, 60))

