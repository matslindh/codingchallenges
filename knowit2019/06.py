from PIL import Image


def xorify_image(inp, out):
    im = Image.open(inp)
    pixels = im.getdata()
    pixelsNew = im.load()
    fixed = xorify_list(list(pixels))

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixelsNew[i,j] = tuple(fixed[j * im.size[1] + i])

    im.save(out)


def xorify_list(l):
    output = []

    for p_idx, p in enumerate(l):
        if p_idx == 0:
            output.append(list(p))
            continue

        row = []

        for idx in range(0, len(p)):
            row.append(l[p_idx][idx] ^ output[p_idx-1][idx])

        output.append(row)

    return output


def test_xorify_list():
    assert [[240, 33, 11], [61, 78, 109], [69, 46, 106], [104, 45, 160], [36, 192, 143]] == xorify_list([[240, 33, 11], [205, 111, 102], [120, 96, 7], [45, 3, 202], [76, 237, 47]])


if __name__ == '__main__':
    xorify_image('input/06.png', 'output/06.png')