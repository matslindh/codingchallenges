fib = [1, 1]
sum = 0

while True:
    n = fib[0] + fib[1]
    fib.append(n)
    fib.pop(0)
    print(n)

    if n >= 4000000000:
        break

    if n % 2 == 0:
        sum += n
        print('S: ' + str(sum))

print(sum)
