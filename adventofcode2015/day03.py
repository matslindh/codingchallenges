from collections import defaultdict


def run(instructions, actor_count=1):
    lookup = defaultdict(int)
    actors = []

    for _ in range(actor_count):
        actors.append([0, 0])

    lookup[0, 0] = 1

    for idx, instr in enumerate(instructions):
        actor = actors[idx%actor_count]

        if instr == '^':
            actor[1] -= 1
        elif instr == 'v':
            actor[1] += 1
        elif instr == '>':
            actor[0] += 1
        elif instr == '<':
            actor[0] -= 1

        lookup[(actor[0], actor[1])] += 1

    return lookup


def test_run():
    assert len(run(">")) == 2
    assert len(run("^>v<")) == 4
    assert len(run("^v^v^v^v^v")) == 2


def test_run_multiple_actors():
    assert len(run("^v", actor_count=2)) == 3
    assert len(run("^>v<", actor_count=2)) == 3
    assert len(run("^v^v^v^v^v", actor_count=2)) == 11


if __name__ == '__main__':
    print(len(run(open("input/03").read())))
    print(len(run(open("input/03").read(), actor_count=2)))