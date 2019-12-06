from PIL import Image


def xorify_image(inp, out):
    im = Image.open(inp)
    pixels = im.getdata()
    pixelsNew = im.load()
    fixed = xorify_list(list(pixels), op='decode')

    width, height = im.size

    for x in range(width):
        for y in range(height):
            pixelsNew[x,y] = tuple(fixed[y * width + x])

    im.save(out)


def xorify_list(l, op='encode'):
    output = [l[0]]

    for p_idx in range(1, len(l)):
        p = l[p_idx]
        row = []

        for idx in range(0, len(p)):
            if op == 'encode':
                row.append(l[p_idx][idx] ^ output[p_idx-1][idx])
            elif op == 'decode':
                row.append(l[p_idx][idx] ^ l[p_idx - 1][idx])

        output.append(row)

    return output


def test_xorify_list():
    assert [[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]] == xorify_list([[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]], op='encode')
    assert [[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]] == xorify_list([[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]], op='decode')


if __name__ == '__main__':
    xorify_image('input/06.png', 'output/06.png')