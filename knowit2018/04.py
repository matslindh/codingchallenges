from PIL import Image

im = Image.open('input/04.png')
red = im.split()[0]
width, height = im.size

count = 0


for c in red.getdata():
    count += 1
    print('x' if c & 1 == 0 else ' ', end='')

    if count == width:
        print("")
        count = 0
