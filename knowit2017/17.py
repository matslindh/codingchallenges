n = 46

for i in range(0, 1000000):
    n += 100
    
    s_n = str(n)
    n_2 = int('6' + s_n[:-1])

    if n * 4 == n_2:
        print(n)
        break
        

