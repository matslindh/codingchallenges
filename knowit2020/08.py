from cachetools import cached

cities = {}


def city_builder(f):
    lines = [x.strip() for x in open(f).readlines()]
    mode = 'cities'
    itinerary = []

    for line in lines:
        if mode == 'cities' and ':' not in line:
            mode = 'itinerary'

        if mode == 'cities':
            name, coords = line.split(':')
            x, y = [int(x.strip()) for x in coords[2:-1].split(',')]

            cities[name] = {
                'x': x,
                'y': y,
                'time': 0.0,
            }
        else:
            itinerary.append(line)

    x = 0
    y = 0

    for city_name in itinerary:
        city = cities[city_name]

        while x != city['x']:
            x += 1 if x < city['x'] else -1

            update_time(x, y)

        while y != city['y']:
            y += 1 if y < city['y'] else -1

            update_time(x, y)

    return max([x['time'] for x in cities.values()]) - min([x['time'] for x in cities.values()])


def update_time(x, y):
    for city, update in get_time_updates(x, y).items():
        cities[city]['time'] += update


@cached(cache={})
def get_time_updates(x, y):
    updates = {}

    for city, props in cities.items():
        dist = abs(x - props['x']) + abs(y - props['y'])

        if dist == 0:
            updates[city] = 0
        elif dist < 5:
            updates[city] = 0.25
        elif dist < 20:
            updates[city] = 0.5
        elif dist < 50:
            updates[city] = 0.75
        else:
            updates[city] = 1

    return updates


def test_city_builder():
    assert 0.25 == city_builder('input/08.test')


if __name__ == '__main__':
    print(city_builder('input/08'))
