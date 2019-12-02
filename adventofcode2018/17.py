from PIL import Image

def make_it_flow(f):
    clay = []

    for line in f.readlines():
        params = {}

        for param in [x.strip().strip(',') for x in line.split(' ')]:
            dir, values = param.split('=')
            params[dir] = values

        if '..' in params['x']:
            loop = [int(x) for x in params['x'].split('..')]
            y = int(params['y'])

            for x in range(loop[0], loop[1] + 1):
                clay.append((x, y))
        elif '..' in params['y']:
            loop = [int(y) for y in params['y'].split('..')]
            x = int(params['x'])

            for y in range(loop[0], loop[1] + 1):
                clay.append((x, y))
        else:
            clay.append((int(params['x']), int(params['y'])))

    ys = [y for x, y in clay]
    xs = [x for x, y in clay]

    min_y = min(ys)
    max_y = max(ys) + 3

    min_x = min(xs)
    max_x = max(xs) + 2

    buffer = Image.new('RGB', (max_x + 2, max_y + 2))

    for c in clay:
        buffer.putpixel(c, (255, 0, 0))

    buffer.putpixel((500, 0), (255, 255, 0))
    data = {
        'idx': 0,
    }

    def flow_it(x, y):
        pop_x = x
        pop_y = y
        print("starting flow from ", pop_x, pop_y)
        active_flows = []

        x = pop_x
        y = pop_y

        while buffer.getpixel((x, y)) == (0, 0, 0) and y <= max_y:
            active_flows.append((x, y))
            buffer.putpixel((x, y), (0, 0, 255))
            y += 1

        if y != pop_y:
            print(" - Downflow from ", str((x, pop_y)), " to ", str((x, y)))

        if y > max_y:
            print("found end")
            return True

        found_end = False

        while active_flows:
            start_x, start_y = active_flows.pop()
            print(" ! Flowing from ", start_x, start_y)

            x = start_x - 1
            y = start_y

            while buffer.getpixel((x, y)) == (0, 0, 0):
                buffer.putpixel((x, y), (0, 0, 255))

                if buffer.getpixel((x, y+1)) == (0, 0, 0):
                    if flow_it(x, y+1):
                        found_end = True

                    break

                x -= 1

            if x != start_x - 1:
                print(" - Leftflow from ", str((start_x - 1, y)), " to ", str((x + 1, y)))

            x = start_x + 1
            y = start_y

            while buffer.getpixel((x, y)) == (0, 0, 0) and x < max_x:
                buffer.putpixel((x, y), (0, 0, 255))

                if buffer.getpixel((x, y+1)) == (0, 0, 0):
                    if flow_it(x, y+1):
                        found_end = True

                    break

                x += 1

            if x != start_x + 1:
                print(" - Rightflow from ", str((start_x + 1, y)), " to ", str((x - 1, y)))

            if found_end:
                break

        return found_end

    flow_it(500, 1)
    buffer.save("output/17.png")

    pass


def test_make_it_flow():
    assert make_it_flow(open('input/17.test')) == 57


if __name__ == '__main__':
    print(make_it_flow(open('input/17')))