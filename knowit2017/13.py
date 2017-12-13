def generate_sequence(n):
    seq = [False]

    while len(seq) < n:
        seq += [not x for x in seq]
        
    return seq[:n]


def split_loot(loot):
    loot = sorted(loot, reverse=True)
    seq = generate_sequence(len(loot))   
    vals = [0, 0]

    for i, val in enumerate(seq):
        idx = int(val)
        vals[idx] += loot[i]

    return vals

    
def test_generate_sequence():
    assert [False] == generate_sequence(1)
    assert [False, True] == generate_sequence(2)
    assert [False, True, True, False] == generate_sequence(4)
    assert [False, True, True, False, True, False, False, True] == generate_sequence(8)

def test_split_loot():
    assert [10, 9] == split_loot([1, 1, 5, 3, 4, 3, 1, 1])


if __name__ == "__main__":
    loot = []

    for line in open("input/dec13").readlines():
        loot.append(int(line.strip().split(', ')[1]))
        
    print(split_loot(loot))
