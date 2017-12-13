def calculate_firewall_cost(firewall, delay=0):
    layers = max(firewall.keys()) + 1
    hits = []
    
    for iteration in range(delay, layers+delay):
        if iteration not in firewall:
            continue
            
        period = (firewall[iteration] - 1) * 2

        if iteration % period == 0:
            hits.append(iteration * firewall[iteration])
            
    return sum(hits)


def find_first_passable_iteration(firewall):
    for delay in range(0, 10000):
        if calculate_firewall_cost(firewall, delay=delay) == 0:
            return delay
    
    
def test_calculate_firewall_cost():
    assert 24 == calculate_firewall_cost({0: 3, 1: 2, 4: 4, 6: 4})


def test_calculate_firewall_delay():
    assert 10 == find_first_passable_iteration({0: 3, 1: 2, 4: 4, 6: 4})


if __name__ == "__main__":
    inp = {}
    
    for line in open("input/dec13").readlines():
        vals = [int(x) for x in line.strip().split(': ')]
        
        if vals:
            inp[vals[0]] = vals[1]
            
    print(calculate_firewall_cost(inp))

    for i in range(0, 10000):
        res = calculate_firewall_cost(inp, delay=i)
        
        if res == 0:
            print(i)
            break

