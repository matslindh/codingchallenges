def distance(n):
    if n == 1:
        return 0
        
    c = 1
    layer = 0

    while c**2 <= n:
        c += 2
        layer += 1

    p_start = (c-2)**2
    p_ur = p_start + c - 1
    p_ul = p_ur + c - 1
    p_ll = p_ul + c - 1
    p_lr = p_ll + c - 1

    offset = layer

    if n < p_ur:
        offset = n - (p_ur - layer)
        # print(n, p_ur, layer, (p_ur - layer))
    elif n < p_ul:
        offset = n - (p_ul - layer)
    elif n < p_ll:
        offset = n - (p_ll - layer)
    elif n < p_lr:
        offset = n - (p_lr - layer)
    
    offset = abs(offset)
    # print(offset, layer, p_start, p_ur, p_ul, p_ll, p_lr, n, c, c**2)
    return layer + offset
    
def test_distance():
    assert 0 == distance(1)
    assert 3 == distance(12)
    assert 2 == distance(23)
    assert 31 == distance(1024)

if __name__ == "__main__":
    print(distance(289326))
