def cut_trees(trees):
    cut = []
    
    while trees:
        cut.append(len(trees))
        lowest = min(trees)
        
        trees = [tree - lowest for tree in trees if (tree - lowest) > 0]

    return cut

def test_cut_trees():
    assert [6, 4, 2, 1] == cut_trees([5, 4, 4, 2, 2, 8])


if __name__ == "__main__":
    cut = cut_trees([23, 74, 26, 23, 92, 92, 44, 13, 34, 23, 69, 4, 19, 94, 94, 38, 14, 9, 51, 98, 72, 46, 17, 25, 21, 87, 99, 50, 59, 53, 82, 24, 93, 16, 88, 52, 14, 38, 27, 7, 18, 81, 13, 75, 80, 11, 29, 39, 37, 78, 55, 17, 78, 12, 77, 84, 63, 29, 68, 32, 17, 55, 31, 30, 3, 17, 99, 6, 45, 81, 75, 31, 50, 93, 66, 98, 94, 59, 68, 30, 98, 57, 83, 75, 68, 85, 98, 76, 91, 23, 53, 42, 72, 77])
    cut = [str(x) for x in cut]
    
    print(', '.join(cut))
