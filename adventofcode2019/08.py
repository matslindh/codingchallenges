def decode_space_image_format(data, w, h):
    data = list(map(int, data))
    layers = []

    while data:
        layer = []
        
        for y in range(h):
            row = []

            for x in range(w):    
                row.append(data[y * w + x])
            
            layer.append(row)
        
        data = data[h*w:]
        layers.append(layer)

    return layers


def output_image(layers):
    h, w = len(layers[0]), len(layers[0][0])

    for y in range(h):
        output = ''
        
        for x in range(w):
            l = len(output)
        
            for layer in layers:
                if layer[y][x] == 0:
                    output += '#'
                    break
                if layer[y][x] == 1:
                    output += ' '
                    break
            
            if len(output) == l:
                output += '.'
                
        print(output)

            
def test_decode_space_image_format():
    assert [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]] == decode_space_image_format('123456789012', w=3, h=2)
    

if __name__ == '__main__':
    layers = decode_space_image_format(open('input/08').read().strip(), w=25, h=6)
    from collections import Counter
    least_zeroes = 99999
    least_zeros_layer = None

    for layer in layers:
        c = Counter()
        
        for row in layer:
            c.update(row)
       
        if c[0] < least_zeroes:
            least_zeroes = c[0]
            least_zeroes_layer = layer, c     

    c = least_zeroes_layer[1]
    print(c[1] * c[2])

    output_image(layers)
