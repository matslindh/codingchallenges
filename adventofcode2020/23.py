def play(cups, iterations=100):
    idx = 0
    
    while True:
        idx = (idx + 1) % len(cups)
    

def extract(cups, idx):
    end = (idx + 3) % len(cups)
    start_idx = idx
        
    if end < idx:
        if end == 4:
            to_insert = cups[0:4]
            del cups[0:4]
        else:
            to_insert = cups[idx:] + cups[0:end]
            del cups[idx:]
            del cups[0:end]
    else:
        to_insert = cups[idx:idx+3]
        del cups[idx:idx+3]
        
    return to_insert


def test_extract():
    l = [1, 2, 3, 4, 5, 6]
    assert extract(l, 0) == [1, 2, 3]
    assert l == [4, 5, 6]

    l = [1, 2, 3, 4, 5, 6]
    assert extract(l, 5) == [6, 1, 2]
    assert l == [3, 4, 5]

    l = [1, 2, 3, 4, 5, 6]
    assert extract(l, 4) == [5, 6, 1]
    assert l == [2, 3, 4]

    
