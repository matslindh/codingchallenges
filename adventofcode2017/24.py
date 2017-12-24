def build_bridge(parts):
    container = {}
    
    for part in parts:
        p1, p2 = [int(x) for x in part.strip().split('/')]
        item = {
            'name': str(p1) + '/' + str(p2),
            'p1': p1,
            'p2': p2,
            'weight': p1 + p2,
            'used': False,
        }

        if p1 not in container:
            container[p1] = []
            
        if p2 not in container:
            container[p2] = []

        container[p1].append(item)
        container[p2].append(item)

    best = {'length': 0, 'weight': 0}

    def bridge_it(port_size, weight, sequence):
        weights = []
        
        for item in container[port_size]:
            if item['used']:
                continue

            sequence.append(item['name'])                
            item['used'] = True

            if item['p1'] == port_size:
                weights.append(bridge_it(item['p2'],  weight + item['weight'], sequence))
            elif item['p2'] == port_size:
                weights.append(bridge_it(item['p1'], weight + item['weight'], sequence))
                
            item['used'] = False
            sequence.pop()

        if not weights:
            if len(sequence) > best['length'] or (len(sequence) == best['length'] and weight > best['weight']):
                best['length'] = len(sequence)
                best['weight'] = weight

            return weight

        return max(weights)

    return bridge_it(0, 0, []), best


def test_build_bridge():
    assert 31 == build_bridge(open("input/dec24_test").readlines())


if __name__ == "__main__":
    print(build_bridge(open("input/dec24").readlines()))
