from collections import defaultdict


def find_ingredients_without_allergens(definitions):
    defs = []
    all_ingredients = []

    for definition in definitions:
        ing_by_allergens = defaultdict(set)
        all_ingredients.extend(definition['ingredients'])

        for allergen in definition['allergens']:
            for ing in definition['ingredients']:
                ing_by_allergens[allergen].add(ing)

        defs.append(ing_by_allergens)

    possible = {}

    for instr in defs:
        for allergen, vals in instr.items():
            if allergen in possible:
                possible[allergen] &= vals
            else:
                possible[allergen] = vals

    changed = True

    while changed:
        changed = False

        for _, s in possible.items():
            if len(s) == 1:
                my_value = next(iter(s))

                for _, s_i in possible.items():
                    if len(s_i) > 1 and my_value in s_i:
                        s_i.remove(my_value)
                        changed = True

    all_possible = set()

    for _, s in possible.items():
        all_possible |= s

    return [x for x in all_ingredients if x not in all_possible], possible


def load_allergen_definitions_from_file(f):
    defs = []

    for line in [x.strip() for x in open(f)]:
        parts = line.split('(contains ')
        ingredients = set([x.strip() for x in parts[0].split(' ') if x.strip()])
        allergens = set()

        if len(parts) > 1:
            allergens = set([x.strip() for x in parts[1][:-1].split(',')])

        defs.append({
            'ingredients': ingredients,
            'allergens': allergens,
        })

    return defs


def test_load_allergen_definitions_from_file():
    defs = load_allergen_definitions_from_file('input/21.test')
    assert len(defs) == 4
    assert defs[0]['ingredients'] == {'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'}
    assert defs[0]['allergens'] == {'dairy', 'fish'}


def test_find_ingredients_without_allergens():
    defs = load_allergen_definitions_from_file('input/21.test')
    ings = find_ingredients_without_allergens(defs)
    assert len(ings) == 5


if __name__ == '__main__':
    defs = load_allergen_definitions_from_file('input/21')
    all_possible, possible_allergens = find_ingredients_without_allergens(defs)
    ingr_sorted = []

    for k, s in sorted(possible_allergens.items(), key=lambda x: x[0]):
        ingr_sorted.append(next(iter(s)))

    print(len(all_possible), ','.join(ingr_sorted))

