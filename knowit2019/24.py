from PIL import Image, ImageDraw

w = 5120
h = 512
img = Image.new('RGB', (w, h), color='black')
img_draw = ImageDraw.Draw(img)
char = []

def draw_char(char, offset):
    print(offset)
    char_w = sorted(char, reverse=True)[0][0] + 1

    for x, y in char:
        img_draw.point((x + offset, h - y), 'white')

    return char_w

offset = 0

for line in open("input/turer.txt").readlines():
    line = line.strip()
    
    if line == '---':
        offset += draw_char(char, offset)
        char = []
        continue

    char.append([int(c) for c in line.split(',')])
        
img.save('output/24.png')

