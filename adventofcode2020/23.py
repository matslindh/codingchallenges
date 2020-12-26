def play(cups, iterations=100):
    idx = 0
    
    while iterations:
        current = cups[idx]
        extracted = extract(cups, (idx + 1) % len(cups))
        print(current, cups, extracted)
        dest_idx = None

        while True:
            current -= 1
            
            if current < 1:
                current = 9

            try:
                dest_idx = cups.index(current)
                break
            except ValueError:
                continue
        
        cups = cups[:dest_idx+1] + extracted + cups[dest_idx+1:]
        idx = (idx + 1) % len(cups)

        print(cups)    
        iterations -= 1

    return cups


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


def order_after_one(cups):
    idx = cups.index(1)
    print(idx)
    return cups[idx+1:] + cups[:idx]


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


def test_play():
    cups = [int(x) for x in '389125467']
    assert play(cups, 1) == [int(x) for x in '328915467']


def test_order_after_one():
    assert order_after_one([int(x) for x in '328915467']) == [int(x) for x in '54673289']


def test_play_and_order():
    cups = [int(x) for x in '389125467']    
    assert order_after_one(play(cups, 9)) == [int(x) for x in '92658374']
    assert order_after_one(play(cups)) == [int(x) for x in '67384529']
