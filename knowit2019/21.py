def generate_generational_generations(inp):
    lines = [line.strip() for line in open(inp).readlines()]
    generations = []

    for gen_idx, line in enumerate(lines):
        generation = []
        
        for inheritance in line.split(';'):
            generation.append(
                [(gen_idx, int(parent)) for parent in inheritance.split(',')]
            )

        generations.append(generation)
            
    return generations


def parental_guidance(generations):
    parental = []

    for generation in generations[::-1]:
        parents = []

        for idx, individual in enumerate(generation):
            parent_set = set(individual)

            if parental:
                for parent in individual:
                    gen, elf = parent
                    print(gen, elf)
                    #parent_set |= parental[len(parental) - gen][elf]

            parents.append(parent_set)

        parental.append(parents)
    
    import pprint
    pprint.pprint(parental[len(parental) - 2])
    pprint.pprint(parental[len(parental) - 1])
    

def test_generational_gaps():
    generations = generate_generational_generations('input/generations.test.txt')
    parental_guidance(generations)
