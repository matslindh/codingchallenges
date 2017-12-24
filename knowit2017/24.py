import re
from collections import deque
from heapq import heappush, heappop


def find_shortest_path(inp, n):
    portals = {}
    groups = re.findall(r'\((\d+),(\d+)\)\s*->\s*\((\d+),(\d+)', inp)

    for x, y, target_x, target_y in groups:
        x = int(x)
        y = int(y)
        
        if y not in portals:
            portals[y] = {}
            
        portals[y][x] = {
            'x': x,
            'y': y,
            'target_x': int(target_x),
            'target_y': int(target_y),
            'shortest': int(x) + int(y) + 1,
            'in_list': False
        }

    not_done = []

    heappush(not_done, (0, 0, {
        'x': 0,
        'y': 0,
        'target_x': 0,
        'target_y': 0,
        'shortest': 0,
    }))
    
    if n - 1 not in portals:
        portals[n - 1] = {}
        
    portals[n - 1][n - 1] = {
        'x': n-1,
        'y': n-1,
        'target_x': n-1,
        'target_y': n-1,
        'shortest': n*2,
        'in_list': False,
    }

    c = 0
    
    while not_done:
        prio, _, this = heappop(not_done)
        this['in_list'] = False
        
        for y in portals:
            for x in portals[y]:
                portal = portals[y][x]
                d = abs(x - this['target_x']) + abs(y - this['target_y'])

                if this['shortest'] + d < portal['shortest']:
                    portal['shortest'] = this['shortest'] + d
                    if not portal['in_list']:
                        portal['in_list'] = True
                        c += 1
                        heappush(not_done, (portal['shortest'], c, portal))

        if len(not_done) % 100 == 0:
            print(len(not_done))
                
    return portals[n-1][n-1]['shortest']

    
def test_find_shortest_path():
    assert 8 == find_shortest_path(open("input/dec24_test").read(), 20)


if __name__ == "__main__":
    print(find_shortest_path(open("input/dec24").read(), 10000))
    


