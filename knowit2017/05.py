def sum_up_to(n):
    values = [0] * 1000000
    values[0] = 1
    values[1] = 2
    read = 0
    write = 0

    for i in range(0, n):
        done = False
        # print('reading at ' + str(read))

        for j in range(0, values[read]):
            idx = write + j
            
            if idx >= n:
                done = True
                break
                
            w = values[read]
            # print("values[" + str(idx) + "] = " + str(w) +  ", " + str(write) + ", " + str(j))
            values[idx] = read + 1
   
        if done:
            break
            
        write += values[read]
        read += 1

    return sum(values[0:n])

def test_sum_up_to():
    assert sum_up_to(2) == 3
    assert sum_up_to(5) == 11   

if __name__ == '__main__':
    print('n: ' + str(sum_up_to(1000000)))
    print('n+1: ' + str(sum_up_to(1000001)))
    print('n-1: ' + str(sum_up_to(999999)))
