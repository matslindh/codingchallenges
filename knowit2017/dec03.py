from PIL import Image

im = Image.open('input/dec03.png')
red = im.split()[0]

count = 0
bit = 0

for c in red.getdata():
    if c & 1:
        bit |= 1 << (count % 8)

    count += 1

    if count % 8 == 0:
        print(chr(bit), end='')
        bit = 0
            
    if count > 1024:
        break
