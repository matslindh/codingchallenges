def dragon_lives_for(sequence):
    dragon_size = 50
    sheep = 0
    squeezed_for = 0
    days = 0
    
    while True:
        sheep += sequence.pop(0)
    
        if dragon_size <= sheep:
            sheep -= dragon_size
            dragon_size += 1
            squeezed_for = 0
        else:
            sheep = 0
            dragon_size -= 1
            squeezed_for += 1    
    
        if squeezed_for >= 5:
            return days

        days += 1


def test_dragon_lives_for():
    assert dragon_lives_for([50, 52, 52, 49, 50, 47, 45, 43, 50, 55]) == 7


if __name__ == '__main__':
    with open('input/01') as f:
        l = [int(v) for v in f.read().split(', ')]
        print(dragon_lives_for(l))
