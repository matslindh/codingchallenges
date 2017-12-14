def stair_ways(n):
    ways = [0] * n

    ways[0] = 1

    if n > 1:
        ways[1] = 1
        
    if n > 2:
        ways[2] = 1

    for p in range(0, n):
        if p + 1 < n:
            ways[p+1] += ways[p]
            
        if p + 2 < n:
            ways[p+2] += ways[p]
            
        if p + 3 < n:
            ways[p+3] += ways[p]
        
    return ways[n-1]

def test_stair_ways():
    assert 1 == stair_ways(1)
    assert 2 == stair_ways(2)
    assert 4 == stair_ways(3)


if __name__ == "__main__":
    print(stair_ways(30))
