import math
from PIL import (
    Image
)


def map_it(c):
    if c == '0':
        return 0, 0, 0

    if c == '1':
        return 255, 255, 255

    return 255, 0, 0


data = open('input/img.txt').read()
im_data = list(map(map_it, data))
data_len = len(data)

for x in range(100, int(math.sqrt(data_len))):
    if data_len % x == 0:
        height = x
        width = data_len // x

        im = Image.new(mode='RGB', size=(width, height))
        im.putdata(im_data)
        im.save(open('output/foo_' + str(width) + 'x' + str(height) + '.png', 'wb'))

