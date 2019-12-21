def generate_generational_generations(inp):
    lines = [line.strip() for line in open(inp).readlines()]
    generations = []

    for gen_idx, line in enumerate(lines):
        generation = []
        
        for inherit_idx, inheritance in enumerate(line.split(';')):
            generation.append({
                'me': (gen_idx, inherit_idx),
                'parents': [(gen_idx + 1, int(parent)) for parent in inheritance.split(',')],
                'lineage': {(gen_idx, inherit_idx)} if gen_idx == 0 else set(),
                'visit_count': 0,
            })

        generations.append(generation)
            
    return generations


def explore_generations(generations):
    queue = []
    max_c = len(generations[0]) // 2
    last_gen = 0
    best_visit_count = 0
    doners = []
    done = False

    for initial in generations[0][1::2]:
        queue.append(initial['me'])

    while len(queue):
        gen, idx = queue.pop(0)

        if gen > last_gen:
            last_gen = gen

            if done:
                print("DONE BY")
                print(sorted(doners))
                return

            print("New generation: " + str(last_gen))

        me = generations[gen][idx]

        p_l_l = len(me['lineage'])

        if p_l_l > best_visit_count:
            best_visit_count = p_l_l
            print(str(best_visit_count) + ', ' + str(me['me']))

        if p_l_l >= max_c:
            done = True
            doners.append(me['me'])

        for p in me['parents']:
            parent = generations[p[0]][p[1]]

            if not parent['lineage']:
                queue.append(p)

            parent['lineage'] |= me['lineage']


if __name__ == '__main__':
    import time
    start = time.time()
    print('Generations generation')
    generations = generate_generational_generations('input/generations.txt')
    print("Exploring")
    explore_generations(generations)
    print(time.time() - start)
