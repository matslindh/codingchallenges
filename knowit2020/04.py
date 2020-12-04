from collections import Counter
from math import floor


def read_delivery_list(path):
    c = Counter()
    sorry_for_list_comprehension_hell = [[[z.strip() for z in y.split(':')] for y in x.split(',')] for x in open(path).readlines()]

    for delivery in sorry_for_list_comprehension_hell:
        for ingredient, count in delivery:
            c.update({ingredient: int(count)})

    return c


def the_great_bakeoff(ingredients):
    requirements = {
        'sukker': 2,
        'mel': 3,
        'melk': 3,
        'egg': 1,
    }

    return min([floor(cnt / requirements[ing]) for ing, cnt in ingredients.items()])


def test_read_delivery_lines():
    products = read_delivery_list('input/04.test')

    assert products['melk'] == 56
    assert products['egg'] == 44
    assert products['mel'] == 35
    assert products['sukker'] == 108


def test_the_great_bakeoff():
    assert 11 == the_great_bakeoff(read_delivery_list('input/04.test'))


if __name__ == '__main__':
    print(the_great_bakeoff(read_delivery_list('input/04')))
