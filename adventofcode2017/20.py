import re
from math import sqrt

def parse_particles(lines):
    particles = []

    for line in lines:
        res = re.findall(r'<(.*?)>', line)

        if len(res) != 3:
            print("wtf ", line)
            return

        p = [int(x) for x in res[0].split(',')]
        v = [int(x) for x in res[1].split(',')]
        a = [int(x) for x in res[2].split(',')]

        particles.append((p, v, a))

    return particles

def find_closest(lines):
    particles = parse_particles(lines)

    best = None
    least_accel = 99999999

    for idx, particle in enumerate(particles):
        p, v, a = particle[0], particle[1], particle[2]
        accel = abs(sqrt(a[0]**2 + a[1]**2 + a[2]**2))

        if accel < least_accel:
            best = idx
            least_accel = accel
            
    return best
    

def find_alive(lines):
    particles = parse_particles(lines)

    parts = dict(enumerate(particles))
    prev_len = None
    identical_len_count = 0

    while True:
        occupied = {}

        for k in list(parts.keys()):
            ke = str(parts[k][0][0]) + ',' + str(parts[k][0][1]) + ',' + str(parts[k][0][2])

            if ke in occupied:
                if occupied[ke] in parts:
                    del parts[occupied[ke]]

                del parts[k]
                continue

            occupied[ke] = k

            parts[k][1][0] += parts[k][2][0]
            parts[k][1][1] += parts[k][2][1]
            parts[k][1][2] += parts[k][2][2]
            
            parts[k][0][0] += parts[k][1][0]
            parts[k][0][1] += parts[k][1][1]
            parts[k][0][2] += parts[k][1][2]
            
        l = len(parts)
        
        if l == prev_len:
            identical_len_count += 1
        else:
            prev_len = l
            identical_len_count = 0


        if identical_len_count > 20:
            return l


def test_find_closest():
    assert 0 == find_closest(open("input/dec20_test").readlines())
    assert 1 == find_alive(open("input/dec20_test_b").readlines())
    

if __name__ == "__main__":
    print(find_closest(open("input/dec20").readlines()))
    print(find_alive(open("input/dec20").readlines()))
